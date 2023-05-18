# Fatest JSON Python module on macOS

The current cross-versions winner is `python-rapidjson` :tada:

## Python 3.12

```diff
@@ Python 3.12.0 @@
+ rapidjson… loads:  1.865  x0.5 | dumps:  2.449  x0.5
+ ujson…………… loads:  2.494  x0.7 | dumps:  2.692  x0.6
! json……………… loads:  3.407  x1.0 | dumps:  4.856  x1.0
- fast_json… loads:  2.509  x0.7 | dumps:  7.060  x1.5
- simplejson loads: 33.632  x9.9 | dumps: 48.556 x10.0
- pyjson5……… loads:  -.---  x-.- | dumps:  -.---  x-.-
```

## Python 3.11

```diff
@@ Python 3.11.3 @@
+ rapidjson… loads:  2.077  x0.6 | dumps:  2.525  x0.5
+ ujson…………… loads:  2.457  x0.7 | dumps:  2.444  x0.5
+ pyjson5……… loads:  2.752  x0.8 | dumps:  3.526  x0.7
! json……………… loads:  3.344  x1.0 | dumps:  4.977  x1.0
- fast_json… loads:  2.582  x0.8 | dumps:  6.656  x1.3
- simplejson loads:  4.050  x1.2 | dumps: 10.392  x2.1
```

## Python 3.10

```diff
@@ Python 3.10.11 @@
+ rapidjson… loads:  2.208  x0.5 | dumps:  3.390  x0.5
+ ujson…………… loads:  3.331  x0.7 | dumps:  3.113  x0.5
+ pyjson5……… loads:  3.273  x0.7 | dumps:  3.647  x0.6
! json……………… loads:  4.845  x1.0 | dumps:  6.363  x1.0
- fast_json… loads:  3.318  x0.7 | dumps:  8.890  x1.4
- simplejson loads:  5.944  x1.2 | dumps: 14.921  x2.3
```

## Python 3.9

```diff
@@ Python 3.9.16 @@
+ rapidjson… loads:  2.546  x0.5 | dumps:  2.895  x0.4
+ ujson…………… loads:  2.699  x0.6 | dumps:  2.979  x0.5
+ pyjson5……… loads:  3.010  x0.6 | dumps:  4.374  x0.7
! json……………… loads:  4.791  x1.0 | dumps:  6.583  x1.0
- fast_json… loads:  2.848  x0.6 | dumps:  9.831  x1.5
- simplejson loads:  5.307  x1.1 | dumps: 12.267  x1.9
```

## Python 3.8

```diff
@@ Python 3.8.16 @@
+ rapidjson… loads:  2.652  x0.3 | dumps:  2.794  x0.3
+ pyjson5……… loads:  2.846  x0.4 | dumps:  3.836  x0.4
+ ujson…………… loads:  3.873  x0.5 | dumps:  4.207  x0.5
! json……………… loads:  7.789  x1.0 | dumps:  8.566  x1.0
- fast_json… loads:  5.839  x0.7 | dumps: 10.484  x1.2
- simplejson loads:  5.904  x0.8 | dumps: 13.274  x1.5
```

## Python 3.7

```diff
@@ Python 3.7.16 @@
+ ujson…………… loads:  2.534  x0.5 | dumps:  2.579  x0.4
+ rapidjson… loads:  2.337  x0.5 | dumps:  2.824  x0.5
+ pyjson5……… loads:  2.806  x0.5 | dumps:  4.626  x0.8
! json……………… loads:  5.180  x1.0 | dumps:  6.031  x1.0
- fast_json… loads:  2.552  x0.5 | dumps:  8.481  x1.4
- simplejson loads:  5.605  x1.1 | dumps: 10.403  x1.7
```
