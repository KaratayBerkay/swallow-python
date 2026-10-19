## `int.to_bytes`

```
int.to_bytes(length=1, byteorder='big', *, signed=False)
```

Return an array of bytes representing an integer.

``` python
>>> (1024).to_bytes(2, byteorder='big')
b'\x04\x00'
>>> (1024).to_bytes(10, byteorder='big')
b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00'
>>> (-1024).to_bytes(10, byteorder='big', signed=True)
b'\xff\xff\xff\xff\xff\xff\xff\xff\xfc\x00'
>>> x = 1000
>>> x.to_bytes((x.bit_length() + 7) // 8, byteorder='little')
b'\xe8\x03'
```
> Code: [example_01.py](example_01.py)

The integer is represented using *length* bytes, and defaults to 1.  An
[OverflowError](https://docs.python.org/3.15/builtins/exceptions.html#OverflowError) is raised if the integer is not representable with
the given number of bytes.

The *byteorder* argument determines the byte order used to represent the
integer, and defaults to `"big"`.  If *byteorder* is
`"big"`, the most significant byte is at the beginning of the byte
array.  If *byteorder* is `"little"`, the most significant byte is at
the end of the byte array.

The *signed* argument determines whether two's complement is used to
represent the integer.  If *signed* is `False` and a negative integer is
given, an [OverflowError](https://docs.python.org/3.15/builtins/exceptions.html#OverflowError) is raised. The default value for *signed*
is `False`.

The default values can be used to conveniently turn an integer into a
single byte object:

``` python
>>> (65).to_bytes()
b'A'
```
> Code: [example_02.py](example_02.py)

However, when using the default arguments, don't try
to convert a value greater than 255 or you'll get an [OverflowError](https://docs.python.org/3.15/builtins/exceptions.html#OverflowError).

Equivalent to:

``` python
def to_bytes(n, length=1, byteorder='big', signed=False):
    if byteorder == 'little':
        order = range(length)
    elif byteorder == 'big':
        order = reversed(range(length))
    else:
        raise ValueError("byteorder must be either 'little' or 'big'")

    return bytes((n >> i*8) & 0xff for i in order)
```

> *Added in version 3.2.*

> *Changed in version 3.11:* Added default argument values for `length` and `byteorder`.
