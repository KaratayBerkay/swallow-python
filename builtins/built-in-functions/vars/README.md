## `vars()`

```
vars()
vars(object, /)
```

Return the [__dict__](https://docs.python.org/3.15/reference/datamodel.html#object.__dict__) attribute for a module, class, instance,
or any other object with a `__dict__` attribute.

Objects such as modules and instances have an updateable [__dict__](https://docs.python.org/3.15/reference/datamodel.html#object.__dict__)
attribute; however, other objects may have write restrictions on their
`__dict__` attributes (for example, classes use a
[types.MappingProxyType](https://docs.python.org/3.15/library/types.html#types.MappingProxyType) to prevent direct dictionary updates).

Without an argument, vars() acts like [locals()](../locals/README.md).

A [TypeError](https://docs.python.org/3.15/builtins/exceptions.html#TypeError) exception is raised if an object is specified but
it doesn't have a [__dict__](https://docs.python.org/3.15/reference/datamodel.html#object.__dict__) attribute (for example, if
its class defines the `__slots__` attribute).

> *Changed in version 3.13:* The result of calling this function without an argument has been
> updated as described for the [locals()](../locals/README.md) builtin.
