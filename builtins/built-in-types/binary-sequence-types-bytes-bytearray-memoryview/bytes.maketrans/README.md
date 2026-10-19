## `bytes.maketrans`

```
bytes.maketrans(from, to, /)
bytearray.maketrans(from, to, /)
```

This static method returns a translation table usable for
[bytes.translate()](../bytes.translate/README.md) that will map each character in *from* into the
character at the same position in *to*; *from* and *to* must both be
[bytes-like objects](https://docs.python.org/3.15/glossary.html#term-bytes-like-object) and have the same length.

> *Added in version 3.1.*
