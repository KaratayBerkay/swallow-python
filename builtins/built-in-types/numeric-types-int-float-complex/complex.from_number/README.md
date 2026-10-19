## `complex.from_number`

```
complex.from_number(x)
```

Class method to convert a number to a complex number.

For a general Python object `x`, `complex.from_number(x)` delegates to
`x.__complex__()`.  If [__complex__()](https://docs.python.org/3.15/reference/datamodel.html#object.__complex__) is not defined then it falls back
to [__float__()](https://docs.python.org/3.15/reference/datamodel.html#object.__float__).  If `__float__()` is not defined then it falls back
to [__index__()](https://docs.python.org/3.15/reference/datamodel.html#object.__index__).

> *Added in version 3.14.*
