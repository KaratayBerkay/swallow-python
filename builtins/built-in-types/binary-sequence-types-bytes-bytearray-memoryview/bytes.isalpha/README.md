## `bytes.isalpha`

```
bytes.isalpha()
bytearray.isalpha()
```

Return `True` if all bytes in the sequence are alphabetic ASCII characters
and the sequence is not empty, `False` otherwise.  Alphabetic ASCII
characters are those byte values in the sequence
`b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'`.

For example:

``` python
>>> b'ABCabc'.isalpha()
True
>>> b'ABCabc1'.isalpha()
False
```
> Code: [example_01.py](example_01.py)
