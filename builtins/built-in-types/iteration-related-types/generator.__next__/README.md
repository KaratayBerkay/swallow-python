## `generator.__next__`

```
generator.__next__()
```

Starts the execution of a generator function or resumes it at the
[yield expression](https://docs.python.org/3.15/reference/expressions.html#yieldexpr) where the function is currently suspended.
When a generator function is resumed with a __next__()
method, the current yield expression always evaluates to [None](https://docs.python.org/3.15/builtins/constants.html#None).
The execution then continues to the next yield expression, where the
generator is suspended again, and the value of the expression after the
`yield` keyword is returned to __next__()'s
caller.
If the generator exits without yielding another value,
__next__() raises a [StopIteration](https://docs.python.org/3.15/builtins/exceptions.html#StopIteration) exception,
signalling that iteration has completed.

This method is normally called implicitly, for example by a `for`
loop, or by the built-in [next()](../../../built-in-functions/next/README.md) function.
