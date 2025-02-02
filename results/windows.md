# Fastest JSON Python module on Windows

The current cross-versions winner is `usjon` :tada:

## Python 3.13

```diff
@@ Python 3.13.1 @@
+ ujson…………… loads:  2.098  x0.9 | dumps:  2.152  x0.7
+ pyjson5……… loads:  2.164  x1.0 | dumps:  2.948  x0.9
! json……………… loads:  2.239  x1.0 | dumps:  3.148  x1.0
- rapidjson… loads:  2.923  x1.3 | dumps:  2.113  x0.7
- fast_json… loads:  2.072  x0.9 | dumps:  4.113  x1.3
- simplejson loads:  2.516  x1.1 | dumps:  7.170  x2.3
```

## Python 3.12

```diff
@@ Python 3.12.8 @@
+ ujson…………… loads:  2.098  x0.9 | dumps:  2.115  x0.7
+ pyjson5……… loads:  2.166  x0.9 | dumps:  2.960  x1.0
! json……………… loads:  2.297  x1.0 | dumps:  3.064  x1.0
- rapidjson… loads:  2.911  x1.3 | dumps:  1.866  x0.6
- fast_json… loads:  2.101  x0.9 | dumps:  3.936  x1.3
- simplejson loads:  2.623  x1.1 | dumps:  7.052  x2.3
```

## Python 3.11

```diff
@@ Python 3.11.9 @@
+ ujson…………… loads:  1.912  x0.8 | dumps:  1.993  x0.6
+ pyjson5……… loads:  1.976  x0.9 | dumps:  2.636  x0.8
! json……………… loads:  2.257  x1.0 | dumps:  3.368  x1.0
- rapidjson… loads:  2.746  x1.2 | dumps:  1.929  x0.6
- fast_json… loads:  1.885  x0.8 | dumps:  3.872  x1.1
- simplejson loads:  2.467  x1.1 | dumps:  6.707  x2.0
```

## Python 3.10

```diff
@@ Python 3.10.11 @@
+ ujson…………… loads:  1.934  x0.8 | dumps:  1.994  x0.6
+ pyjson5……… loads:  2.207  x0.9 | dumps:  2.817  x0.8
! json……………… loads:  2.385  x1.0 | dumps:  3.515  x1.0
- rapidjson… loads:  2.793  x1.2 | dumps:  2.286  x0.7
- fast_json… loads:  2.078  x0.9 | dumps:  4.462  x1.3
- simplejson loads:  2.785  x1.2 | dumps:  7.382  x2.1
```

## Python 3.9

```diff
@@ Python 3.9.13 @@
+ ujson…………… loads:  1.929  x0.8 | dumps:  1.935  x0.6
+ pyjson5……… loads:  2.182  x0.9 | dumps:  2.808  x0.9
! json……………… loads:  2.442  x1.0 | dumps:  3.299  x1.0
- rapidjson… loads:  2.782  x1.1 | dumps:  1.889  x0.6
- fast_json… loads:  1.939  x0.8 | dumps:  4.503  x1.4
- simplejson loads:  3.078  x1.3 | dumps:  5.944  x1.8
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
