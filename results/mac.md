# Fatest JSON Python module on macOS

The current cross-versions winner is `python-rapidjson` :tada:

## Python 3.12

```diff
@@ Python 3.12.0 @@
+ rapidjson… loads:  2.421  x0.5 | dumps:  2.832  x0.4
+ ujson…………… loads:  3.290  x0.7 | dumps:  3.486  x0.5
! json……………… loads:  4.742  x1.0 | dumps:  6.676  x1.0
- pyjson5……… loads:  -.---  x-.- | dumps:  -.---  x-.-
- fast_json… loads:  3.522  x0.7 | dumps:  9.165  x1.4
- simplejson loads: 42.004  x8.9 | dumps: 52.725  x7.9
```

## Python 3.11

```diff
@@ Python 3.11.4 @@
+ rapidjson… loads:  2.700  x0.6 | dumps:  3.335  x0.5
+ ujson…………… loads:  3.461  x0.8 | dumps:  3.191  x0.5
+ pyjson5……… loads:  3.700  x0.8 | dumps:  4.918  x0.8
! json……………… loads:  4.439  x1.0 | dumps:  6.396  x1.0
- fast_json… loads:  3.162  x0.7 | dumps:  8.655  x1.4
- simplejson loads:  5.197  x1.2 | dumps: 14.173  x2.2
```

## Python 3.10

```diff
@@ Python 3.10.12 @@
+ rapidjson… loads:  2.162  x0.5 | dumps:  2.735  x0.4
+ ujson…………… loads:  2.646  x0.6 | dumps:  2.750  x0.4
+ pyjson5……… loads:  2.845  x0.7 | dumps:  3.805  x0.6
! json……………… loads:  4.347  x1.0 | dumps:  6.213  x1.0
- fast_json… loads:  2.607  x0.6 | dumps:  8.229  x1.3
- simplejson loads:  5.470  x1.3 | dumps: 14.352  x2.3
```

## Python 3.9

```diff
@@ Python 3.9.17 @@
+ rapidjson… loads:  2.612  x0.6 | dumps:  2.829  x0.4
+ ujson…………… loads:  2.669  x0.6 | dumps:  2.760  x0.4
+ pyjson5……… loads:  2.922  x0.6 | dumps:  3.900  x0.6
! json……………… loads:  4.604  x1.0 | dumps:  6.496  x1.0
- fast_json… loads:  2.852  x0.6 | dumps:  8.546  x1.3
- simplejson loads:  5.083  x1.1 | dumps: 11.118  x1.7
```

## Python 3.8

```diff
@@ Python 3.8.17 @@
+ ujson…………… loads:  2.714  x0.6 | dumps:  2.841  x0.5
+ rapidjson… loads:  2.549  x0.5 | dumps:  3.114  x0.5
+ pyjson5……… loads:  2.996  x0.6 | dumps:  4.219  x0.7
! json……………… loads:  4.777  x1.0 | dumps:  5.705  x1.0
- fast_json… loads:  2.777  x0.6 | dumps:  8.685  x1.5
- simplejson loads:  5.266  x1.1 | dumps: 10.581  x1.9
```
