## `iterator.__iter__`

```
iterator.__iter__()
```

Return the [iterator](https://docs.python.org/3.15/glossary.html#term-iterator) object itself.  This is required to allow both
containers and iterators to be used with the `for` and
`in` statements.  This method corresponds to the
[tp_iter](https://docs.python.org/3.15/c-api/typeobj.html#c.PyTypeObject.tp_iter) slot of the type structure for Python
objects in the Python/C API.
