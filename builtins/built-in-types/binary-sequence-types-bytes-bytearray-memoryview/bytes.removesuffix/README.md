## `bytes.removesuffix`

```
bytes.removesuffix(suffix, /)
bytearray.removesuffix(suffix, /)
```

If the binary data ends with the *suffix* string and that *suffix* is
not empty, return `bytes[:-len(suffix)]`.  Otherwise, return a copy of
the original binary data:

``` python
>>> b'MiscTests'.removesuffix(b'Tests')
b'Misc'
>>> b'TmpDirMixin'.removesuffix(b'Tests')
b'TmpDirMixin'
```
> Code: [example_01.py](example_01.py)

The *suffix* may be any [bytes-like object](https://docs.python.org/3.15/glossary.html#term-bytes-like-object).

> **Note**
>
> The bytearray version of this method does *not* operate in place -
> it always produces a new object, even if no changes were made.

> *Added in version 3.9.*
