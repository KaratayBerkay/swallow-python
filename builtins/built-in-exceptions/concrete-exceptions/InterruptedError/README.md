## `InterruptedError`

```
InterruptedError
```

Raised when a system call is interrupted by an incoming signal.
Corresponds to `errno` [EINTR](https://docs.python.org/3.15/library/errno.html#errno.EINTR).

> *Changed in version 3.5:* Python now retries system calls when a syscall is interrupted by a
> signal, except if the signal handler raises an exception (see [PEP 475](https://peps.python.org/pep-475/)
> for the rationale), instead of raising InterruptedError.
