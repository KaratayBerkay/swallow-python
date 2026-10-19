## `bytes.lower`

```
bytes.lower()
bytearray.lower()
```

Return a copy of the sequence with all the uppercase ASCII characters
converted to their corresponding lowercase counterpart.

For example:

``` python
>>> b'Hello World'.lower()
b'hello world'
```
> Code: [example_01.py](example_01.py)

Lowercase ASCII characters are those byte values in the sequence
`b'abcdefghijklmnopqrstuvwxyz'`. Uppercase ASCII characters
are those byte values in the sequence `b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`.

> **Note**
>
> The bytearray version of this method does *not* operate in place - it
> always produces a new object, even if no changes were made.
