# Fatest JSON Python module on Windows

The current cross-versions winner is `usjon` :tada:

## Python 3.12

```diff
@@ Python 3.12.0 @@
+ ujson…………… loads:  2.426  x0.8 | dumps:  2.415  x0.6
! json……………… loads:  2.906  x1.0 | dumps:  4.136  x1.0
- rapidjson… loads:  3.233  x1.1 | dumps:  3.045  x0.7
- fast_json… loads:  2.436  x0.8 | dumps:  5.195  x1.3
- simplejson loads: 25.721  x8.9 | dumps: 30.215  x7.3
- pyjson5……… loads:  -.---  x-.- | dumps:  -.---  x-.-
```

## Python 3.11

```diff
@@ Python 3.11.3 @@
@@ Python 3.11.3 @@
+ ujson…………… loads:  2.931  x0.8 | dumps:  2.833  x0.5
! json……………… loads:  3.517  x1.0 | dumps:  5.417  x1.0
- rapidjson… loads:  3.891  x1.1 | dumps:  2.998  x0.6
- pyjson5……… loads:  3.871  x1.1 | dumps:  4.032  x0.7
- fast_json… loads:  2.867  x0.8 | dumps:  6.672  x1.2
- simplejson loads:  4.152  x1.2 | dumps: 10.732  x2.0
```

## Python 3.10

```diff
@@ Python 3.10.11 @@
+ ujson…………… loads:  2.436  x0.7 | dumps:  2.298  x0.5
+ pyjson5……… loads:  3.159  x1.0 | dumps:  3.877  x0.8
+ rapidjson… loads:  3.242  x1.0 | dumps:  3.921  x0.8
! json……………… loads:  3.268  x1.0 | dumps:  4.849  x1.0
- fast_json… loads:  2.424  x0.7 | dumps:  6.360  x1.3
- simplejson loads:  3.940  x1.2 | dumps:  9.267  x1.9
```

## Python 3.9

```diff
@@ Python 3.9.13 @@
+ ujson…………… loads:  2.916  x0.6 | dumps:  2.967  x0.6
+ rapidjson… loads:  3.627  x0.8 | dumps:  3.298  x0.6
+ pyjson5……… loads:  3.170  x0.7 | dumps:  3.850  x0.7
! json……………… loads:  4.776  x1.0 | dumps:  5.291  x1.0
- fast_json… loads:  2.205  x0.5 | dumps:  6.304  x1.2
- simplejson loads:  5.438  x1.1 | dumps:  9.650  x1.8
```

## Python 3.8

```diff
@@ Python 3.8.10 @@
+ ujson…………… loads:  2.441  x0.8 | dumps:  2.575  x0.6
+ pyjson5……… loads:  2.952  x1.0 | dumps:  3.683  x0.9
! json……………… loads:  3.004  x1.0 | dumps:  4.154  x1.0
- rapidjson… loads:  3.451  x1.1 | dumps:  2.452  x0.6
- fast_json… loads:  2.361  x0.8 | dumps:  5.739  x1.4
- simplejson loads:  3.706  x1.2 | dumps:  7.534  x1.8
```

## Python 3.7

```diff
@@ Python 3.7.9 @@
+ ujson…………… loads:  2.585  x0.6 | dumps:  2.477  x0.5
+ rapidjson… loads:  3.676  x0.8 | dumps:  2.667  x0.5
! json……………… loads:  4.352  x1.0 | dumps:  5.361  x1.0
- pyjson5……… loads:  3.153  x0.7 | dumps:  5.373  x1.0
- fast_json… loads:  2.463  x0.6 | dumps:  7.240  x1.4
- simplejson loads:  5.321  x1.2 | dumps:  8.914  x1.7
```
