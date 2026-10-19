## `BlockingIOError`

```
BlockingIOError
```

Raised when an operation would block on an object (e.g. socket) set
for non-blocking operation.
Corresponds to `errno` [EAGAIN](https://docs.python.org/3.15/library/errno.html#errno.EAGAIN), [EALREADY](https://docs.python.org/3.15/library/errno.html#errno.EALREADY),
[EWOULDBLOCK](https://docs.python.org/3.15/library/errno.html#errno.EWOULDBLOCK) and [EINPROGRESS](https://docs.python.org/3.15/library/errno.html#errno.EINPROGRESS).

In addition to those of [OSError](../OSError/README.md), BlockingIOError can have
one more attribute:

### characters_written

An integer containing the number of **bytes** written to the stream
before it blocked. This attribute is available when using the
buffered I/O classes from the [io](https://docs.python.org/3.15/library/io.html#module-io) module.
