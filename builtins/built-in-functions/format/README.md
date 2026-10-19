## `format()`

```
format(value, format_spec="", /)
```

Convert a *value* to a "formatted" representation, as controlled by
*format_spec*.  The interpretation of *format_spec* will depend on the type
of the *value* argument; however, there is a standard formatting syntax that
is used by most built-in types: [Format specification mini-language](https://docs.python.org/3.15/library/string.html#formatspec).

The default *format_spec* is an empty string which usually gives the same
effect as calling `str(value)`.

A call to `format(value, format_spec)` is translated to
`type(value).__format__(value, format_spec)` which bypasses the instance
dictionary when searching for the value's [__format__()](https://docs.python.org/3.15/reference/datamodel.html#object.__format__) method.
A [TypeError](https://docs.python.org/3.15/builtins/exceptions.html#TypeError) exception is raised if the method search reaches
`object` and the *format_spec* is non-empty, or if either the
*format_spec* or the return value are not strings.

> *Changed in version 3.4:* `object().__format__(format_spec)` raises [TypeError](https://docs.python.org/3.15/builtins/exceptions.html#TypeError)
> if *format_spec* is not an empty string.
