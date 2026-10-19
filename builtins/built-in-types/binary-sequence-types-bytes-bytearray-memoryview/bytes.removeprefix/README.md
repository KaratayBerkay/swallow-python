## `bytes.removeprefix`

```
bytes.removeprefix(prefix, /)
bytearray.removeprefix(prefix, /)
```

If the binary data starts with the *prefix* string, return
`bytes[len(prefix):]`. Otherwise, return a copy of the original
binary data:

``` python
>>> b'TestHook'.removeprefix(b'Test')
b'Hook'
>>> b'BaseTestCase'.removeprefix(b'Test')
b'BaseTestCase'
```
> Code: [example_01.py](example_01.py)

The *prefix* may be any [bytes-like object](https://docs.python.org/3.15/glossary.html#term-bytes-like-object).

> **Note**
>
> The bytearray version of this method does *not* operate in place -
> it always produces a new object, even if no changes were made.

> *Added in version 3.9.*
