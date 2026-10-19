## `set`

```
set(iterable=(), /)
frozenset(iterable=(), /)
```

Return a new set or frozenset object whose elements are taken from
*iterable*.  The elements of a set must be [hashable](https://docs.python.org/3.15/glossary.html#term-hashable).  To
represent sets of sets, the inner sets must be frozenset
objects.  If *iterable* is not specified, a new empty set is
returned.
