# Fatest JSON Python module on macOS

## Results

The current cross-versions winner is `python-rapidjson` :tada:

### Python 3.12

```diff
@@ Python 3.12.0 @@
+ rapidjson… loads:  1.865  x0.5 | dumps:  2.449  x0.5
+ ujson…………… loads:  2.494  x0.7 | dumps:  2.692  x0.6
! json……………… loads:  3.407  x1.0 | dumps:  4.856  x1.0
- fast_json… loads:  2.509  x0.7 | dumps:  7.060  x1.5
- simplejson loads: 33.632  x9.9 | dumps: 48.556 x10.0
```

### Python 3.11

```diff
@@ Python 3.11.3 @@
+ rapidjson… loads:  2.133  x0.6 | dumps:  2.585  x0.5
+ ujson…………… loads:  2.544  x0.7 | dumps:  2.491  x0.5
! json……………… loads:  3.585  x1.0 | dumps:  5.292  x1.0
- fast_json… loads:  2.516  x0.7 | dumps:  7.132  x1.3
- simplejson loads:  4.357  x1.2 | dumps: 11.256  x2.1
```

### Python 3.10

```diff
@@ Python 3.10.11 @@
+ rapidjson… loads:  2.142  x0.5 | dumps:  2.803  x0.5
+ ujson…………… loads:  2.561  x0.6 | dumps:  2.821  x0.5
! json……………… loads:  4.376  x1.0 | dumps:  5.772  x1.0
- fast_json… loads:  2.547  x0.6 | dumps:  7.771  x1.3
- simplejson loads:  5.068  x1.2 | dumps: 12.154  x2.1
```

### Python 3.9

```diff
@@ Python 3.9.16 @@
+ rapidjson… loads:  2.318  x0.5 | dumps:  2.768  x0.5
+ ujson…………… loads:  2.704  x0.6 | dumps:  2.657  x0.4
! json……………… loads:  4.709  x1.0 | dumps:  6.124  x1.0
- fast_json… loads:  2.682  x0.6 | dumps:  8.380  x1.4
- simplejson loads:  5.286  x1.1 | dumps: 11.101  x1.8
```

### Python 3.8

```diff
@@ Python 3.8.16 @@
+ rapidjson… loads:  2.466  x0.5 | dumps:  2.936  x0.5
+ ujson…………… loads:  2.661  x0.6 | dumps:  2.796  x0.4
! json……………… loads:  4.617  x1.0 | dumps:  6.291  x1.0
- fast_json… loads:  2.713  x0.6 | dumps:  9.002  x1.4
- simplejson loads:  5.275  x1.1 | dumps: 10.932  x1.7
```

### Python 3.7

```diff
@@ Python 3.7.16 @@
+ rapidjson… loads:  2.472  x0.5 | dumps:  2.767  x0.5
+ ujson…………… loads:  2.636  x0.5 | dumps:  2.740  x0.5
! json……………… loads:  4.936  x1.0 | dumps:  6.051  x1.0
- fast_json… loads:  2.636  x0.5 | dumps:  8.516  x1.4
- simplejson loads:  5.638  x1.1 | dumps: 10.100  x1.7
```
