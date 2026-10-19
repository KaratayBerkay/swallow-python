## `bytes.find`

```
bytes.find(sub[, start[, end]])
bytearray.find(sub[, start[, end]])
```

Return the lowest index in the data where the subsequence *sub* is found,
such that *sub* is contained in the slice `s[start:end]`.  Optional
arguments *start* and *end* are interpreted as in slice notation.  Return
`-1` if *sub* is not found.

The subsequence to search for may be any [bytes-like object](https://docs.python.org/3.15/glossary.html#term-bytes-like-object) or an
integer in the range 0 to 255.

> **Note**
>
> The find() method should be used only if you need to know the
> position of *sub*.  To check if *sub* is a substring or not, use the
> `in` operator:
>
> ``` python
> >>> b'Py' in b'Python'
> True
> ```
> > Code: [example_01.py](example_01.py)

> *Changed in version 3.3:* Also accept an integer in the range 0 to 255 as the subsequence.
