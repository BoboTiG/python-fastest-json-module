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
    orjson      loads: -.--- x-.- | dumps: -.--- x-.- ❌
    rapidjson   loads: 2.128 x0.8 | dumps: 2.121 x0.5 ✅
    simdjson    loads: -.--- x-.- | dumps: -.--- x-.- ❌
    simplejson  loads: 24.037 x9.0 | dumps: 28.560 x6.3 ❌
    ujson       loads: 2.184 x0.8 | dumps: 2.597 x0.6 ✅

Potential candidates = 'rapidjson, ujson'
```

### Python 3.11

```bash
 Python 3.11.2
    json        loads: 2.905 x1.0 | dumps: 4.393 x1.0 ✅
    fast_json   loads: 1.944 x0.7 | dumps: 5.643 x1.3 ❌
    orjson      loads: -.--- x-.- | dumps: -.--- x-.- ❌
    rapidjson   loads: 2.058 x0.7 | dumps: 1.741 x0.4 ✅
    simdjson    loads: -.--- x-.- | dumps: 4.436 x1.0 ❌
    simplejson  loads: 3.125 x1.1 | dumps: 9.215 x2.1 ❌
    ujson       loads: 1.970 x0.7 | dumps: 2.139 x0.5 ✅

Potential candidates = 'rapidjson, ujson'
```

### Python 3.10

```bash
Python 3.10.10
    json        loads: 3.850 x1.0 | dumps: 5.652 x1.0 ✅
    fast_json   loads: 2.517 x0.7 | dumps: 7.710 x1.4 ❌
    orjson      loads: -.--- x-.- | dumps: -.--- x-.- ❌
    rapidjson   loads: 2.458 x0.6 | dumps: 2.190 x0.4 ✅
    simdjson    loads: -.--- x-.- | dumps: 5.621 x1.0 ❌
    simplejson  loads: 4.256 x1.1 | dumps: 11.648 x2.1 ❌
    ujson       loads: 2.552 x0.7 | dumps: 2.717 x0.5 ✅

Potential candidates = 'rapidjson, ujson'
```

### Python 3.9

```bash
Python 3.9.16
    json        loads: 3.271 x1.0 | dumps: 4.765 x1.0 ✅
    fast_json   loads: 2.150 x0.7 | dumps: 6.435 x1.4 ❌
    orjson      loads: -.--- x-.- | dumps: -.--- x-.- ❌
    rapidjson   loads: 2.116 x0.6 | dumps: 1.868 x0.4 ✅
    simdjson    loads: -.--- x-.- | dumps: 4.772 x1.0 ❌
    simplejson  loads: 3.752 x1.1 | dumps: 8.030 x1.7 ❌
    ujson       loads: 2.176 x0.7 | dumps: 2.180 x0.5 ✅

Potential candidates = 'rapidjson, ujson'
```

### Python 3.8

```bash
Python 3.8.16
    json        loads: 3.359 x1.0 | dumps: 4.779 x1.0 ✅
    fast_json   loads: 2.077 x0.6 | dumps: 6.900 x1.4 ❌
    orjson      loads: -.--- x-.- | dumps: -.--- x-.- ❌
    rapidjson   loads: 2.253 x0.7 | dumps: 1.921 x0.4 ✅
    simdjson    loads: -.--- x-.- | dumps: 4.795 x1.0 ❌
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
- `python-cjson`: no more maintained
- `yajl`: no more maintained
