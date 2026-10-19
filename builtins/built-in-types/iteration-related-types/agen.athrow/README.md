## `agen.athrow`

```
agen.athrow(value)
agen.athrow(type[, value[, traceback]])
```

Returns an awaitable that, when run, raises an exception at the point where
the underlying asynchronous generator function is currently suspended.

Otherwise, this method behaves like [__anext__()](../agen.__anext__/README.md): when the
returned awaitable runs, it resumes the underlying function (with an
exception raised) and either returns the next yielded value as the value of
the raised [StopIteration](https://docs.python.org/3.15/builtins/exceptions.html#StopIteration), or raises [StopAsyncIteration](https://docs.python.org/3.15/builtins/exceptions.html#StopAsyncIteration).
If the underlying function does not catch the passed-in exception, or
raises a different exception, then when the awaitable is run, that
exception propagates to the caller of the awaitable.

When athrow() is called to start the generator, the generator
exits when the awaitable runs (that is, subsequent results from
[__anext__()](../agen.__anext__/README.md) will raise [StopAsyncIteration](https://docs.python.org/3.15/builtins/exceptions.html#StopAsyncIteration) when run)
and the thrown exception is propagated to the awaitable's caller.

In typical use, this is called with a single argument, an exception instance,
similar to the way the `raise` keyword is used.

For backwards compatibility, however, the second signature is
supported.
An exception instance is created from three arguments in the same way as in
[generator.throw()](../generator.throw/README.md).

> *Changed in version 3.12:* The second signature (type[, value[, traceback]]) is deprecated and
> may be removed in a future version of Python.
