# Fastest JSON Python module

> [!TIP]
> Become **my boss** to help me work on this awesome software, and make the world better:
> 
> [![Patreon](https://img.shields.io/badge/Patreon-F96854?style=for-the-badge&logo=patreon&logoColor=white)](https://www.patreon.com/mschoentgen)

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
