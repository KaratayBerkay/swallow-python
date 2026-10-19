## `enumerate()`

```
enumerate(iterable, start=0)
```

Return an enumerate object. *iterable* must be a sequence, an
[iterator](https://docs.python.org/3.15/glossary.html#term-iterator), or some other object which supports iteration.
The [__next__()](https://docs.python.org/3.15/builtins/stdtypes.html#iterator.__next__) method of the iterator returned by
enumerate() returns a tuple containing a count (from *start* which
defaults to 0) and the values obtained from iterating over *iterable*.

``` python
>>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
```
> Code: [example_01.py](example_01.py)

Equivalent to:

``` python
def enumerate(iterable, start=0):
    n = start
    for elem in iterable:
        yield n, elem
        n += 1
```
