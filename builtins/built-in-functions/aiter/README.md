## `aiter()`

```
aiter(async_iterable, /)
```

Return an [asynchronous iterator](https://docs.python.org/3.15/glossary.html#term-asynchronous-iterator) for an [asynchronous iterable](https://docs.python.org/3.15/glossary.html#term-asynchronous-iterable).
Equivalent to calling `x.__aiter__()`.

Note: Unlike [iter()](../iter/README.md), aiter() has no 2-argument variant.

> *Added in version 3.10.*
