## `NotImplementedError`

```
NotImplementedError
```

This exception is derived from [RuntimeError](../RuntimeError/README.md).  In user defined base
classes, abstract methods should raise this exception when they require
derived classes to override the method, or while the class is being
developed to indicate that the real implementation still needs to be added.

> **Note**
>
> It should not be used to indicate that an operator or method is not
> meant to be supported at all -- in that case either leave the operator /
> method undefined or, if a subclass, set it to [None](https://docs.python.org/3.15/builtins/constants.html#None).

> **Caution**
>
> NotImplementedError and [NotImplemented](https://docs.python.org/3.15/builtins/constants.html#NotImplemented) are not
> interchangeable. This exception should only be used as described
> above; see [NotImplemented](https://docs.python.org/3.15/builtins/constants.html#NotImplemented) for details on correct usage of
> the built-in constant.
