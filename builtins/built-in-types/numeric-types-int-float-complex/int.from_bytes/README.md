## `int.from_bytes`

```
int.from_bytes(bytes, byteorder='big', *, signed=False)
```

Return the integer represented by the given array of bytes.

``` python
>>> int.from_bytes(b'\x00\x10', byteorder='big')
16
>>> int.from_bytes(b'\x00\x10', byteorder='little')
4096
>>> int.from_bytes(b'\xfc\x00', byteorder='big', signed=True)
-1024
>>> int.from_bytes(b'\xfc\x00', byteorder='big', signed=False)
64512
>>> int.from_bytes([255, 0, 0], byteorder='big')
16711680
```
> Code: [example_01.py](example_01.py)

The argument *bytes* must either be a [bytes-like object](https://docs.python.org/3.15/glossary.html#term-bytes-like-object) or an
iterable producing bytes.

The *byteorder* argument determines the byte order used to represent the
integer, and defaults to `"big"`.  If *byteorder* is
`"big"`, the most significant byte is at the beginning of the byte
array.  If *byteorder* is `"little"`, the most significant byte is at
the end of the byte array.  To request the native byte order of the host
system, use [sys.byteorder](https://docs.python.org/3.15/library/sys.html#sys.byteorder) as the byte order value.

The *signed* argument indicates whether two's complement is used to
represent the integer.

Equivalent to:

``` python
def from_bytes(bytes, byteorder='big', signed=False):
    if byteorder == 'little':
        little_ordered = list(bytes)
    elif byteorder == 'big':
        little_ordered = list(reversed(bytes))
    else:
        raise ValueError("byteorder must be either 'little' or 'big'")

    n = sum(b << i*8 for i, b in enumerate(little_ordered))
    if signed and little_ordered and (little_ordered[-1] & 0x80):
        n -= 1 << 8*len(little_ordered)

    return n
```

> *Added in version 3.2.*

> *Changed in version 3.11:* Added default argument value for `byteorder`.
