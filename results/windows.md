# Fatest JSON Python module on Windows

## Results

The current cross-versions winner is `usjon` :tada:

### Python 3.12

```diff
@@ Python 3.12.0 @@
+ ujson…………… loads:  2.426  x0.8 | dumps:  2.415  x0.6
! json……………… loads:  2.906  x1.0 | dumps:  4.136  x1.0
- rapidjson… loads:  3.233  x1.1 | dumps:  3.045  x0.7
- fast_json… loads:  2.436  x0.8 | dumps:  5.195  x1.3
- simplejson loads: 25.721  x8.9 | dumps: 30.215  x7.3
```

### Python 3.11

```diff
@@ Python 3.11.3 @@
+ ujson…………… loads:  2.124  x0.7 | dumps:  2.315  x0.5
! json……………… loads:  3.159  x1.0 | dumps:  4.607  x1.0
- rapidjson… loads:  3.432  x1.1 | dumps:  3.114  x0.7
- fast_json… loads:  2.184  x0.7 | dumps:  5.927  x1.3
- simplejson loads:  4.529  x1.4 | dumps:  9.320  x2.0
```

### Python 3.10

```diff
@@ Python 3.10.11 @@
+ ujson…………… loads:  2.441  x0.7 | dumps:  2.325  x0.5
+ rapidjson… loads:  3.288  x1.0 | dumps:  2.586  x0.5
! json……………… loads:  3.351  x1.0 | dumps:  5.065  x1.0
- fast_json… loads:  2.461  x0.7 | dumps:  6.493  x1.3
- simplejson loads:  3.958  x1.2 | dumps:  9.319  x1.8
```

### Python 3.9

```diff
@@ Python 3.9.13 @@
+ ujson…………… loads:  2.346  x0.7 | dumps:  2.278  x0.5
+ rapidjson… loads:  3.249  x1.0 | dumps:  3.226  x0.7
! json……………… loads:  3.286  x1.0 | dumps:  4.626  x1.0
- fast_json… loads:  2.348  x0.7 | dumps:  6.178  x1.3
- simplejson loads:  4.168  x1.3 | dumps:  7.906  x1.7
```

### Python 3.8

```diff
@@ Python 3.8.10 @@
+ ujson…………… loads:  2.435  x0.6 | dumps:  2.398  x0.4
+ rapidjson… loads:  3.442  x0.8 | dumps:  2.603  x0.5
! json……………… loads:  4.162  x1.0 | dumps:  5.663  x1.0
- fast_json… loads:  2.804  x0.7 | dumps:  7.109  x1.3
- simplejson loads:  4.464  x1.1 | dumps:  8.292  x1.5
```

### Python 3.7

```diff
@@ Python 3.7.9 @@
+ rapidjson… loads:  3.383  x0.9 | dumps:  2.355  x0.5
! json……………… loads:  3.750  x1.0 | dumps:  4.558  x1.0
- ujson…………… loads:  3.887  x1.0 | dumps:  4.226  x0.9
- fast_json… loads:  3.928  x1.0 | dumps:  6.085  x1.3
- simplejson loads:  4.340  x1.2 | dumps:  7.564  x1.7
```
