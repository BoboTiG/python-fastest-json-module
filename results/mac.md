# Fastest JSON Python module on macOS

The current cross-versions winner is `python-rapidjson` :tada:

## Python 3.13

```diff
@@ Python 3.13.1 @@
+ ujson…………… loads:  3.018  x0.8 | dumps:  3.207  x0.5
! json……………… loads:  3.870  x1.0 | dumps:  6.166  x1.0
- rapidjson… loads:  4.133  x1.1 | dumps:  4.619  x0.7
- fast_json… loads:  3.027  x0.8 | dumps:  6.548  x1.1
- pyjson5……… loads:  7.567  x2.0 | dumps:  4.352  x0.7
- simplejson loads:  4.440  x1.1 | dumps: 10.123  x1.6
```

## Python 3.12

```diff
@@ Python 3.12.8 @@
! json……………… loads:  3.849  x1.0 | dumps:  6.565  x1.0
- ujson…………… loads:  4.085  x1.1 | dumps:  4.512  x0.7
- fast_json… loads:  3.599  x0.9 | dumps:  7.850  x1.2
- rapidjson… loads:  5.422  x1.4 | dumps:  5.299  x0.8
- pyjson5……… loads:  9.465  x2.5 | dumps:  5.173  x0.8
- simplejson loads:  5.949  x1.5 | dumps: 13.206  x2.0
- simdjson…… loads:  -.---  x-.- | dumps:  6.887  x1.0
```

## Python 3.11

```diff
@@ Python 3.11.9 @@
+ ujson…………… loads:  2.877  x0.8 | dumps:  2.963  x0.5
! json……………… loads:  3.442  x1.0 | dumps:  6.082  x1.0
- fast_json… loads:  2.782  x0.8 | dumps:  6.962  x1.1
- rapidjson… loads:  4.425  x1.3 | dumps:  4.895  x0.8
- simplejson loads:  4.597  x1.3 | dumps:  9.964  x1.6
- pyjson5……… loads:  8.926  x2.6 | dumps:  4.434  x0.7
- simdjson…… loads:  -.---  x-.- | dumps:  6.413  x1.1
```

## Python 3.10

```diff
@@ Python 3.10.11 @@
+ ujson…………… loads:  3.064  x0.7 | dumps:  3.018  x0.4
+ rapidjson… loads:  3.605  x0.9 | dumps:  4.642  x0.7
+ fast_json… loads:  3.067  x0.7 | dumps:  6.654  x0.9
! json……………… loads:  4.140  x1.0 | dumps:  7.054  x1.0
- pyjson5……… loads:  7.084  x1.7 | dumps:  3.968  x0.6
- simplejson loads:  4.193  x1.0 | dumps: 10.706  x1.5
- simdjson…… loads:  -.---  x-.- | dumps:  6.197  x0.9
```

## Python 3.9

```diff
@@ Python 3.9.13 @@
+ ujson…………… loads:  3.265  x0.7 | dumps:  3.181  x0.4
+ rapidjson… loads:  4.327  x0.9 | dumps:  5.156  x0.7
! json……………… loads:  4.779  x1.0 | dumps:  7.297  x1.0
- fast_json… loads:  3.052  x0.6 | dumps:  7.901  x1.1
- pyjson5……… loads:  7.350  x1.5 | dumps:  4.205  x0.6
- simplejson loads:  7.081  x1.5 | dumps: 10.794  x1.5
- simdjson…… loads:  -.---  x-.- | dumps:  9.413  x1.3
```
