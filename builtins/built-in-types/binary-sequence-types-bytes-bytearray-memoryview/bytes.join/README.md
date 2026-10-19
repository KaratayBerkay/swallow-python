## `bytes.join`

```
bytes.join(iterable, /)
bytearray.join(iterable, /)
```

Return a bytes or bytearray object which is the concatenation of the
binary data sequences in *iterable*.  A [TypeError](https://docs.python.org/3.15/builtins/exceptions.html#TypeError) will be raised
if there are any values in *iterable* that are not `bytes-like
objects <bytes-like object>`, including [str](../../text-sequence-type-str/str/README.md) objects.  The
separator between elements is the contents of the bytes or
bytearray object providing this method.
