Booleans represent truth values. The [bool](../../built-in-functions/bool/README.md) type has exactly two
constant instances: `True` and `False`.

The built-in function [bool()](../../built-in-functions/bool/README.md)  converts any value to a boolean, if the
value can be interpreted as a truth value (see section [Truth Value Testing](https://docs.python.org/3.15/builtins/stdtypes.html#truth) above).

For logical operations, use the [boolean operators](https://docs.python.org/3.15/builtins/stdtypes.html#boolean) `and`,
`or` and `not`.
When applying the bitwise operators `&`, `|`, `^` to two booleans, they
return a bool equivalent to the logical operations "and", "or", "xor". However,
the logical operators `and`, `or` and `!=` should be preferred
over `&`, `|` and `^`.

> *Deprecated since version 3.12:* The use of the bitwise inversion operator `~` is deprecated and will
> raise an error in Python 3.16.

[bool](../../built-in-functions/bool/README.md) is a subclass of [int](../../built-in-functions/int/README.md) (see [Numeric Types — int, float, complex](https://docs.python.org/3.15/builtins/stdtypes.html#typesnumeric)). In
many numeric contexts, `False` and `True` behave like the integers 0 and 1, respectively.
However, relying on this is discouraged; explicitly convert using [int()](../../built-in-functions/int/README.md)
instead.
