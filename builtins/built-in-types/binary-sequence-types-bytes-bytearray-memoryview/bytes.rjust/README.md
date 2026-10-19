## `bytes.rjust`

```
bytes.rjust(width, fillbyte=b' ', /)
bytearray.rjust(width, fillbyte=b' ', /)
```

Return a copy of the object right justified in a sequence of length *width*.
Padding is done using the specified *fillbyte* (default is an ASCII
space). For [bytes](../bytes/README.md) objects, the original sequence is returned if
*width* is less than or equal to `len(s)`.

> **Note**
>
> The bytearray version of this method does *not* operate in place -
> it always produces a new object, even if no changes were made.
