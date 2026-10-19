## `bytes()`

```
bytes(source=b'')
bytes(source, encoding, errors='strict')
```

Return a new "bytes" object which is an immutable sequence of integers in
the range `0 <= x < 256`.  bytes is an immutable version of
[bytearray](../bytearray/README.md) -- it has the same non-mutating methods and the same
indexing and slicing behavior.

Accordingly, constructor arguments are interpreted as for `bytearray()`.

Bytes objects can also be created with literals, see [String and Bytes literals](https://docs.python.org/3.15/reference/lexical_analysis.html#strings).

See also [Binary Sequence Types — bytes, bytearray, memoryview](https://docs.python.org/3.15/builtins/stdtypes.html#binaryseq), [Bytes Objects](https://docs.python.org/3.15/builtins/stdtypes.html#typebytes), and [Bytes and Bytearray Operations](https://docs.python.org/3.15/builtins/stdtypes.html#bytes-methods).
