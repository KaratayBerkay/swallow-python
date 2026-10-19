## `sorted()`

```
sorted(iterable, /, *, key=None, reverse=False)
```

Return a new sorted list from the items in *iterable*.

Has two optional arguments which must be specified as keyword arguments.

*key* specifies a function of one argument that is used to extract a comparison
key from each element in *iterable* (for example, `key=str.lower`).  The
default value is `None` (compare the elements directly).

*reverse* is a boolean value.  If set to `True`, then the list elements are
sorted as if each comparison were reversed.

Use [functools.cmp_to_key()](https://docs.python.org/3.15/library/functools.html#functools.cmp_to_key) to convert an old-style *cmp* function to a
*key* function.

The built-in sorted() function is guaranteed to be stable. A sort is
stable if it guarantees not to change the relative order of elements that
compare equal --- this is helpful for sorting in multiple passes (for
example, sort by department, then by salary grade).

The sort algorithm uses only `<` comparisons between items.  While
defining an [__lt__()](https://docs.python.org/3.15/reference/datamodel.html#object.__lt__) method will suffice for sorting,
[PEP 8](https://peps.python.org/pep-8/) recommends that all six [rich comparisons](https://docs.python.org/3.15/reference/expressions.html#comparisons) be implemented.  This will help avoid bugs when using
the same data with other ordering tools such as [max()](../max/README.md) that rely
on a different underlying method.  Implementing all six comparisons
also helps avoid confusion for mixed type comparisons which can call
the reflected [__gt__()](https://docs.python.org/3.15/reference/datamodel.html#object.__gt__) method.

For sorting examples and a brief sorting tutorial, see [Sorting Techniques](https://docs.python.org/3.15/howto/sorting.html#sortinghowto).
