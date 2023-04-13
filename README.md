# Fatest JSON Python module

Run Python JSON benchmarks to find the fastest module that can be used as a drop-in replacement of the `json` standard one.

Benchmarks are run from a [GitHub workflow](.github/workflows/benchmark.yml).

See the [requirements.txt](requirements.txt) file for exact modules being tested, and [which imports](bench-json.py#L9) are being used in the benchmark script.

## Results

Current cross-versions winner: `python-rapidjson` :tada:

### Python 3.12

```bash
Python 3.12.0a7
    json        loads: 2.676 x1.0 | dumps: 4.561 x1.0 ✅
    fast_json   loads: 2.151 x0.8 | dumps: 5.842 x1.3 ❌
    rapidjson   loads: 2.128 x0.8 | dumps: 2.121 x0.5 ✅
    simplejson  loads: 24.037 x9.0 | dumps: 28.560 x6.3 ❌
    ujson       loads: 2.184 x0.8 | dumps: 2.597 x0.6 ✅

Potential candidates = 'rapidjson, ujson'
```

### Python 3.11

```bash
Python 3.11.3
    json        loads: 2.880 x1.0 | dumps: 4.389 x1.0 ✅
    fast_json   loads: 1.990 x0.7 | dumps: 5.697 x1.3 ❌
    rapidjson   loads: 2.065 x0.7 | dumps: 1.772 x0.4 ✅
    simplejson  loads: 3.221 x1.1 | dumps: 9.158 x2.1 ❌
    ujson       loads: 1.985 x0.7 | dumps: 2.282 x0.5 ✅

Potential candidates = 'rapidjson, ujson'
```

### Python 3.10

```bash
Python 3.10.11
    json        loads: 3.652 x1.0 | dumps: 5.241 x1.0 ✅
    fast_json   loads: 2.415 x0.7 | dumps: 6.978 x1.3 ❌
    rapidjson   loads: 2.217 x0.6 | dumps: 1.908 x0.4 ✅
    simplejson  loads: 4.008 x1.1 | dumps: 10.494 x2.0 ❌
    ujson       loads: 2.351 x0.6 | dumps: 2.343 x0.4 ✅

Potential candidates = 'rapidjson, ujson'
```

### Python 3.9

```bash
Python 3.9.16
    json        loads: 3.271 x1.0 | dumps: 4.765 x1.0 ✅
    fast_json   loads: 2.150 x0.7 | dumps: 6.435 x1.4 ❌
    rapidjson   loads: 2.116 x0.6 | dumps: 1.868 x0.4 ✅
    simplejson  loads: 3.752 x1.1 | dumps: 8.030 x1.7 ❌
    ujson       loads: 2.176 x0.7 | dumps: 2.180 x0.5 ✅

Potential candidates = 'rapidjson, ujson'
```

### Python 3.8

```bash
Python 3.8.16
    json        loads: 3.359 x1.0 | dumps: 4.779 x1.0 ✅
    fast_json   loads: 2.077 x0.6 | dumps: 6.900 x1.4 ❌
    rapidjson   loads: 2.253 x0.7 | dumps: 1.921 x0.4 ✅
    simplejson  loads: 3.973 x1.2 | dumps: 8.552 x1.8 ❌
    ujson       loads: 2.149 x0.6 | dumps: 2.606 x0.5 ✅

Potential candidates = 'rapidjson, ujson'
```

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
