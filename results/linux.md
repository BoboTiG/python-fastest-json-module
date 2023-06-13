# Fatest JSON Python module on GNU/Linux

The current cross-versions winner is `python-rapidjson` :tada:

## Python 3.12

```diff
@@ Python 3.12.0 @@
+ rapidjson… loads:  2.005  x0.7 | dumps:  2.142  x0.5
+ ujson…………… loads:  2.118  x0.8 | dumps:  2.508  x0.6
! json……………… loads:  2.694  x1.0 | dumps:  4.261  x1.0
- fast_json… loads:  2.092  x0.8 | dumps:  5.578  x1.3
- simplejson loads: 25.065  x9.3 | dumps: 27.842  x6.5
- pyjson5……… loads:  -.---  x-.- | dumps:  -.---  x-.-
```

## Python 3.11

```diff
@@ Python 3.11.3 @@
+ rapidjson… loads:  2.388  x0.7 | dumps:  2.054  x0.4
+ ujson…………… loads:  2.630  x0.8 | dumps:  2.558  x0.5
+ pyjson5……… loads:  3.243  x1.0 | dumps:  3.864  x0.7
! json……………… loads:  3.353  x1.0 | dumps:  5.342  x1.0
- fast_json… loads:  2.614  x0.8 | dumps:  6.901  x1.3
- simplejson loads:  3.705  x1.1 | dumps: 10.336  x1.9
```

## Python 3.10

```diff
@@ Python 3.10.11 @@
+ rapidjson… loads:  2.055  x0.6 | dumps:  1.847  x0.4
+ ujson…………… loads:  2.220  x0.7 | dumps:  2.263  x0.5
+ pyjson5……… loads:  2.819  x0.8 | dumps:  3.573  x0.7
! json……………… loads:  3.412  x1.0 | dumps:  4.830  x1.0
- fast_json… loads:  2.189  x0.6 | dumps:  6.396  x1.3
- simplejson loads:  3.648  x1.1 | dumps:  9.370  x1.9
```

## Python 3.9

```diff
@@ Python 3.9.16 @@
+ rapidjson… loads:  2.022  x0.6 | dumps:  1.805  x0.4
+ ujson…………… loads:  2.160  x0.7 | dumps:  2.196  x0.5
+ pyjson5……… loads:  2.735  x0.8 | dumps:  3.601  x0.8
! json……………… loads:  3.235  x1.0 | dumps:  4.735  x1.0
- fast_json… loads:  2.188  x0.7 | dumps:  6.429  x1.4
- simplejson loads:  3.784  x1.2 | dumps:  8.097  x1.7
```

## Python 3.8

```diff
 @@ Python 3.8.16 @@
+ rapidjson… loads:  2.273  x0.6 | dumps:  1.878  x0.4
+ ujson…………… loads:  2.111  x0.6 | dumps:  2.697  x0.6
+ pyjson5……… loads:  2.541  x0.7 | dumps:  4.021  x0.9
! json……………… loads:  3.546  x1.0 | dumps:  4.697  x1.0
- fast_json… loads:  2.118  x0.6 | dumps:  6.781  x1.4
- simplejson loads:  3.909  x1.1 | dumps:  8.601  x1.8
```
