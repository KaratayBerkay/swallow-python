## `bytes.replace`

```
bytes.replace(old, new, /, count=-1)
bytearray.replace(old, new, /, count=-1)
```

Return a copy of the sequence with all occurrences of subsequence *old*
replaced by *new*.  If *count* is given, only the first *count* occurrences
are replaced.  If *count* is not specified or `-1`, then all occurrences
are replaced.

The subsequence to search for and its replacement may be any
[bytes-like object](https://docs.python.org/3.15/glossary.html#term-bytes-like-object).

> **Note**
>
> The bytearray version of this method does *not* operate in place - it
> always produces a new object, even if no changes were made.

> *Changed in version 3.15:* *count* is now supported as a keyword argument.
