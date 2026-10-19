## `generator.close`

```
generator.close()
```

Raises a [GeneratorExit](https://docs.python.org/3.15/builtins/exceptions.html#GeneratorExit) exception at the point where the generator
function is currently suspended (equivalent to calling `throw(GeneratorExit)`).

If the generator function has already exited (due to an exception or
normal return), or raises [GeneratorExit](https://docs.python.org/3.15/builtins/exceptions.html#GeneratorExit) (by not catching the
exception), `close()` returns [None](https://docs.python.org/3.15/builtins/constants.html#None).
If the generator yields a value, a [RuntimeError](https://docs.python.org/3.15/builtins/exceptions.html#RuntimeError) is raised.
If the generator raises any other exception, it is propagated to the caller.
If a generator returns a value upon being closed, that value is returned
by `close()`.

When a generator iterator is garbage collected before it has exited,
close() is called automatically.

> *Changed in version 3.13:* If a generator returns a value upon being closed, the value is returned
> by `close()`.
> Previously, it returned `None`.
