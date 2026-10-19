## `callable()`

```
callable(object, /)
```

Return [True](https://docs.python.org/3.15/builtins/constants.html#True) if the *object* argument appears callable,
[False](https://docs.python.org/3.15/builtins/constants.html#False) if not.  If this returns `True`, it is still possible that a
call fails, but if it is `False`, calling *object* will never succeed.
Note that classes are callable (calling a class returns a new instance);
instances are callable if their class has a [__call__()](https://docs.python.org/3.15/reference/datamodel.html#object.__call__) method.

> *Added in version 3.2:* This function was first removed in Python 3.0 and then brought back
> in Python 3.2.
