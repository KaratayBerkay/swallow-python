## `bytes.rindex`

```
bytes.rindex(sub[, start[, end]])
bytearray.rindex(sub[, start[, end]])
```

Like [rfind()](../bytes.rfind/README.md) but raises [ValueError](https://docs.python.org/3.15/builtins/exceptions.html#ValueError) when the
subsequence *sub* is not found.

The subsequence to search for may be any [bytes-like object](https://docs.python.org/3.15/glossary.html#term-bytes-like-object) or an
integer in the range 0 to 255.

> *Changed in version 3.3:* Also accept an integer in the range 0 to 255 as the subsequence.
