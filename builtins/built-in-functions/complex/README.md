## `complex()`

```
complex(number=0, /)
complex(string, /)
complex(real=0, imag=0)
```

Convert a single string or number to a complex number, or create a
complex number from real and imaginary parts.

Examples:

``` python
>>> complex('+1.23')
(1.23+0j)
>>> complex('-4.5j')
-4.5j
>>> complex('-1.23+4.5j')
(-1.23+4.5j)
>>> complex('\t( -1.23+4.5J )\n')
(-1.23+4.5j)
>>> complex('-Infinity+NaNj')
(-inf+nanj)
>>> complex(1.23)
(1.23+0j)
>>> complex(imag=-4.5)
-4.5j
>>> complex(-1.23, 4.5)
(-1.23+4.5j)
```
> Code: [example_01.py](example_01.py)

If the argument is a string, it must contain either a real part (in the
same format as for `float()`) or an imaginary part (in the same
format but with a `'j'` or `'J'` suffix), or both real and imaginary
parts (the sign of the imaginary part is mandatory in this case).
The string can optionally be surrounded by whitespaces and the round
parentheses `'('` and `')'`, which are ignored.
The string must not contain whitespace between `'+'`, `'-'`, the
`'j'` or `'J'` suffix, and the decimal number.
For example, `complex('1+2j')` is fine, but `complex('1 + 2j')` raises
[ValueError](https://docs.python.org/3.15/builtins/exceptions.html#ValueError).
More precisely, the input must conform to the [complexvalue](https://docs.python.org/3.15/builtins/functions.html#grammar-token-float-complexvalue)
production rule in the following grammar, after parentheses and leading and
trailing whitespace characters are removed:

```
complexvalue: `floatvalue` |
            : `floatvalue` ("j" | "J") |
            : `floatvalue` `sign` `absfloatvalue` ("j" | "J")
```

If the argument is a number, the constructor serves as a numeric
conversion like [int](../int/README.md) and [float](../float/README.md).
For a general Python object `x`, `complex(x)` delegates to
`x.__complex__()`.
If [__complex__()](https://docs.python.org/3.15/reference/datamodel.html#object.__complex__) is not defined then it falls back
to [__float__()](https://docs.python.org/3.15/reference/datamodel.html#object.__float__).
If `__float__()` is not defined then it falls back
to [__index__()](https://docs.python.org/3.15/reference/datamodel.html#object.__index__).

If two arguments are provided or keyword arguments are used, each argument
may be any numeric type (including complex).
If both arguments are real numbers, return a complex number with the real
component *real* and the imaginary component *imag*.
If both arguments are complex numbers, return a complex number with the real
component `real.real-imag.imag` and the imaginary component
`real.imag+imag.real`.
If one of arguments is a real number, only its real component is used in
the above expressions.

See also [complex.from_number()](https://docs.python.org/3.15/builtins/stdtypes.html#complex.from_number) which only accepts a single numeric argument.

If all arguments are omitted, returns `0j`.

The complex type is described in [Numeric Types — int, float, complex](https://docs.python.org/3.15/builtins/stdtypes.html#typesnumeric).

> *Changed in version 3.6:* Grouping digits with underscores as in code literals is allowed.

> *Changed in version 3.8:* Falls back to [__index__()](https://docs.python.org/3.15/reference/datamodel.html#object.__index__) if [__complex__()](https://docs.python.org/3.15/reference/datamodel.html#object.__complex__) and
> [__float__()](https://docs.python.org/3.15/reference/datamodel.html#object.__float__) are not defined.

> *Deprecated since version 3.14:* Passing a complex number as the *real* or *imag* argument is now
> deprecated; it should only be passed as a single positional argument.
