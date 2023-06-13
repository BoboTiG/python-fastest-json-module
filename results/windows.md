# Fatest JSON Python module on Windows

The current cross-versions winner is `usjon` :tada:

## Python 3.12

```diff
@@ Python 3.12.0 @@
+ ujson…………… loads:  2.576  x0.8 | dumps:  2.605  x0.6
! json……………… loads:  3.129  x1.0 | dumps:  4.541  x1.0
- pyjson5……… loads:  -.---  x-.- | dumps:  -.---  x-.-
- rapidjson… loads:  3.585  x1.1 | dumps:  3.161  x0.7
- fast_json… loads:  2.623  x0.8 | dumps:  5.651  x1.2
- simplejson loads: 29.643  x9.5 | dumps: 33.550  x7.4
```

## Python 3.11

```diff
@@ Python 3.11.4 @@
+ ujson…………… loads:  2.982  x0.8 | dumps:  2.778  x0.5
! json……………… loads:  3.904  x1.0 | dumps:  5.679  x1.0
- rapidjson… loads:  4.394  x1.1 | dumps:  3.190  x0.6
- pyjson5……… loads:  4.145  x1.1 | dumps:  4.263  x0.8
- fast_json… loads:  2.890  x0.7 | dumps:  6.926  x1.2
- simplejson loads:  4.423  x1.1 | dumps: 11.058  x1.9
```

## Python 3.10

```diff
@@ Python 3.10.11 @@
+ ujson…………… loads:  2.792  x0.7 | dumps:  2.738  x0.5
+ pyjson5……… loads:  3.838  x0.9 | dumps:  4.663  x0.8
+ rapidjson… loads:  3.960  x1.0 | dumps:  4.612  x0.8
! json……………… loads:  4.108  x1.0 | dumps:  5.886  x1.0
- fast_json… loads:  2.762  x0.7 | dumps:  7.541  x1.3
- simplejson loads:  4.818  x1.2 | dumps: 11.351  x1.9
```

## Python 3.9

```diff
@@ Python 3.9.13 @@
+ ujson…………… loads:  2.345  x0.7 | dumps:  2.279  x0.5
+ rapidjson… loads:  3.262  x1.0 | dumps:  2.600  x0.6
+ pyjson5……… loads:  3.174  x1.0 | dumps:  3.755  x0.8
! json……………… loads:  3.337  x1.0 | dumps:  4.654  x1.0
- fast_json… loads:  2.366  x0.7 | dumps:  6.057  x1.3
- simplejson loads:  4.351  x1.3 | dumps:  7.848  x1.7
```

## Python 3.8

```diff
@@ Python 3.8.10 @@
+ ujson…………… loads:  3.258  x0.7 | dumps:  3.056  x0.5
+ pyjson5……… loads:  3.825  x0.9 | dumps:  4.515  x0.8
! json……………… loads:  4.423  x1.0 | dumps:  6.017  x1.0
- rapidjson… loads:  4.501  x1.0 | dumps:  3.234  x0.5
- fast_json… loads:  3.458  x0.8 | dumps:  8.240  x1.4
- simplejson loads:  5.554  x1.3 | dumps: 10.366  x1.7
```
