## `PythonFinalizationError`

```
PythonFinalizationError
```

This exception is derived from [RuntimeError](../RuntimeError/README.md).  It is raised when
an operation is blocked during interpreter shutdown also known as
[Python finalization](https://docs.python.org/3.15/glossary.html#term-interpreter-shutdown).

Examples of operations which can be blocked with a
PythonFinalizationError during the Python finalization:

- Creating a new Python thread.

- [Joining](https://docs.python.org/3.15/library/threading.html#threading.Thread.join) a running daemon thread.

- [os.fork()](https://docs.python.org/3.15/library/os.html#os.fork),

- acquiring a lock such as [threading.Lock](https://docs.python.org/3.15/library/threading.html#threading.Lock), when it is known that
  the operation would otherwise deadlock.

See also the [sys.is_finalizing()](https://docs.python.org/3.15/library/sys.html#sys.is_finalizing) function.

> *Added in version 3.13:* Previously, a plain [RuntimeError](../RuntimeError/README.md) was raised.

> *Changed in version 3.14:* [threading.Thread.join()](https://docs.python.org/3.15/library/threading.html#threading.Thread.join) can now raise this exception.

> *Changed in version 3.15:* This exception may be raised when acquiring `threading.Lock()`
> or `threading.RLock()`.
