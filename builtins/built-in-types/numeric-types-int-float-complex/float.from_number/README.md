## `float.from_number`

```
float.from_number(x)
```

Class method to return a floating-point number constructed from a number *x*.

If the argument is an integer or a floating-point number, a
floating-point number with the same value (within Python's floating-point
precision) is returned.  If the argument is outside the range of a Python
float, an [OverflowError](https://docs.python.org/3.15/builtins/exceptions.html#OverflowError) will be raised.

For a general Python object `x`, `float.from_number(x)` delegates to
`x.__float__()`.
If [__float__()](https://docs.python.org/3.15/reference/datamodel.html#object.__float__) is not defined then it falls back
to [__index__()](https://docs.python.org/3.15/reference/datamodel.html#object.__index__).

> *Added in version 3.14.*
