# Fastest JSON Python module

Run Python JSON benchmarks to find the fastest module that can be used as a drop-in replacement of the `json` standard one.

Benchmarks are run from a [GitHub workflow](.github/workflows/benchmark.yml).

See the [requirements.txt](requirements.txt) file for exact modules being tested, and [which imports](bench-json.py#L9) are being used in the benchmark script.

## Results

- 🐧 [GNU/Linux](results/linux.md)
- 🍎 [macOS](results/mac.md)
- 🪟 [Windows](results/windows.md)

## Not An Option

### Incorrect Output

But they are still tested, in case their behavior changes over time.

- `orjson`
- `pysimdjson`

### Not a Drop-In Replacement

- `cysimdjson`

### No More Maintained

- `hyperjson`
- `jsonlib2`
- `libpy_simdjson`
- `metamagic.json`
- `python-cjson`
- `yajl`
