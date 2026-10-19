## `next()`

```
next(iterator, /)
next(iterator, default, /)
```

Retrieve the next item from the [iterator](https://docs.python.org/3.15/glossary.html#term-iterator) by calling its
[__next__()](https://docs.python.org/3.15/builtins/stdtypes.html#iterator.__next__) method.  If *default* is given, it is returned
if the iterator is [exhausted](https://docs.python.org/3.15/glossary.html#term-exhausted), otherwise [StopIteration](https://docs.python.org/3.15/builtins/exceptions.html#StopIteration) is raised.
