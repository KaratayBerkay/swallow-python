## `agen.asend`

```
agen.asend(value)
```

Returns an awaitable which, when run, "sends" a value into the underlying
asynchronous generator function: the *value* argument becomes
the result of the current yield expression.

Otherwise, this method behaves like [__anext__()](../agen.__anext__/README.md): when the
returned awaitable runs, it resumes the underlying function and either
returns the next yielded value as the value of the raised
[StopIteration](https://docs.python.org/3.15/builtins/exceptions.html#StopIteration), or raises [StopAsyncIteration](https://docs.python.org/3.15/builtins/exceptions.html#StopAsyncIteration).

When `asend()` is called to start the asynchronous
generator, it must be called with [None](https://docs.python.org/3.15/builtins/constants.html#None) as the argument,
because there is no yield expression that could receive the value.
