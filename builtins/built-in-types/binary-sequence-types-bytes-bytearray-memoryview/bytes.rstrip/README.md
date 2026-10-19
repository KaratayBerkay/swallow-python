## `bytes.rstrip`

```
bytes.rstrip(bytes=None, /)
bytearray.rstrip(bytes=None, /)
```

Return a copy of the sequence with specified trailing bytes removed.  The
*bytes* argument is a binary sequence specifying the set of byte values to
be removed.  If omitted or `None`, the *bytes* argument defaults to
removing [ASCII whitespace](../bytes.isspace/README.md).
The *bytes* argument is not a suffix; rather,
all combinations of its values are stripped:

``` python
>>> b'   spacious   '.rstrip()
b'   spacious'
>>> b'mississippi'.rstrip(b'ipz')
b'mississ'
```
> Code: [example_01.py](example_01.py)

The binary sequence of byte values to remove may be any
[bytes-like object](https://docs.python.org/3.15/glossary.html#term-bytes-like-object). See [removesuffix()](../bytes.removesuffix/README.md) for a method
that will remove a single suffix string rather than all of a set of
characters.  For example:

``` python
>>> b'Monty Python'.rstrip(b' Python')
b'M'
>>> b'Monty Python'.removesuffix(b' Python')
b'Monty'
```
> Code: [example_02.py](example_02.py)

> **Note**
>
> The bytearray version of this method does *not* operate in place -
> it always produces a new object, even if no changes were made.
