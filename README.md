# Fatest JSON Python module

Run Python JSON benchmarks to find the fastest module that can be used as a drop-in replacement of the `json` standard one.

Benchmarks are run from a [GitHub workflow](.github/workflows/benchmark.yml).

See the [requirements.txt](requirements.txt) file for exact modules being tested, and [which imports](bench-json.py#L9) are being used in the benchmark script.

## Results

- GNU/Linux + macOS: current cross-versions winner is `python-rapidjson` :tada:
- Windows: current cross-versions winner is `ujson` :tada:

Have a look at detailled results for all currently supported Python versions: [GNU/Linux](results/linux.md), [macOS](results/mac.md), and [Windows](results/windows.md).

## Not An Option

- `cysimdjson`: not a drop-in replacement
- `hyperjson`: no more maintained, and the author recommands `orjson`
- `jsonlib2`: no more maintained
- `libpy_simdjson`: no wheel provided
- `metamagic.json`: no more maintained
- `orjson`: not a drop-in replacement
- `python-cjson`: no more maintained
- `simdjson`: not a drop-in replacement
- `yajl`: no more maintained
