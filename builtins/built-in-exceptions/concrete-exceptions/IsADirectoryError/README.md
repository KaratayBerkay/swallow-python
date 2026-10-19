## `IsADirectoryError`

```
IsADirectoryError
```

Raised when a file operation (such as [os.remove()](https://docs.python.org/3.15/library/os.html#os.remove)) is requested
on a directory.
Corresponds to `errno` [EISDIR](https://docs.python.org/3.15/library/errno.html#errno.EISDIR).
