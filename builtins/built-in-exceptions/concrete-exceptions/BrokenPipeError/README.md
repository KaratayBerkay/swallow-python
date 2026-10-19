## `BrokenPipeError`

```
BrokenPipeError
```

A subclass of [ConnectionError](../ConnectionError/README.md), raised when trying to write on a
pipe while the other end has been closed, or trying to write on a socket
which has been shutdown for writing.
Corresponds to `errno` [EPIPE](https://docs.python.org/3.15/library/errno.html#errno.EPIPE) and [ESHUTDOWN](https://docs.python.org/3.15/library/errno.html#errno.ESHUTDOWN).
