## `issubclass()`

```
issubclass(cls, classinfo, /)
```

Return `True` if *cls* is a subclass (direct, indirect, or [virtual](https://docs.python.org/3.15/glossary.html#term-abstract-base-class)) of *classinfo*.  A
class is considered a subclass of itself. *classinfo* may be a tuple of class
objects (or recursively, other such tuples)
or a [Union Type](https://docs.python.org/3.15/builtins/stdtypes.html#types-union), in which case return `True` if *cls* is a
subclass of any entry in *classinfo*.  In any other case, a [TypeError](https://docs.python.org/3.15/builtins/exceptions.html#TypeError)
exception is raised.

> *Changed in version 3.10:* *classinfo* can be a [Union Type](https://docs.python.org/3.15/builtins/stdtypes.html#types-union).
