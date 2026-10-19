## `setattr()`

```
setattr(object, name, value, /)
```

This is the counterpart of [getattr()](../getattr/README.md).  The arguments are an object, a
string, and an arbitrary value.  The string may name an existing attribute or a
new attribute.  The function assigns the value to the attribute, provided the
object allows it.  For example, `setattr(x, 'foobar', 123)` is equivalent to
`x.foobar = 123`.

*name* need not be a Python identifier as defined in [Names (identifiers and keywords)](https://docs.python.org/3.15/reference/lexical_analysis.html#identifiers)
unless the object chooses to enforce that, for example in a custom
[__getattribute__()](https://docs.python.org/3.15/reference/datamodel.html#object.__getattribute__) or via `__slots__`.
An attribute whose name is not an identifier will not be accessible using
the dot notation, but is accessible through [getattr()](../getattr/README.md) etc..

> **Note**
>
> Since [private name mangling](https://docs.python.org/3.15/reference/expressions.html#private-name-mangling) happens at
> compilation time, one must manually mangle a private attribute's
> (attributes with two leading underscores) name in order to set it with
> setattr().
