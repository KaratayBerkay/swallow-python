## `getattr()`

```
getattr(object, name, /)
getattr(object, name, default, /)
```

Return the value of the named attribute of *object*.  *name* must be a string.
If the string is the name of one of the object's attributes, the result is the
value of that attribute.  For example, `getattr(x, 'foobar')` is equivalent to
`x.foobar`.  If the named attribute does not exist, *default* is returned if
provided, otherwise [AttributeError](https://docs.python.org/3.15/builtins/exceptions.html#AttributeError) is raised.
*name* need not be a Python identifier (see [setattr()](../setattr/README.md)).

> **Note**
>
> Since [private name mangling](https://docs.python.org/3.15/reference/expressions.html#private-name-mangling) happens at
> compilation time, one must manually mangle a private attribute's
> (attributes with two leading underscores) name in order to retrieve it with
> getattr().
