## `chr()`

```
chr(codepoint, /)
```

Return the string representing a character with the specified Unicode code point.
For example, `chr(97)` returns the string `'a'`, while
`chr(8364)` returns the string `'€'`. This is the inverse of [ord()](../ord/README.md).

The valid range for the argument is from 0 through 1,114,111 (0x10FFFF in
base 16).  [ValueError](https://docs.python.org/3.15/builtins/exceptions.html#ValueError) will be raised if it is outside that range.
