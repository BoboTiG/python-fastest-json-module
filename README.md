# Fatest JSON Python module

Run Python JSON benchmarks to find the fastest module that can be used as a drop-in replacement of the `json` standard one.

Run the benchmark:

```bash
./bench-json.sh
```

## Results

Current cross-versions winner: `python-rapidjson` :tada:

### Python 3.12

```bash
Python 3.12.0a7
    fast-json==0.3.2
    orjson==3.8.10
    python-rapidjson==1.10
    simplejson==3.19.1
    ujson==5.7.0

json        loads: 3.125 x1.0 | dumps: 4.982 x1.0 ✅
fast_json   loads: 2.568 x0.8 | dumps: 6.390 x1.3 ❌
orjson      loads: -.--- x-.- | dumps: -.--- x-.- ❌
rapidjson   loads: 2.338 x0.7 | dumps: 2.510 x0.5 ✅
simplejson  loads: 29.099 x9.3 | dumps: 33.922 x6.8 ❌
ujson       loads: 2.557 x0.8 | dumps: 3.077 x0.6 ✅

Potential candidates = 'rapidjson, ujson'
```

### Python 3.11

```bash
Run from 2023-04-12 21h36

Python 3.11.3
    fast-json==0.3.2
    orjson==3.8.10
    pysimdjson==5.0.2
    python-rapidjson==1.10
    simplejson==3.19.1
    ujson==5.7.0

json        loads: 2.880 x1.0 | dumps: 4.364 x1.0 ✅
fast_json   loads: 2.033 x0.7 | dumps: 5.665 x1.3 ❌
orjson      loads: -.--- x-.- | dumps: -.--- x-.- ❌
rapidjson   loads: 2.058 x0.7 | dumps: 1.771 x0.4 ✅
simdjson    loads: -.--- x-.- | dumps: 4.383 x1.0 ❌
simplejson  loads: 3.205 x1.1 | dumps: 9.071 x2.1 ❌
ujson       loads: 2.070 x0.7 | dumps: 2.167 x0.5 ✅

Potential candidates = 'rapidjson, ujson'
```

### Python 3.10

```bash
Run from 2023-04-12 21h36

Python 3.10.10
    fast-json==0.3.2
    orjson==3.8.10
    pysimdjson==5.0.2
    python-rapidjson==1.10
    simplejson==3.19.1
    ujson==5.7.0

json        loads: 4.231 x1.0 | dumps: 5.889 x1.0 ✅
fast_json   loads: 2.558 x0.6 | dumps: 8.021 x1.4 ❌
orjson      loads: -.--- x-.- | dumps: -.--- x-.- ❌
rapidjson   loads: 2.590 x0.6 | dumps: 2.282 x0.4 ✅
simdjson    loads: -.--- x-.- | dumps: 6.319 x1.1 ❌
simplejson  loads: 4.482 x1.1 | dumps: 12.234 x2.1 ❌
ujson       loads: 2.679 x0.6 | dumps: 2.966 x0.5 ✅

Potential candidates = 'rapidjson, ujson'
```

### Python 3.9

```bash
Run from 2023-04-12 21h36

Python 3.9.16
    fast-json==0.3.2
    orjson==3.8.10
    pysimdjson==5.0.2
    python-rapidjson==1.10
    simplejson==3.19.1
    ujson==5.7.0

json        loads: 3.987 x1.0 | dumps: 5.645 x1.0 ✅
fast_json   loads: 2.475 x0.6 | dumps: 7.551 x1.3 ❌
orjson      loads: -.--- x-.- | dumps: -.--- x-.- ❌
rapidjson   loads: 2.378 x0.6 | dumps: 2.084 x0.4 ✅
simdjson    loads: -.--- x-.- | dumps: 5.492 x1.0 ❌
simplejson  loads: 4.490 x1.1 | dumps: 10.267 x1.8 ❌
ujson       loads: 2.638 x0.7 | dumps: 2.714 x0.5 ✅

Potential candidates = 'rapidjson, ujson'
```

### Python 3.8

```bash
Run from 2023-04-12 21h36

Python 3.8.16
    fast-json==0.3.2
    orjson==3.8.10
    pysimdjson==5.0.2
    python-rapidjson==1.10
    simplejson==3.19.1
    ujson==5.7.0

json        loads: 3.382 x1.0 | dumps: 4.739 x1.0 ✅
fast_json   loads: 2.054 x0.6 | dumps: 6.785 x1.4 ❌
orjson      loads: -.--- x-.- | dumps: -.--- x-.- ❌
rapidjson   loads: 2.255 x0.7 | dumps: 1.904 x0.4 ✅
simdjson    loads: -.--- x-.- | dumps: 4.888 x1.0 ❌
simplejson  loads: 3.905 x1.2 | dumps: 8.595 x1.8 ❌
ujson       loads: 2.349 x0.7 | dumps: 2.578 x0.5 ✅

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
