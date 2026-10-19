## `isinstance()`

```
isinstance(object, classinfo, /)
```

Return `True` if the *object* argument is an instance of the *classinfo*
argument, or of a (direct, indirect, or `virtual`) subclass thereof.  If *object* is not
an object of the given type, the function always returns `False`.
If *classinfo* is a tuple of type objects (or recursively, other such
tuples) or a [Union Type](https://docs.python.org/3.15/builtins/stdtypes.html#types-union) of multiple types, return `True` if
*object* is an instance of any of the types.
If *classinfo* is not a type or tuple of types and such tuples,
a [TypeError](https://docs.python.org/3.15/builtins/exceptions.html#TypeError) exception is raised. [TypeError](https://docs.python.org/3.15/builtins/exceptions.html#TypeError) may not be
raised for an invalid type if an earlier check succeeds.

> *Changed in version 3.10:* *classinfo* can be a [Union Type](https://docs.python.org/3.15/builtins/stdtypes.html#types-union).
