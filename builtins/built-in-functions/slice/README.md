## `slice()`

```
slice(stop, /)
slice(start, stop, step=None, /)
```

Return a [slice](https://docs.python.org/3.15/glossary.html#term-slice) object representing the set of indices specified by
`range(start, stop, step)`.  The *start* and *step* arguments default to
`None`.

Slice objects are also generated when [slicing syntax](https://docs.python.org/3.15/reference/expressions.html#slicings)
is used.  For example: `a[start:stop:step]` or `a[start:stop, i]`.

See [itertools.islice()](https://docs.python.org/3.15/library/itertools.html#itertools.islice) for an alternate version that returns an
[iterator](https://docs.python.org/3.15/glossary.html#term-iterator).

### slice.start, slice.stop, slice.step

These read-only attributes are set to the argument values
(or their default).  They have no other explicit functionality;
however, they are used by NumPy and other third-party packages.

> *Changed in version 3.12:* Slice objects are now [hashable](https://docs.python.org/3.15/glossary.html#term-hashable) (provided [start](https://docs.python.org/3.15/builtins/functions.html#slice.start),
> [stop](https://docs.python.org/3.15/builtins/functions.html#slice.stop), and [step](https://docs.python.org/3.15/builtins/functions.html#slice.step) are hashable).
