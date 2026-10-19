## `container.__iter__`

```
container.__iter__()
```

Return an [iterator](https://docs.python.org/3.15/glossary.html#term-iterator) object.  The object is required to support the
iterator protocol described below.  If a container supports different types
of iteration, additional methods can be provided to specifically request
iterators for those iteration types.  (An example of an object supporting
multiple forms of iteration would be a tree structure which supports both
breadth-first and depth-first traversal.)  This method corresponds to the
[tp_iter](https://docs.python.org/3.15/c-api/typeobj.html#c.PyTypeObject.tp_iter) slot of the type structure for Python
objects in the Python/C API.
