## `pow()`

```
pow(base, exp, mod=None)
```

Return *base* to the power *exp*; if *mod* is present, return *base* to the
power *exp*, modulo *mod* (computed more efficiently than
`pow(base, exp) % mod`). The two-argument form `pow(base, exp)` is
equivalent to using the power operator: `base**exp`.

When arguments are builtin numeric types with mixed operand types, the
coercion rules for binary arithmetic operators apply.  For [int](../int/README.md)
operands, the result has the same type as the operands (after coercion)
unless the second argument is negative; in that case, all arguments are
converted to float and a float result is delivered.  For example, `pow(10, 2)`
returns `100`, but `pow(10, -2)` returns `0.01`.  For a negative base of
type [int](../int/README.md) or [float](../float/README.md) and a non-integral exponent, a complex
result is delivered.  For example, `pow(-9, 0.5)` returns a value close
to `3j`. Whereas, for a negative base of type [int](../int/README.md) or [float](../float/README.md)
with an integral exponent, a float result is delivered. For example,
`pow(-9, 2.0)` returns `81.0`.

For [int](../int/README.md) operands *base* and *exp*, if *mod* is present, *mod* must
also be of integer type and *mod* must be nonzero. If *mod* is present and
*exp* is negative, *base* must be relatively prime to *mod*. In that case,
`pow(inv_base, -exp, mod)` is returned, where *inv_base* is an inverse to
*base* modulo *mod*.

Here's an example of computing an inverse for `38` modulo `97`:

``` python
>>> pow(38, -1, mod=97)
23
>>> 23 * 38 % 97 == 1
True
```
> Code: [example_01.py](example_01.py)

> *Changed in version 3.8:* For [int](../int/README.md) operands, the three-argument form of `pow` now allows
> the second argument to be negative, permitting computation of modular
> inverses.

> *Changed in version 3.8:* Allow keyword arguments.  Formerly, only positional arguments were
> supported.
