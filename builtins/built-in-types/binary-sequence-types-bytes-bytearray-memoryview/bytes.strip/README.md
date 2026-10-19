## `bytes.strip`

```
bytes.strip(bytes=None, /)
bytearray.strip(bytes=None, /)
```

Return a copy of the sequence with specified leading and trailing bytes
removed. The *bytes* argument is a binary sequence specifying the set of
byte values to be removed.  If omitted or `None`, the *bytes*
argument defaults to removing [ASCII whitespace](../bytes.isspace/README.md).
The *bytes* argument is
not a prefix or suffix; rather, all combinations of its values are
stripped:

``` python
>>> b'   spacious   '.strip()
b'spacious'
>>> b'www.example.com'.strip(b'cmowz.')
b'example'
```
> Code: [example_01.py](example_01.py)

The binary sequence of byte values to remove may be any
[bytes-like object](https://docs.python.org/3.15/glossary.html#term-bytes-like-object).

> **Note**
>
> The bytearray version of this method does *not* operate in place -
> it always produces a new object, even if no changes were made.
