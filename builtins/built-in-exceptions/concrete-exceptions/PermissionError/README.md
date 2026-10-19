## `PermissionError`

```
PermissionError
```

Raised when trying to run an operation without the adequate access
rights - for example filesystem permissions.
Corresponds to `errno` [EACCES](https://docs.python.org/3.15/library/errno.html#errno.EACCES),
[EPERM](https://docs.python.org/3.15/library/errno.html#errno.EPERM), and [ENOTCAPABLE](https://docs.python.org/3.15/library/errno.html#errno.ENOTCAPABLE).

> *Changed in version 3.11.1:* WASI's [ENOTCAPABLE](https://docs.python.org/3.15/library/errno.html#errno.ENOTCAPABLE) is now mapped to
> PermissionError.
