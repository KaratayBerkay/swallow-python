## `bytearray()`

```
bytearray(source=b'')
bytearray(source, encoding, errors='strict')
```

Return a new array of bytes.  The bytearray class is a mutable
sequence of integers in the range 0 <= x < 256.  It has most of the usual
methods of mutable sequences, described in [Mutable Sequence Types](https://docs.python.org/3.15/builtins/stdtypes.html#typesseq-mutable), as well
as most methods that the [bytes](../bytes/README.md) type has, see [Bytes and Bytearray Operations](https://docs.python.org/3.15/builtins/stdtypes.html#bytes-methods).

The optional *source* parameter can be used to initialize the array in a few
different ways:

- If it is a *string*, you must also give the *encoding* (and optionally,
  *errors*) parameters; `bytearray()` then converts the string to
  bytes using [str.encode()](https://docs.python.org/3.15/builtins/stdtypes.html#str.encode).

- If it is an *integer*, the array will have that size and will be
  initialized with null bytes.

- If it is an object conforming to the [buffer interface](https://docs.python.org/3.15/c-api/buffer.html#bufferobjects),
  a read-only buffer of the object will be used to initialize the bytes array.

- If it is an *iterable*, it must be an iterable of integers in the range
  `0 <= x < 256`, which are used as the initial contents of the array.

Without an argument, an array of size 0 is created.

See also [Binary Sequence Types — bytes, bytearray, memoryview](https://docs.python.org/3.15/builtins/stdtypes.html#binaryseq) and [Bytearray Objects](https://docs.python.org/3.15/builtins/stdtypes.html#typebytearray).
