## `len()`

```
len(object, /)
```

Return the length (the number of items) of an object.  The argument may be a
sequence (such as a string, bytes, tuple, list, or range) or a collection
(such as a dictionary, set, or frozen set).

> **CPython implementation detail:** `len` raises [OverflowError](https://docs.python.org/3.15/builtins/exceptions.html#OverflowError) on lengths larger than
> [sys.maxsize](https://docs.python.org/3.15/library/sys.html#sys.maxsize), such as [range(2 ** 100)](../range/README.md).
