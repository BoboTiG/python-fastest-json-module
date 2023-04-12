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

```

### Python 3.11

```bash
Run from 2023-04-12 21h05

Python 3.11.3
    fast-json==0.3.2
    orjson==3.8.10
    pysimdjson==5.0.2
    python-rapidjson==1.10
    simplejson==3.19.1
    ujson==5.7.0

json        loads: 2.711 x1.0 | dumps: 4.378 x1.0 ✅
fast_json   loads: 2.131 x0.8 | dumps: 5.542 x1.3 ❌
orjson      loads: -.--- x-.- | dumps: -.--- x-.- ❌
rapidjson   loads: 1.913 x0.7 | dumps: 1.657 x0.4 ✅
simdjson    loads: -.--- x-.- | dumps: 4.399 x1.0 ❌
simplejson  loads: 3.042 x1.1 | dumps: 8.558 x2.0 ❌
ujson       loads: 2.125 x0.8 | dumps: 2.125 x0.5 ✅

Potential candidates = 'rapidjson, ujson'
```

### Python 3.10

```bash
Run from 2023-04-12 21h05

Python 3.10.10
    fast-json==0.3.2
    orjson==3.8.10
    pysimdjson==5.0.2
    python-rapidjson==1.10
    simplejson==3.19.1
    ujson==5.7.0

json        loads: 3.290 x1.0 | dumps: 4.846 x1.0 ✅
fast_json   loads: 2.169 x0.7 | dumps: 6.400 x1.3 ❌
orjson      loads: -.--- x-.- | dumps: -.--- x-.- ❌
rapidjson   loads: 1.975 x0.6 | dumps: 1.842 x0.4 ✅
simdjson    loads: -.--- x-.- | dumps: 4.751 x1.0 ❌
simplejson  loads: 3.722 x1.1 | dumps: 9.494 x2.0 ❌
ujson       loads: 2.200 x0.7 | dumps: 2.165 x0.4 ✅

Potential candidates = 'rapidjson, ujson'
```

### Python 3.9

```bash
Run from 2023-04-12 21h05

Python 3.9.16
    fast-json==0.3.2
    orjson==3.8.10
    pysimdjson==5.0.2
    python-rapidjson==1.10
    simplejson==3.19.1
    ujson==5.7.0

json        loads: 3.833 x1.0 | dumps: 5.599 x1.0 ✅
fast_json   loads: 2.537 x0.7 | dumps: 7.397 x1.3 ❌
orjson      loads: -.--- x-.- | dumps: -.--- x-.- ❌
rapidjson   loads: 2.473 x0.6 | dumps: 2.203 x0.4 ✅
simdjson    loads: -.--- x-.- | dumps: 5.629 x1.0 ❌
simplejson  loads: 4.324 x1.1 | dumps: 9.345 x1.7 ❌
ujson       loads: 2.555 x0.7 | dumps: 2.580 x0.5 ✅

Potential candidates = 'rapidjson, ujson'
```

### Python 3.8

```bash
Run from 2023-04-12 21h05

Python 3.8.16
    fast-json==0.3.2
    orjson==3.8.10
    pysimdjson==5.0.2
    python-rapidjson==1.10
    simplejson==3.19.1
    ujson==5.7.0

json        loads: 4.219 x1.0 | dumps: 5.792 x1.0 ✅
fast_json   loads: 2.578 x0.6 | dumps: 8.493 x1.5 ❌
orjson      loads: -.--- x-.- | dumps: -.--- x-.- ❌
rapidjson   loads: 2.559 x0.6 | dumps: 2.222 x0.4 ✅
simdjson    loads: -.--- x-.- | dumps: 5.709 x1.0 ❌
simplejson  loads: 4.541 x1.1 | dumps: 13.574 x2.3 ❌
ujson       loads: 2.881 x0.7 | dumps: 2.842 x0.5 ✅

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
