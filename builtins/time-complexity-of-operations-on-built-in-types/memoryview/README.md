[memoryview](../../built-in-types/binary-sequence-types-bytes-bytearray-memoryview/memoryview/README.md) objects allow Python code to access the internal data
of an object that supports the [buffer protocol](https://docs.python.org/3.15/c-api/buffer.html#bufferobjects) without
copying. In particular, slicing a memory view returns a new view onto the same
buffer.

| Operation | Complexity |
| --- | --- |
| Create (`memoryview(obj)`) | *O*(1) |
| Get item (`v[k]`) | *O*(1) |
| Get slice (`v[i:j]`) | *O*(1) |
| Index (`v.index(x)`) [^1] [^2] | *O*(*n*) |
| Count (`v.count(x)`) [^2] | *O*(*n*) |
| Convert to bytes (`v.tobytes()`, `bytes(v)`) | *O*(*n*) |
| Get length (`len(v)`) [^3] | *O*(1) |

[^1]: With *start* and *end* arguments, *n* is the length of the region searched rather than of *s*, and unlike slicing nothing is copied.
[^2]: These unpack and compare each element individually, so they are much slower than the equivalent [bytes](../../built-in-types/binary-sequence-types-bytes-bytearray-memoryview/bytes/README.md) methods.
[^3]: The number of elements is stored in the object, so `len()` does not need to count them.
