## `AttributeError`

```
AttributeError
```

Raised when an attribute reference (see [Attribute references](https://docs.python.org/3.15/reference/expressions.html#attribute-references)) or
assignment fails.  (When an object does not support attribute references or
attribute assignments at all, [TypeError](../TypeError/README.md) is raised.)

The optional *name* and *obj* keyword-only arguments
set the corresponding attributes:

### name

The name of the attribute that was attempted to be accessed.

### obj

The object that was accessed for the named attribute.

> *Changed in version 3.10:* Added the `name` and `obj` attributes.
