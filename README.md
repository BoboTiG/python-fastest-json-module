# Fatest JSON Python module

Run Python JSON benchmarks to find the fastest module that can be used as a drop-in replacement of the `json` standard one.

Benchmarks are run from a [GitHub workflow](.github/workflows/benchmark.yml).

See the [requirements.txt](requirements.txt) file for exact modules being tested, and [which imports](bench-json.py#L9) are being used in the benchmark script.

## Results

Current cross-versions winner: `python-rapidjson` :tada:

### Python 3.12

```bash
```

### Python 3.11

```bash
```

### Python 3.10

```bash
```

### Python 3.9

```bash
```

### Python 3.8

```bash
```

## Not An Option

- `cysimdjson`: not a drop-in replacement
- `hyperjson`: no more maintained, and the author recommands `orjson`
- `jsonlib2`: no more maintained
- `libpy_simdjson`: no wheel provided
- `metamagic.json`: no more maintained
- `python-cjson`: no more maintained
- `yajl`: no more maintained
