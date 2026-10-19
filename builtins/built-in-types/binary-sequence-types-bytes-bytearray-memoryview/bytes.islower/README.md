## `bytes.islower`

```
bytes.islower()
bytearray.islower()
```

Return `True` if there is at least one lowercase ASCII character
in the sequence and no uppercase ASCII characters, `False` otherwise.

For example:

``` python
>>> b'hello world'.islower()
True
>>> b'Hello world'.islower()
False
```
> Code: [example_01.py](example_01.py)

Lowercase ASCII characters are those byte values in the sequence
`b'abcdefghijklmnopqrstuvwxyz'`. Uppercase ASCII characters
are those byte values in the sequence `b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`.
