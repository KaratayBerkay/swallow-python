## 10.6. Mathematics

The `math` module gives access to the underlying C library functions for floating-point math:

``` python
>>> import math
>>> math.cos(math.pi / 4)
0.70710678118654757
>>> math.log(1024, 2)
10.0
```
> Code: [math_example.py](math_example.py)

The `random` module provides tools for making random selections:

``` python
>>> import random
>>> random.choice(['apple', 'pear', 'banana'])
'apple'
>>> random.sample(range(100), 10)   # sampling without replacement
[30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
>>> random.random()    # random float from the interval [0.0, 1.0)
0.17970987693706186
>>> random.randrange(6)    # random integer chosen from range(6)
4
```
> Code: [random_example.py](random_example.py)

The `statistics` module calculates basic statistical properties (the mean, median, variance, etc.) of numeric data:

``` python
>>> import statistics
>>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
>>> statistics.mean(data)
1.6071428571428572
>>> statistics.median(data)
1.25
>>> statistics.variance(data)
1.3720238095238095
```
> Code: [data.py](data.py)

The SciPy project \<[https://scipy.org](https://scipy.org)\> has many other modules for numerical computations.
