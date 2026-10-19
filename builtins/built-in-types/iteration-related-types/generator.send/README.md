## `generator.send`

```
generator.send(value)
```

"Sends" a value into the generator function: the *value* argument becomes
the result of the current yield expression.

Otherwise, this method behaves like [__next__()](../generator.__next__/README.md): it resumes
the underlying function and either returns the next yielded value or raises
[StopIteration](https://docs.python.org/3.15/builtins/exceptions.html#StopIteration).

When `send()` is called to start the generator, it must be called
with [None](https://docs.python.org/3.15/builtins/constants.html#None) as the argument, because there is no current yield
expression that could receive the value.
