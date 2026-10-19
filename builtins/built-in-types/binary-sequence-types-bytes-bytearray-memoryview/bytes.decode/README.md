## `bytes.decode`

```
bytes.decode(encoding="utf-8", errors="strict")
bytearray.decode(encoding="utf-8", errors="strict")
```

Return the bytes decoded to a [str](../../text-sequence-type-str/str/README.md).

*encoding* defaults to `'utf-8'`;
see [Standard Encodings](https://docs.python.org/3.15/library/codecs.html#standard-encodings) for possible values.

*errors* controls how decoding errors are handled.
If `'strict'` (the default), a [UnicodeError](https://docs.python.org/3.15/builtins/exceptions.html#UnicodeError) exception is raised.
Other possible values are `'ignore'`, `'replace'`,
and any other name registered via [codecs.register_error()](https://docs.python.org/3.15/library/codecs.html#codecs.register_error).
See [Error Handlers](https://docs.python.org/3.15/library/codecs.html#error-handlers) for details.

For performance reasons, the value of *errors* is not checked for validity
unless a decoding error actually occurs,
[Python Development Mode](https://docs.python.org/3.15/library/devmode.html#devmode) is enabled or a [debug build](https://docs.python.org/3.15/using/configure.html#debug-build) is used.

> **Note**
>
> Passing the *encoding* argument to [str](../../text-sequence-type-str/str/README.md) allows decoding any
> [bytes-like object](https://docs.python.org/3.15/glossary.html#term-bytes-like-object) directly, without needing to make a temporary
> [bytes](../bytes/README.md) or [bytearray](../bytearray/README.md) object.

> *Changed in version 3.1:* Added support for keyword arguments.

> *Changed in version 3.9:* The value of the *errors* argument is now checked in [Python Development Mode](https://docs.python.org/3.15/library/devmode.html#devmode) and
> in [debug mode](https://docs.python.org/3.15/using/configure.html#debug-build).
