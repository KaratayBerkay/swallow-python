## `iterator.__next__`

```
iterator.__next__()
```

Return the next item from the [iterator](https://docs.python.org/3.15/glossary.html#term-iterator).  If there are no further
items, raise the [StopIteration](https://docs.python.org/3.15/builtins/exceptions.html#StopIteration) exception.  This method corresponds to
the [tp_iternext](https://docs.python.org/3.15/c-api/typeobj.html#c.PyTypeObject.tp_iternext) slot of the type structure for
Python objects in the Python/C API.
