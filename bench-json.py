"""Run JSON benchmarks on given modules."""
import sys
from collections import namedtuple
from timeit import timeit
from types import ModuleType
from typing import Any, Dict, List

# XXX: here you set which modules you want to benchmark
MODULES_TO_TEST = ["fast_json", "orjson", "rapidjson", "simdjson", "simplejson", "ujson"]

RAW = (
    '[["uint256", "amountOutMin", 235921602440841030081], ["address[]", "path", ["0x'
    'b31f66aa3c1e785363f0875a1b74e27b85fd66c7", "0x3df307e8e9a897da488211682430776cd'
    'f0f17cc"]], ["address", "to", "0x6ef4158bf7304b966929945248927fb400ece8b5"], ["'
    'uint256", "deadline", 1647035873]]'
)
FMT = [
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


def run_dumps(implementation: ModuleType) -> str:
    return implementation.dumps(FMT)


def run_loads(implementation: ModuleType) -> Dict[str, Any]:
    return implementation.loads(RAW)


def run(stmt: str, setup: str) -> float:
    try:
        return timeit(stmt=stmt, setup=setup)
    except (AssertionError, ImportError, OverflowError, TypeError, ValueError):
        return 0.0


def res(value: float) -> str:
    return f"{value:.3f}" if value else "-.---"


def coef(value: float) -> str:
    color = "33" if value == 1.0 else "31" if value > 1.0 else "32"
    return f"\033[{color}mx{value:.1f}\033[0m" if value else "x-.-"


def is_potential_candidate(loads_coef: float, dumps_coef: float) -> bool:
    return 0.0 < loads_coef <= 1.0 and 0.0 < dumps_coef <= 1.0


def potential_candidate(good: bool) -> str:
    color = "32" if good else "31"
    text = "✅" if good else "❌"
    return f"\033[{color}m{text}\033[0m"


def benchmark(*implementations: str) -> List[str]:
    candidates: List[str] = []
    reference = None
    justify = len(max(implementations, key=len)) + 1

    for impl in implementations:
        loads = run(
            f"run_loads({impl})",
            "; ".join(
                [
                    f"import {impl}",
                    "from __main__ import FMT, run_loads",
                    f"assert run_loads({impl})[0] == FMT[0]",
                ]
            ),
        )
        dumps = run(
            f"run_dumps({impl})",
            "; ".join(
                [
                    f"import {impl}",
                    "from __main__ import run_dumps",
                    f"assert isinstance(run_dumps({impl}), str)",
                ]
            ),
        )

        if not reference:
            reference = Ref(loads, dumps)
            loads_coef = dumps_coef = 1
            good = True
        else:
            loads_coef = loads / reference.loads
            dumps_coef = dumps / reference.dumps
            if good := is_potential_candidate(loads_coef, dumps_coef):
                candidates.append(impl)

        print(
            f"    {impl.ljust(justify)}",
            "loads:",
            res(loads),
            coef(loads_coef),
            "|",
            "dumps:",
            res(dumps),
            coef(dumps_coef),
            potential_candidate(good),
        )

    return candidates


def main() -> int:
    all_modules = ["json"] + sorted(MODULES_TO_TEST)
    candidates = ", ".join(benchmark(*all_modules))
    print(f"\nPotential {candidates = }")
    return int(not candidates)


if __name__ == "__main__":
    sys.exit(main())
