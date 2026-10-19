## `bytes.index`

```
bytes.index(sub[, start[, end]])
bytearray.index(sub[, start[, end]])
```

Like [find()](../bytes.find/README.md), but raise [ValueError](https://docs.python.org/3.15/builtins/exceptions.html#ValueError) when the
subsequence is not found.

The subsequence to search for may be any [bytes-like object](https://docs.python.org/3.15/glossary.html#term-bytes-like-object) or an
integer in the range 0 to 255.

> *Changed in version 3.3:* Also accept an integer in the range 0 to 255 as the subsequence.
