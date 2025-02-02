# Fastest JSON Python module on GNU/Linux

The current cross-versions winner is `python-rapidjson` :tada:

## Python 3.13

```diff
@@ Python 3.13.1 @@
+ rapidjson… loads:  2.017  x0.9 | dumps:  1.746  x0.5
! json……………… loads:  2.259  x1.0 | dumps:  3.398  x1.0
- ujson…………… loads:  2.681  x1.2 | dumps:  2.889  x0.9
- pyjson5……… loads:  2.955  x1.3 | dumps:  4.343  x1.3
- fast_json… loads:  2.622  x1.2 | dumps:  5.664  x1.7
- simplejson loads:  3.248  x1.4 | dumps: 10.474  x3.1
```

## Python 3.12

```diff
@@ Python 3.12.8 @@
+ rapidjson… loads:  1.986  x0.8 | dumps:  1.776  x0.5
! json……………… loads:  2.374  x1.0 | dumps:  3.422  x1.0
- ujson…………… loads:  2.710  x1.1 | dumps:  2.902  x0.8
- pyjson5……… loads:  2.991  x1.3 | dumps:  4.567  x1.3
- fast_json… loads:  2.664  x1.1 | dumps:  5.692  x1.7
- simplejson loads:  3.531  x1.5 | dumps: 10.436  x3.0
```

## Python 3.11

```diff
@@ Python 3.11.11 @@
+ rapidjson… loads:  1.444  x0.7 | dumps:  1.276  x0.4
+ ujson…………… loads:  1.870  x0.9 | dumps:  1.914  x0.6
+ pyjson5……… loads:  1.702  x0.8 | dumps:  2.367  x0.7
! json……………… loads:  2.071  x1.0 | dumps:  3.162  x1.0
- fast_json… loads:  1.825  x0.9 | dumps:  4.104  x1.3
- simplejson loads:  2.280  x1.1 | dumps:  7.128  x2.3
```

## Python 3.10

```diff
@@ Python 3.10.16 @@
+ rapidjson… loads:  1.541  x0.6 | dumps:  1.356  x0.4
+ ujson…………… loads:  1.920  x0.8 | dumps:  2.005  x0.6
+ pyjson5……… loads:  1.860  x0.8 | dumps:  2.688  x0.8
! json……………… loads:  2.441  x1.0 | dumps:  3.454  x1.0
- fast_json… loads:  1.939  x0.8 | dumps:  4.649  x1.3
- simplejson loads:  2.674  x1.1 | dumps:  7.557  x2.2
```

## Python 3.9

```diff
@@ Python 3.9.21 @@
+ rapidjson… loads:  1.498  x0.6 | dumps:  1.417  x0.4
+ ujson…………… loads:  1.949  x0.8 | dumps:  2.003  x0.6
+ pyjson5……… loads:  2.002  x0.8 | dumps:  2.781  x0.8
! json……………… loads:  2.597  x1.0 | dumps:  3.623  x1.0
- fast_json… loads:  1.954  x0.8 | dumps:  4.975  x1.4
- simplejson loads:  2.911  x1.1 | dumps:  6.506  x1.8
```

## Python 3.8 (no more updated since 2023-06-13)

```diff
@@ Python 3.8.17 @@
+ rapidjson… loads:  2.497  x0.6 | dumps:  2.192  x0.4
+ ujson…………… loads:  2.555  x0.6 | dumps:  2.947  x0.5
+ pyjson5……… loads:  3.122  x0.8 | dumps:  4.186  x0.8
! json……………… loads:  4.006  x1.0 | dumps:  5.580  x1.0
- fast_json… loads:  2.591  x0.6 | dumps:  7.842  x1.4
- simplejson loads:  4.406  x1.1 | dumps:  9.891  x1.8
```

## Python 3.7 (no more updated since 2023-05-18)

```diff
@@ Python 3.7.16 @@
+ rapidjson… loads:  2.361  x0.6 | dumps:  2.081  x0.4
+ ujson…………… loads:  2.594  x0.6 | dumps:  2.719  x0.5
+ pyjson5……… loads:  3.034  x0.7 | dumps:  4.766  x0.9
! json……………… loads:  4.099  x1.0 | dumps:  5.445  x1.0
- fast_json… loads:  2.594  x0.6 | dumps:  7.472  x1.4
- simplejson loads:  4.614  x1.1 | dumps:  9.788  x1.8
```
