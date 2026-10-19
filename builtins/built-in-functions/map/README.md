## `map()`

```
map(function, iterable, /, *iterables, strict=False)
```

Return an iterator that applies *function* to every item of *iterable*,
yielding the results.  If additional *iterables* arguments are passed,
*function* must take that many arguments and is applied to the items from all
iterables in parallel.  With multiple iterables, the iterator stops when the
shortest iterable is [exhausted](https://docs.python.org/3.15/glossary.html#term-exhausted).  If *strict* is `True` and one of the
iterables is exhausted before the others, a [ValueError](https://docs.python.org/3.15/builtins/exceptions.html#ValueError) is raised. For
cases where the function inputs are already arranged into argument tuples,
see [itertools.starmap()](https://docs.python.org/3.15/library/itertools.html#itertools.starmap).

> *Changed in version 3.14:* Added the *strict* parameter.
