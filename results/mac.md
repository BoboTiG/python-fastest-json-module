# Fastest JSON Python module on macOS

The current cross-versions winner is `python-rapidjson` :tada:

## Python 3.13

```diff
@@ Python 3.13.1 @@
+ rapidjson… loads:  0.895  x0.7 | dumps:  1.213  x0.6
+ ujson…………… loads:  0.947  x0.8 | dumps:  1.226  x0.6
! json……………… loads:  1.231  x1.0 | dumps:  2.018  x1.0
- fast_json… loads:  0.958  x0.8 | dumps:  2.510  x1.2
- pyjson5……… loads:  1.511  x1.2 | dumps:  1.634  x0.8
- simplejson loads:  1.507  x1.2 | dumps:  4.008  x2.0
```

## Python 3.12

```diff
@@ Python 3.12.8 @@
+ rapidjson… loads:  0.949  x0.8 | dumps:  1.214  x0.6
+ ujson…………… loads:  0.999  x0.8 | dumps:  1.389  x0.7
! json……………… loads:  1.240  x1.0 | dumps:  2.020  x1.0
- fast_json… loads:  0.963  x0.8 | dumps:  2.538  x1.3
- pyjson5……… loads:  1.505  x1.2 | dumps:  1.875  x0.9
- simplejson loads:  1.517  x1.2 | dumps:  4.262  x2.1
```

## Python 3.11

```diff
@@ Python 3.11.9 @@
+ rapidjson… loads:  0.811  x0.7 | dumps:  1.208  x0.6
+ ujson…………… loads:  0.888  x0.8 | dumps:  1.137  x0.6
! json……………… loads:  1.144  x1.0 | dumps:  1.947  x1.0
- pyjson5……… loads:  1.361  x1.2 | dumps:  1.343  x0.7
- fast_json… loads:  0.858  x0.8 | dumps:  2.386  x1.2
- simplejson loads:  1.523  x1.3 | dumps:  3.968  x2.0
```

## Python 3.10

```diff
@@ Python 3.10.11 @@
+ ujson…………… loads:  0.870  x0.7 | dumps:  1.107  x0.5
+ rapidjson… loads:  0.815  x0.6 | dumps:  1.219  x0.6
! json……………… loads:  1.267  x1.0 | dumps:  2.042  x1.0
- pyjson5……… loads:  1.384  x1.1 | dumps:  1.411  x0.7
- fast_json… loads:  0.861  x0.7 | dumps:  2.623  x1.3
- simplejson loads:  1.511  x1.2 | dumps:  4.082  x2.0
```

## Python 3.9

```diff
@@ Python 3.9.13 @@
+ ujson…………… loads:  0.982  x0.6 | dumps:  1.148  x0.5
+ rapidjson… loads:  0.978  x0.5 | dumps:  1.232  x0.5
+ pyjson5……… loads:  1.652  x0.9 | dumps:  1.778  x0.7
! json……………… loads:  1.781  x1.0 | dumps:  2.529  x1.0
- fast_json… loads:  0.998  x0.6 | dumps:  3.276  x1.3
- simplejson loads:  2.054  x1.2 | dumps:  4.077  x1.6
```

## Python 3.8 (no more updated since 2023-06-13)

```diff
@@ Python 3.8.17 @@
+ ujson…………… loads:  2.714  x0.6 | dumps:  2.841  x0.5
+ rapidjson… loads:  2.549  x0.5 | dumps:  3.114  x0.5
+ pyjson5……… loads:  2.996  x0.6 | dumps:  4.219  x0.7
! json……………… loads:  4.777  x1.0 | dumps:  5.705  x1.0
- fast_json… loads:  2.777  x0.6 | dumps:  8.685  x1.5
- simplejson loads:  5.266  x1.1 | dumps: 10.581  x1.9
```

## Python 3.7 (no more updated since 2023-05-18)

```diff
@@ Python 3.7.16 @@
+ ujson…………… loads:  2.534  x0.5 | dumps:  2.579  x0.4
+ rapidjson… loads:  2.337  x0.5 | dumps:  2.824  x0.5
+ pyjson5……… loads:  2.806  x0.5 | dumps:  4.626  x0.8
! json……………… loads:  5.180  x1.0 | dumps:  6.031  x1.0
- fast_json… loads:  2.552  x0.5 | dumps:  8.481  x1.4
- simplejson loads:  5.605  x1.1 | dumps: 10.403  x1.7
```
