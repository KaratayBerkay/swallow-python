## 10.2. File wildcards

The `glob` module provides a function for making file lists from directory wildcard searches:

``` python
>>> import glob
>>> glob.glob('*.py')
['primes.py', 'random.py', 'quote.py']
```
> Code: [glob_example.py](glob_example.py)
