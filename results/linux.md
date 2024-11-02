# Fastest JSON Python module on GNU/Linux

The current cross-versions winner is `python-rapidjson` :tada:

## Python 3.13

```diff
@@ Python 3.13.0 @@
+ rapidjson… loads:  2.021  x0.9 | dumps:  1.727  x0.5
! json……………… loads:  2.274  x1.0 | dumps:  3.481  x1.0
- ujson…………… loads:  2.671  x1.2 | dumps:  2.901  x0.8
- pyjson5……… loads:  3.034  x1.3 | dumps:  4.460  x1.3
- fast_json… loads:  2.639  x1.2 | dumps:  5.821  x1.7
- simplejson loads:  3.274  x1.4 | dumps: 10.873  x3.1
```

## Python 3.12

```diff
@@ Python 3.12.7 @@
+ rapidjson… loads:  2.040  x0.9 | dumps:  1.745  x0.5
! json……………… loads:  2.304  x1.0 | dumps:  3.376  x1.0
- ujson…………… loads:  2.674  x1.2 | dumps:  2.915  x0.9
- pyjson5……… loads:  2.929  x1.3 | dumps:  4.438  x1.3
- fast_json… loads:  2.619  x1.1 | dumps:  5.710  x1.7
- simplejson loads:  3.429  x1.5 | dumps: 10.443  x3.1
```

## Python 3.11

```diff
@@ Python 3.11.10 @@
+ rapidjson… loads:  1.465  x0.7 | dumps:  1.280  x0.4
+ ujson…………… loads:  1.868  x0.9 | dumps:  1.948  x0.6
+ pyjson5……… loads:  1.720  x0.8 | dumps:  2.347  x0.8
! json……………… loads:  2.082  x1.0 | dumps:  3.098  x1.0
- fast_json… loads:  1.845  x0.9 | dumps:  4.103  x1.3
- simplejson loads:  2.259  x1.1 | dumps:  7.107  x2.3
```

## Python 3.10

```diff
 @@ Python 3.10.15 @@
+ rapidjson… loads:  1.521  x0.6 | dumps:  1.388  x0.4
+ ujson…………… loads:  1.910  x0.8 | dumps:  2.022  x0.6
+ pyjson5……… loads:  1.924  x0.8 | dumps:  2.671  x0.8
! json……………… loads:  2.428  x1.0 | dumps:  3.534  x1.0
- fast_json… loads:  1.912  x0.8 | dumps:  4.704  x1.3
- simplejson loads:  2.718  x1.1 | dumps:  7.458  x2.1
```

## Python 3.9

```diff
@@ Python 3.9.20 @@
+ rapidjson… loads:  1.501  x0.6 | dumps:  1.348  x0.4
+ ujson…………… loads:  1.915  x0.8 | dumps:  2.027  x0.6
+ pyjson5……… loads:  1.862  x0.7 | dumps:  2.734  x0.8
! json……………… loads:  2.537  x1.0 | dumps:  3.509  x1.0
- fast_json… loads:  1.934  x0.8 | dumps:  4.821  x1.4
- simplejson loads:  2.789  x1.1 | dumps:  6.409  x1.8
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
