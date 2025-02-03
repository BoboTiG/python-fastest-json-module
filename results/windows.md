# Fastest JSON Python module on Windows

The current cross-versions winner is `usjon` :tada:

## Python 3.13

```diff
@@ Python 3.13.1 @@
! json……………… loads:  5.816  x1.0 | dumps:  8.162  x1.0
- ujson…………… loads:  7.314  x1.3 | dumps:  6.905  x0.8
- fast_json… loads:  7.338  x1.3 | dumps:  9.165  x1.1
- rapidjson… loads:  9.276  x1.6 | dumps:  7.219  x0.9
- pyjson5……… loads:  9.861  x1.7 | dumps:  8.017  x1.0
- simplejson loads:  6.645  x1.1 | dumps: 17.459  x2.1
```

## Python 3.12

```diff
@@ Python 3.12.8 @@
! json……………… loads:  5.864  x1.0 | dumps:  7.838  x1.0
- ujson…………… loads:  7.435  x1.3 | dumps:  6.804  x0.9
- fast_json… loads:  7.343  x1.3 | dumps:  8.649  x1.1
- rapidjson… loads:  8.799  x1.5 | dumps:  6.946  x0.9
- pyjson5……… loads:  8.983  x1.5 | dumps:  7.813  x1.0
- simplejson loads:  7.285  x1.2 | dumps: 17.637  x2.3
- simdjson…… loads:  -.---  x-.- | dumps:  7.676  x1.0
```

## Python 3.11

```diff
@@ Python 3.11.9 @@
! json……………… loads:  5.914  x1.0 | dumps:  8.889  x1.0
- ujson…………… loads:  7.011  x1.2 | dumps:  6.519  x0.7
- pyjson5……… loads:  8.398  x1.4 | dumps:  7.045  x0.8
- fast_json… loads:  6.922  x1.2 | dumps:  9.406  x1.1
- rapidjson… loads:  8.379  x1.4 | dumps:  7.841  x0.9
- simplejson loads:  6.207  x1.0 | dumps: 16.493  x1.9
- simdjson…… loads:  -.---  x-.- | dumps:  8.605  x1.0
```

## Python 3.10

```diff
@@ Python 3.10.11 @@
! json……………… loads:  6.089  x1.0 | dumps:  8.893  x1.0
- ujson…………… loads:  7.036  x1.2 | dumps:  6.593  x0.7
- pyjson5……… loads:  8.503  x1.4 | dumps:  7.410  x0.8
- rapidjson… loads:  8.592  x1.4 | dumps:  7.392  x0.8
- fast_json… loads:  6.970  x1.1 | dumps: 10.110  x1.1
- simplejson loads:  7.100  x1.2 | dumps: 16.524  x1.9
- simdjson…… loads:  -.---  x-.- | dumps:  9.071  x1.0
```

## Python 3.9

```diff
@@ Python 3.9.13 @@
! json……………… loads:  6.363  x1.0 | dumps:  8.697  x1.0
- ujson…………… loads:  7.037  x1.1 | dumps:  6.679  x0.8
- rapidjson… loads:  8.851  x1.4 | dumps:  6.781  x0.8
- fast_json… loads:  7.075  x1.1 | dumps: 10.093  x1.2
- pyjson5……… loads:  9.191  x1.4 | dumps:  7.294  x0.8
- simplejson loads:  7.437  x1.2 | dumps: 14.090  x1.6
- simdjson…… loads:  -.---  x-.- | dumps:  8.999  x1.0
```

## Python 3.8 (no more updated since 2023-06-13)

```diff
@@ Python 3.8.17 @@
+ ujson…………… loads:  3.258  x0.7 | dumps:  3.056  x0.5
+ pyjson5……… loads:  3.825  x0.9 | dumps:  4.515  x0.8
! json……………… loads:  4.423  x1.0 | dumps:  6.017  x1.0
- rapidjson… loads:  4.501  x1.0 | dumps:  3.234  x0.5
- fast_json… loads:  3.458  x0.8 | dumps:  8.240  x1.4
- simplejson loads:  5.554  x1.3 | dumps: 10.366  x1.7
```

## Python 3.7 (no more updated since 2023-05-18)

```diff
@@ Python 3.7.9 @@
+ ujson…………… loads:  2.585  x0.6 | dumps:  2.477  x0.5
+ rapidjson… loads:  3.676  x0.8 | dumps:  2.667  x0.5
! json……………… loads:  4.352  x1.0 | dumps:  5.361  x1.0
- pyjson5……… loads:  3.153  x0.7 | dumps:  5.373  x1.0
- fast_json… loads:  2.463  x0.6 | dumps:  7.240  x1.4
- simplejson loads:  5.321  x1.2 | dumps:  8.914  x1.7
