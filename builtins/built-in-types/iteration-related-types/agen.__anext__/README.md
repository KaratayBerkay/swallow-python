## `agen.__anext__`

```
agen.__anext__()
```

Returns an [awaitable](https://docs.python.org/3.15/glossary.html#term-awaitable) which when run starts to execute the
asynchronous generator function or resumes it at the
[yield expression](https://docs.python.org/3.15/reference/expressions.html#yieldexpr) where the function is currently suspended.
When an asynchronous generator function is resumed with an
__anext__() method, the current yield expression always
evaluates to [None](https://docs.python.org/3.15/builtins/constants.html#None) in the returned awaitable, which when run will
continue to the next yield expression.
The value of the expression after the `yield` keyword is the value
of the [StopIteration](https://docs.python.org/3.15/builtins/exceptions.html#StopIteration) exception raised by the completing coroutine.
If the asynchronous generator exits without yielding another value, the
awaitable instead raises a [StopAsyncIteration](https://docs.python.org/3.15/builtins/exceptions.html#StopAsyncIteration) exception,
signalling that the asynchronous iteration has completed.

This method is normally called implicitly by an `async for` loop,
or by the built-in [anext()](../../../built-in-functions/anext/README.md) function.
