## `agen.aclose`

```
agen.aclose()
```

Returns an awaitable that when run will throw a [GeneratorExit](https://docs.python.org/3.15/builtins/exceptions.html#GeneratorExit) into
the underlying asynchronous generator function at the point where it is
currently suspended (equivalent to calling `athrow(GeneratorExit)`).

If the asynchronous generator function then exits gracefully, is already
closed, or raises [GeneratorExit](https://docs.python.org/3.15/builtins/exceptions.html#GeneratorExit) (by not catching the exception),
then the returned awaitable will raise a [StopIteration](https://docs.python.org/3.15/builtins/exceptions.html#StopIteration) exception.
Any further awaitables returned by subsequent calls to the asynchronous
generator will raise a [StopAsyncIteration](https://docs.python.org/3.15/builtins/exceptions.html#StopAsyncIteration) exception.

If the asynchronous generator yields a value, a [RuntimeError](https://docs.python.org/3.15/builtins/exceptions.html#RuntimeError) is
raised by the awaitable.
If the asynchronous generator raises any other exception, that exception
is propagated to the caller of the awaitable.

If the asynchronous generator has already exited due to an exception or
normal exit, then further calls to `aclose()` will return an awaitable
that does nothing.
