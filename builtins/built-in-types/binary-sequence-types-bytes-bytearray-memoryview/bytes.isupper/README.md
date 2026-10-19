## `bytes.isupper`

```
bytes.isupper()
bytearray.isupper()
```

Return `True` if there is at least one uppercase alphabetic ASCII character
in the sequence and no lowercase ASCII characters, `False` otherwise.

For example:

``` python
>>> b'HELLO WORLD'.isupper()
True
>>> b'Hello world'.isupper()
False
```
> Code: [example_01.py](example_01.py)

Lowercase ASCII characters are those byte values in the sequence
`b'abcdefghijklmnopqrstuvwxyz'`. Uppercase ASCII characters
are those byte values in the sequence `b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`.
