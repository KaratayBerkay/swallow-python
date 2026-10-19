## `genericalias.__parameters__`

```
genericalias.__parameters__
```

This attribute is a lazily computed tuple (possibly empty) of unique type
variables found in `__args__`:

``` python
>>> from typing import TypeVar

>>> T = TypeVar('T')
>>> list[T].__parameters__
(~T,)
```
> Code: [example_01.py](example_01.py)

> **Note**
>
> A `GenericAlias` object with [typing.ParamSpec](https://docs.python.org/3.15/library/typing.html#typing.ParamSpec) parameters may not
> have correct `__parameters__` after substitution because
> [typing.ParamSpec](https://docs.python.org/3.15/library/typing.html#typing.ParamSpec) is intended primarily for static type checking.
