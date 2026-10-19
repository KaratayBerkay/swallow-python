## `str.format`

```
str.format(*args, **kwargs)
```

Perform a string formatting operation.  The string on which this method is
called can contain literal text or replacement fields delimited by braces
`{}`.  Each replacement field contains either the numeric index of a
positional argument, or the name of a keyword argument.  Returns a copy of
the string where each replacement field is replaced with the string value of
the corresponding argument. For example:

``` python
>>> "The sum of 1 + 2 is {0}".format(1+2)
'The sum of 1 + 2 is 3'
>>> "The sum of {a} + {b} is {answer}".format(answer=1+2, a=1, b=2)
'The sum of 1 + 2 is 3'
>>> "{1} expects the {0} Inquisition!".format("Spanish", "Nobody")
'Nobody expects the Spanish Inquisition!'
```
> Code: [example_01.py](example_01.py)

See [Format string syntax](https://docs.python.org/3.15/library/string.html#formatstrings) for a description of the various formatting options
that can be specified in format strings.

> **Note**
>
> When formatting a number ([int](../../../built-in-functions/int/README.md), [float](../../../built-in-functions/float/README.md), [complex](../../../built-in-functions/complex/README.md),
> [decimal.Decimal](https://docs.python.org/3.15/library/decimal.html#decimal.Decimal) and subclasses) with the `n` type
> (ex: `'{:n}'.format(1234)`), the function temporarily sets the
> `LC_CTYPE` locale to the `LC_NUMERIC` locale to decode
> `decimal_point` and `thousands_sep` fields of `localeconv` if
> they are non-ASCII or longer than 1 byte, and the `LC_NUMERIC` locale is
> different than the `LC_CTYPE` locale.  This temporary change affects
> other threads.

> *Changed in version 3.7:* When formatting a number with the `n` type, the function sets
> temporarily the `LC_CTYPE` locale to the `LC_NUMERIC` locale in some
> cases.
