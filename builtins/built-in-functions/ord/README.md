## `ord()`

```
ord(character, /)
```

Return the ordinal value of a character.

If the argument is a one-character string, return the Unicode code point
of that character.  For example,
`ord('a')` returns the integer `97` and `ord('€')` (Euro sign)
returns `8364`.  This is the inverse of [chr()](../chr/README.md).

If the argument is a [bytes](../bytes/README.md) or [bytearray](../bytearray/README.md) object of
length 1, return its single byte value.
For example, `ord(b'a')` returns the integer `97`.
