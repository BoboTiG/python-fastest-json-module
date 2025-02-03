# Fastest JSON Python module on GNU/Linux

The current cross-versions winner is `python-rapidjson` :tada:

## Python 3.13

```diff
@@ Python 3.13.1 @@
! json……………… loads:  5.857  x1.0 | dumps:  7.574  x1.0
- rapidjson… loads:  6.217  x1.1 | dumps:  4.582  x0.6
- ujson…………… loads:  7.360  x1.3 | dumps:  6.725  x0.9
- pyjson5……… loads:  8.019  x1.4 | dumps:  7.556  x1.0
- fast_json… loads:  7.343  x1.3 | dumps:  8.672  x1.1
- simplejson loads:  6.333  x1.1 | dumps: 19.505  x2.6
```

## Python 3.12

```diff
@@ Python 3.12.8 @@
+ rapidjson… loads:  5.830  x1.0 | dumps:  4.567  x0.6
! json……………… loads:  5.952  x1.0 | dumps:  8.047  x1.0
- ujson…………… loads:  7.358  x1.2 | dumps:  6.754  x0.8
- pyjson5……… loads:  7.992  x1.3 | dumps:  7.439  x0.9
- fast_json… loads:  7.354  x1.2 | dumps:  9.304  x1.2
- simplejson loads:  6.603  x1.1 | dumps: 19.783  x2.5
- simdjson…… loads:  -.---  x-.- | dumps:  8.149  x1.0
```

## Python 3.11

```diff
@@ Python 3.11.11 @@
! json……………… loads:  5.255  x1.0 | dumps:  8.078  x1.0
- rapidjson… loads:  5.503  x1.0 | dumps:  4.330  x0.5
- pyjson5……… loads:  6.930  x1.3 | dumps:  5.590  x0.7
- ujson…………… loads:  6.805  x1.3 | dumps:  6.106  x0.8
- fast_json… loads:  6.734  x1.3 | dumps:  8.950  x1.1
- simplejson loads:  5.875  x1.1 | dumps: 17.296  x2.1
- simdjson…… loads:  -.---  x-.- | dumps:  8.048  x1.0
```

## Python 3.10

```diff
@@ Python 3.10.16 @@
+ rapidjson… loads:  5.531  x0.9 | dumps:  4.353  x0.5
! json……………… loads:  5.957  x1.0 | dumps:  8.207  x1.0
- ujson…………… loads:  6.839  x1.1 | dumps:  6.250  x0.8
- pyjson5……… loads:  7.264  x1.2 | dumps:  6.375  x0.8
- fast_json… loads:  6.843  x1.1 | dumps:  9.611  x1.2
- simplejson loads:  6.402  x1.1 | dumps: 16.678  x2.0
- simdjson…… loads:  -.---  x-.- | dumps:  8.392  x1.0
```

## Python 3.9

```diff
@@ Python 3.9.21 @@
+ rapidjson… loads:  5.618  x1.0 | dumps:  4.441  x0.5
! json……………… loads:  5.893  x1.0 | dumps:  8.286  x1.0
- ujson…………… loads:  6.414  x1.1 | dumps:  6.116  x0.7
- pyjson5……… loads:  7.106  x1.2 | dumps:  6.735  x0.8
- fast_json… loads:  6.418  x1.1 | dumps:  9.670  x1.2
- simplejson loads:  6.498  x1.1 | dumps: 14.442  x1.7
- simdjson…… loads:  -.---  x-.- | dumps:  8.413  x1.0
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
