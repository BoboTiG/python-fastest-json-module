# Fatest JSON Python module on GNU/Linux

The current cross-versions winner is `python-rapidjson` :tada:

## Python 3.12

```diff
@@ Python 3.12.0 @@
+ rapidjson… loads:  2.798  x0.8 | dumps:  2.967  x0.6
+ ujson…………… loads:  3.449  x1.0 | dumps:  3.906  x0.8
! json……………… loads:  3.454  x1.0 | dumps:  4.935  x1.0
- pyjson5……… loads:  -.---  x-.- | dumps:  -.---  x-.-
- fast_json… loads:  3.343  x1.0 | dumps:  8.050  x1.6
- simplejson loads: 37.018 x10.7 | dumps: 42.891  x8.7
```

## Python 3.11

```diff
@@ Python 3.11.4 @@
+ rapidjson… loads:  2.100  x0.7 | dumps:  1.766  x0.4
+ ujson…………… loads:  2.111  x0.7 | dumps:  2.277  x0.5
+ pyjson5……… loads:  2.661  x0.9 | dumps:  3.497  x0.8
! json……………… loads:  2.886  x1.0 | dumps:  4.358  x1.0
- fast_json… loads:  2.121  x0.7 | dumps:  5.726  x1.3
- simplejson loads:  3.253  x1.1 | dumps:  9.159  x2.1
```

## Python 3.10

```diff
@@ Python 3.10.12 @@
+ rapidjson… loads:  2.491  x0.6 | dumps:  2.304  x0.4
+ ujson…………… loads:  2.740  x0.7 | dumps:  2.823  x0.5
+ pyjson5……… loads:  3.431  x0.9 | dumps:  4.210  x0.7
! json……………… loads:  4.009  x1.0 | dumps:  5.924  x1.0
- fast_json… loads:  2.747  x0.7 | dumps:  7.969  x1.3
- simplejson loads:  4.559  x1.1 | dumps: 11.631  x2.0
```

## Python 3.9

```diff
@@ Python 3.9.17 @@
+ rapidjson… loads:  2.144  x0.6 | dumps:  1.966  x0.4
+ ujson…………… loads:  2.214  x0.6 | dumps:  2.294  x0.4
+ pyjson5……… loads:  3.031  x0.9 | dumps:  3.817  x0.7
! json……………… loads:  3.468  x1.0 | dumps:  5.164  x1.0
- fast_json… loads:  2.228  x0.6 | dumps:  6.842  x1.3
- simplejson loads:  4.043  x1.2 | dumps:  8.679  x1.7
```

## Python 3.8

```diff
@@ Python 3.8.17 @@
+ rapidjson… loads:  2.497  x0.6 | dumps:  2.192  x0.4
+ ujson…………… loads:  2.555  x0.6 | dumps:  2.947  x0.5
+ pyjson5……… loads:  3.122  x0.8 | dumps:  4.186  x0.8
! json……………… loads:  4.006  x1.0 | dumps:  5.580  x1.0
- fast_json… loads:  2.591  x0.6 | dumps:  7.842  x1.4
- simplejson loads:  4.406  x1.1 | dumps:  9.891  x1.8
```
