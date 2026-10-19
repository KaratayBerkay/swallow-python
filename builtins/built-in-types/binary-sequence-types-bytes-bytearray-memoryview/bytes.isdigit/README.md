## `bytes.isdigit`

```
bytes.isdigit()
bytearray.isdigit()
```

Return `True` if all bytes in the sequence are ASCII decimal digits
and the sequence is not empty, `False` otherwise. ASCII decimal digits are
those byte values in the sequence `b'0123456789'`.

For example:

``` python
>>> b'1234'.isdigit()
True
>>> b'1.23'.isdigit()
False
```
> Code: [example_01.py](example_01.py)
