## `ascii()`

```
ascii(object, /)
```

As [repr()](../repr/README.md), return a string containing a printable representation of an
object, but escape the non-ASCII characters in the string returned by
[repr()](../repr/README.md) using `\x`, `\u`, or `\U` escapes.  This generates a string
similar to that returned by [repr()](../repr/README.md) in Python 2.
