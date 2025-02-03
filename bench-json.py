"""Run JSON benchmarks on given modules."""

import sys
from collections import namedtuple
from timeit import timeit

# XXX: here you set which modules you want to benchmark
MODULES_TO_TEST = [
    "fast_json",
    "orjson",
    "pyjson5",
    "rapidjson",
    "simdjson",
    "simplejson",
    "ujson",
]
MODULE_REF = "json"

RAW = (
    '[["uint256", "amountOutMin", 235921602440841030081], ["address[]", "path", ["0x'
    'b31f66aa3c1e785363f0875a1b74e27b85fd66c7", "0x3df307e8e9a897da488211682430776cd'
    'f0f17cc"]], ["address", "to", "0x6ef4158bf7304b966929945248927fb400ece8b5"], ["'
    'uint256", "deadline", 1647035873]]'
)
FORMATED = [
    ["uint256", "amountOutMin", 235921602440841030081],
    [
        "address[]",
        "path",
        [
            "0xb31f66aa3c1e785363f0875a1b74e27b85fd66c7",
            "0x3df307e8e9a897da488211682430776cdf0f17cc",
        ],
    ],
    ["address", "to", "0x6ef4158bf7304b966929945248927fb400ece8b5"],
    ["uint256", "deadline", 1647035873],
]

Ref = namedtuple("Ref", "loads, dumps")


def run(stmt: str, setup: str) -> float:
    try:
        timeit(setup=setup, number=1)
    except (AssertionError, ImportError, OverflowError, TypeError, ValueError):
        return 0.0
    return timeit(stmt=stmt, setup=setup)


def res(value: float, justification: int = 6) -> str:
    text = f"{value:.3f}" if value else "-.---"
    return text.rjust(justification)


def coef(value: float, justification: int = 5) -> str:
    if not value:
        return "x-.-".rjust(justification)
    color = "33" if value == 1.0 else "31" if value > 1.0 else "32"
    text = f"x{value:.1f}".rjust(justification)
    return f"\033[{color}m{text}\033[0m"


def is_potential_candidate(loads_coef: float, dumps_coef: float) -> bool:
    return 0.0 < loads_coef <= 1.0 and 0.0 < dumps_coef <= 1.0


def potential_candidate(good: bool) -> str:
    color, text = ("32", "✅") if good else ("31", "❌")
    return f"\033[{color}m{text}\033[0m"


def benchmark(*implementations: str) -> None:
    candidates: list[tuple[bool, str, float, float, float, float]] = []
    reference = None
    justify = len(max(implementations, key=len))

    for impl in implementations:
        loads = run(
            "loads(RAW)",
            "; ".join(
                [
                    f"from {impl} import loads",
                    "from __main__ import FORMATED, RAW",
                    "assert loads(RAW) == FORMATED",
                ]
            ),
        )
        dumps = run(
            "dumps(FORMATED)",
            "; ".join(
                [
                    f"from {impl} import dumps",
                    "from __main__ import FORMATED",
                    "assert isinstance(dumps(FORMATED), str)",
                ]
            ),
        )

        if reference is None:
            reference = Ref(loads, dumps)
            candidates.append((False, impl, loads, 1.0, dumps, 1.0))
        else:
            loads_coef = loads / reference.loads or 10
            dumps_coef = dumps / reference.dumps or 10
            is_candidate = is_potential_candidate(loads_coef, dumps_coef)
            candidates.append(
                (not is_candidate, impl, loads, loads_coef, dumps, dumps_coef)
            )

    signs = {None: "!", True: "+", False: "-"}
    fmt = "{} {} loads: {} {} | dumps: {} {}"
    for is_candidate, impl, loads, loads_coef, dumps, dumps_coef in sorted(
        candidates, key=lambda c: (c[0], c[3] + c[5], c[1])
    ):
        if loads_coef >= 10:
            loads_coef = 0.0
        if dumps_coef >= 10:
            dumps_coef = 0.0
        if loads_coef + dumps_coef == 0.0:
            continue

        # Ugly, I know. But to simplify the previous `sorted()` call, `is_candidate` is True for non candidate implementations
        is_candidate = not is_candidate
        sign = signs[is_candidate if impl != MODULE_REF else None]
        print(
            fmt.format(
                sign,
                impl.ljust(justify, "…"),
                res(loads),
                coef(loads_coef),
                res(dumps),
                coef(dumps_coef),
            )
        )


def main() -> int:
    print("@@", "Python", ".".join(map(str, sys.version_info[:3])), "@@")

    all_modules = [MODULE_REF] + MODULES_TO_TEST
    benchmark(*all_modules)
    return 0


if __name__ == "__main__":
    sys.exit(main())
