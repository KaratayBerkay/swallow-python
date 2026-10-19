## `ImportError`

```
ImportError
```

Raised when the `import` statement has troubles trying to
load a module.  Also raised when the "from list" in `from ... import`
has a name that cannot be found.

The optional *name* and *path* keyword-only arguments
set the corresponding attributes:

### name

The name of the module that was attempted to be imported.

### path

The path to any file which triggered the exception.

> *Changed in version 3.3:* Added the `name` and `path` attributes.
