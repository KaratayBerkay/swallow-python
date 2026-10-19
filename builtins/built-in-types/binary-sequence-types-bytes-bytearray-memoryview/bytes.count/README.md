## `bytes.count`

```
bytes.count(sub[, start[, end]])
bytearray.count(sub[, start[, end]])
```

Return the number of non-overlapping occurrences of subsequence *sub* in
the range [*start*, *end*].  Optional arguments *start* and *end* are
interpreted as in slice notation.

The subsequence to search for may be any [bytes-like object](https://docs.python.org/3.15/glossary.html#term-bytes-like-object) or an
integer in the range 0 to 255.

If *sub* is empty, returns the number of empty slices between characters
which is the length of the bytes object plus one.

> *Changed in version 3.3:* Also accept an integer in the range 0 to 255 as the subsequence.
