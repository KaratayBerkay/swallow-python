## `bytes.swapcase`

```
bytes.swapcase()
bytearray.swapcase()
```

Return a copy of the sequence with all the lowercase ASCII characters
converted to their corresponding uppercase counterpart and vice-versa.

For example:

``` python
>>> b'Hello World'.swapcase()
b'hELLO wORLD'
```
> Code: [example_01.py](example_01.py)

Lowercase ASCII characters are those byte values in the sequence
`b'abcdefghijklmnopqrstuvwxyz'`. Uppercase ASCII characters
are those byte values in the sequence `b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`.

Unlike [str.swapcase()](../../text-sequence-type-str/str.swapcase/README.md), it is always the case that
`bin.swapcase().swapcase() == bin` for the binary versions. Case
conversions are symmetrical in ASCII, even though that is not generally
true for arbitrary Unicode code points.

> **Note**
>
> The bytearray version of this method does *not* operate in place - it
> always produces a new object, even if no changes were made.
