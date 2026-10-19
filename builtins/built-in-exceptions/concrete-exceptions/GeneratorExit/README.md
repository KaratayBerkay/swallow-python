## `GeneratorExit`

```
GeneratorExit
```

Raised when a [generator](https://docs.python.org/3.15/glossary.html#term-generator) or [coroutine](https://docs.python.org/3.15/glossary.html#term-coroutine) is closed;
see [generator.close()](https://docs.python.org/3.15/builtins/stdtypes.html#generator.close) and [coroutine.close()](https://docs.python.org/3.15/reference/datamodel.html#coroutine.close).  It
directly inherits from [BaseException](../../base-classes/BaseException/README.md) instead of [Exception](../../base-classes/Exception/README.md) since
it is technically not an error.
