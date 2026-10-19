## `anext()`

```
anext(async_iterator, /)
anext(async_iterator, default, /)
```

When awaited, return the next item from the given `asynchronous
iterator`, or *default* if given and the iterator is [exhausted](https://docs.python.org/3.15/glossary.html#term-exhausted).

This is the async variant of the [next()](../next/README.md) builtin, and behaves
similarly.

This calls the [__anext__()](https://docs.python.org/3.15/reference/datamodel.html#object.__anext__) method of *async_iterator*,
returning an [awaitable](https://docs.python.org/3.15/glossary.html#term-awaitable). Awaiting this returns the next value of the
iterator. If *default* is given, it is returned if the iterator is exhausted,
otherwise [StopAsyncIteration](https://docs.python.org/3.15/builtins/exceptions.html#StopAsyncIteration) is raised.

> *Added in version 3.10.*
