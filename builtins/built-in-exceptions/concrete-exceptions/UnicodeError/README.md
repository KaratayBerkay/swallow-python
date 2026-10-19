## `UnicodeError`

```
UnicodeError
```

Raised when a Unicode-related encoding or decoding error occurs.  It is a
subclass of [ValueError](../ValueError/README.md).

UnicodeError has attributes that describe the encoding or decoding
error.  For example, `err.object[err.start:err.end]` gives the particular
invalid input that the codec failed on.

### encoding

The name of the encoding that raised the error.

### reason

A string describing the specific codec error.

### object

The object the codec was attempting to encode or decode.

### start

The first index of invalid data in [object](../../../built-in-functions/object/README.md).

This value should not be negative as it is interpreted as an
absolute offset but this constraint is not enforced at runtime.

### end

The index after the last invalid data in [object](../../../built-in-functions/object/README.md).

This value should not be negative as it is interpreted as an
absolute offset but this constraint is not enforced at runtime.
