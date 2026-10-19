## `NotImplemented`

```
NotImplemented
```

A special value which should be returned by the binary special methods
(e.g. [__eq__()](https://docs.python.org/3.15/reference/datamodel.html#object.__eq__), [__lt__()](https://docs.python.org/3.15/reference/datamodel.html#object.__lt__), [__add__()](https://docs.python.org/3.15/reference/datamodel.html#object.__add__), [__rsub__()](https://docs.python.org/3.15/reference/datamodel.html#object.__rsub__),
etc.) to indicate that the operation is not implemented with respect to
the other type; may be returned by the in-place binary special methods
(e.g. [__imul__()](https://docs.python.org/3.15/reference/datamodel.html#object.__imul__), [__iand__()](https://docs.python.org/3.15/reference/datamodel.html#object.__iand__), etc.) for the same purpose.
It should not be evaluated in a boolean context.
NotImplemented is the sole instance of the [types.NotImplementedType](https://docs.python.org/3.15/library/types.html#types.NotImplementedType) type.

> **Note**
>
> When a binary (or in-place) method returns NotImplemented the
> interpreter will try the reflected operation on the other type (or some
> other fallback, depending on the operator).  If all attempts return
> NotImplemented, the interpreter will raise an appropriate exception.
> Incorrectly returning NotImplemented will result in a misleading
> error message or the NotImplemented value being returned to Python code.
>
> See [Implementing the arithmetic operations](https://docs.python.org/3.15/library/numbers.html#implementing-the-arithmetic-operations) for examples.

> **Caution**
>
> NotImplemented and [NotImplementedError](https://docs.python.org/3.15/builtins/exceptions.html#NotImplementedError) are not
> interchangeable. This constant should only be used as described
> above; see [NotImplementedError](https://docs.python.org/3.15/builtins/exceptions.html#NotImplementedError) for details on correct usage
> of the exception.

> *Changed in version 3.9:* Evaluating NotImplemented in a boolean context was deprecated.

> *Changed in version 3.14:* Evaluating NotImplemented in a boolean context now raises a [TypeError](https://docs.python.org/3.15/builtins/exceptions.html#TypeError).
> It previously evaluated to [True](../True/README.md) and emitted a [DeprecationWarning](https://docs.python.org/3.15/builtins/exceptions.html#DeprecationWarning)
> since Python 3.9.
