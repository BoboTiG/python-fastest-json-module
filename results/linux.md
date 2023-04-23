# Fatest JSON Python module on GNU/Linux

## Results

The current cross-versions winner is `python-rapidjson` :tada:

### Python 3.12

```diff
@@ Python 3.12.0 @@
+ rapidjson… loads:  2.005  x0.7 | dumps:  2.142  x0.5
+ ujson…………… loads:  2.118  x0.8 | dumps:  2.508  x0.6
! json……………… loads:  2.694  x1.0 | dumps:  4.261  x1.0
- fast_json… loads:  2.092  x0.8 | dumps:  5.578  x1.3
- simplejson loads: 25.065  x9.3 | dumps: 27.842  x6.5
```

### Python 3.11

```diff
@@ Python 3.11.3 @@
+ rapidjson… loads:  1.995  x0.7 | dumps:  1.764  x0.4
+ ujson…………… loads:  2.203  x0.7 | dumps:  2.185  x0.5
! json……………… loads:  3.014  x1.0 | dumps:  4.846  x1.0
- fast_json… loads:  2.197  x0.7 | dumps:  5.838  x1.2
- simplejson loads:  3.172  x1.1 | dumps:  8.808  x1.8
```

### Python 3.10

```diff
@@ Python 3.10.11 @@
+ rapidjson… loads:  2.048  x0.6 | dumps:  1.821  x0.4
+ ujson…………… loads:  2.260  x0.7 | dumps:  2.265  x0.5
! json……………… loads:  3.277  x1.0 | dumps:  4.900  x1.0
- fast_json… loads:  2.201  x0.7 | dumps:  6.432  x1.3
- simplejson loads:  3.626  x1.1 | dumps:  9.292  x1.9
```

### Python 3.9

```diff
@@ Python 3.9.16 @@
+ rapidjson… loads:  2.520  x0.6 | dumps:  2.266  x0.4
+ ujson…………… loads:  2.714  x0.7 | dumps:  2.810  x0.5
! json……………… loads:  4.149  x1.0 | dumps:  6.036  x1.0
- fast_json… loads:  2.670  x0.6 | dumps:  8.192  x1.4
- simplejson loads:  4.694  x1.1 | dumps: 10.459  x1.7
```

### Python 3.8

```diff
@@ Python 3.8.16 @@
+ rapidjson… loads:  2.565  x0.6 | dumps:  2.150  x0.4
+ ujson…………… loads:  2.610  x0.6 | dumps:  3.006  x0.6
! json……………… loads:  4.042  x1.0 | dumps:  5.406  x1.0
- fast_json… loads:  2.441  x0.6 | dumps:  7.763  x1.4
- simplejson loads:  4.436  x1.1 | dumps: 10.150  x1.9
```

### Python 3.7

```diff
@@ Python 3.7.16 @@
+ rapidjson… loads:  2.494  x0.6 | dumps:  2.155  x0.4
+ ujson…………… loads:  2.813  x0.7 | dumps:  2.821  x0.5
! json……………… loads:  4.120  x1.0 | dumps:  5.662  x1.0
- fast_json… loads:  2.632  x0.6 | dumps:  7.649  x1.4
- simplejson loads:  4.836  x1.2 | dumps: 10.162  x1.8
```
