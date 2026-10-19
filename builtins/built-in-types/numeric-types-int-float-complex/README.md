There are three distinct numeric types: integers, floating-point
numbers, and complex numbers.  In addition, Booleans are a
subtype of integers.  Integers have unlimited precision.  Floating-point
numbers are usually implemented using `double` in C; information
about the precision and internal representation of floating-point
numbers for the machine on which your program is running is available
in [sys.float_info](https://docs.python.org/3.15/library/sys.html#sys.float_info).  Complex numbers have a real and imaginary
part, which are each a floating-point number.  To extract these parts
from a complex number *z*, use `z.real` and `z.imag`. (The standard
library includes the additional numeric types `fractions.Fraction`, for
rationals, and `decimal.Decimal`, for floating-point numbers with
user-definable precision.)

Numbers are created by numeric literals or as the result of built-in functions
and operators.  Unadorned integer literals (including hex, octal and binary
numbers) yield integers.  Numeric literals containing a decimal point or an
exponent sign yield floating-point numbers.  Appending `'j'` or `'J'` to a
numeric literal yields an imaginary number (a complex number with a zero real
part) which you can add to an integer or float to get a complex number with real
and imaginary parts.

The constructors [int()](../../built-in-functions/int/README.md), [float()](../../built-in-functions/float/README.md), and
[complex()](../../built-in-functions/complex/README.md) can be used to produce numbers of a specific type.

Python fully supports mixed arithmetic: when a binary arithmetic operator has
operands of different built-in numeric types, the operand with the "narrower"
type is widened to that of the other:

- If both arguments are complex numbers, no conversion is performed;

- if either argument is a complex or a floating-point number, the other is
  converted to a floating-point number;

- otherwise, both must be integers and no conversion is necessary.

Arithmetic with complex and real operands is defined by the usual mathematical
formula, for example:

```
x + complex(u, v) = complex(x + u, v)
x * complex(u, v) = complex(x * u, x * v)
```

A comparison between numbers of different types behaves as though the exact
values of those numbers were being compared. [^1]

All numeric types (except complex) support the following operations (for priorities of
the operations, see [Operator precedence](https://docs.python.org/3.15/reference/expressions.html#operator-summary)):

| Operation | Result | Notes | Full documentation |
| --- | --- | --- | --- |
| `x + y` | sum of *x* and *y* |  |  |
| `x - y` | difference of *x* and *y* |  |  |
| `x * y` | product of *x* and *y* |  |  |
| `x / y` | quotient of *x* and *y* |  |  |
| `x // y` | floored quotient of *x* and *y* | (1)(2) |  |
| `x % y` | remainder of `x / y` | (2) |  |
| `-x` | *x* negated |  |  |
| `+x` | *x* unchanged |  |  |
| `abs(x)` | absolute value or magnitude of *x* |  | [abs()](../../built-in-functions/abs/README.md) |
| `int(x)` | *x* converted to integer | (3)(6) | [int()](../../built-in-functions/int/README.md) |
| `float(x)` | *x* converted to floating point | (4)(6) | [float()](../../built-in-functions/float/README.md) |
| `complex(re, im)` | a complex number with real part *re*, imaginary part *im*. *im* defaults to zero. | (6) | [complex()](../../built-in-functions/complex/README.md) |
| `c.conjugate()` | conjugate of the complex number *c* |  |  |
| `divmod(x, y)` | the pair `(x // y, x % y)` | (2) | [divmod()](../../built-in-functions/divmod/README.md) |
| `pow(x, y)` | *x* to the power *y* | (5) | [pow()](../../built-in-functions/pow/README.md) |
| `x ** y` | *x* to the power *y* | (5) |  |

Notes:

1. Also referred to as integer division.  For operands of type [int](../../built-in-functions/int/README.md),
   the result has type [int](../../built-in-functions/int/README.md).  For operands of type [float](../../built-in-functions/float/README.md),
   the result has type [float](../../built-in-functions/float/README.md).  In general, the result is a whole
   integer, though the result's type is not necessarily [int](../../built-in-functions/int/README.md).  The result is
   always rounded towards minus infinity: `1//2` is `0`, `(-1)//2` is
   `-1`, `1//(-2)` is `-1`, and `(-1)//(-2)` is `0`.

2. Not for complex numbers.  Instead convert to floats using [abs()](../../built-in-functions/abs/README.md) if
   appropriate.

3. Conversion from [float](../../built-in-functions/float/README.md) to [int](../../built-in-functions/int/README.md) truncates, discarding the
   fractional part. See functions [math.floor()](https://docs.python.org/3.15/library/math.html#math.floor) and [math.ceil()](https://docs.python.org/3.15/library/math.html#math.ceil) for
   alternative conversions.

4. float also accepts the strings "nan" and "inf" with an optional prefix "+"
   or "-" for Not a Number (NaN) and positive or negative infinity.

5. Python defines `pow(0, 0)` and `0 ** 0` to be `1`, as is common for
   programming languages.

6. The numeric literals accepted include the digits `0` to `9` or any
   Unicode equivalent (code points with the `Nd` property).

   See [the Unicode Standard](https://unicode.org/Public/UNIDATA/extracted/DerivedNumericType.txt)
   for a complete list of code points with the `Nd` property.

All [numbers.Real](https://docs.python.org/3.15/library/numbers.html#numbers.Real) types ([int](../../built-in-functions/int/README.md) and [float](../../built-in-functions/float/README.md)) also include
the following operations:

| Operation | Result |
| --- | --- |
| `math.trunc(x) <math.trunc>()` | *x* truncated to [Integral](https://docs.python.org/3.15/library/numbers.html#numbers.Integral) |
| `round(x[, n]) <round>()` | *x* rounded to *n* digits, rounding half to even. If *n* is omitted, it defaults to 0. |
| `math.floor(x) <math.floor>()` | the greatest [Integral](https://docs.python.org/3.15/library/numbers.html#numbers.Integral) <= *x* |
| [math.ceil(x)](https://docs.python.org/3.15/library/math.html#math.ceil) | the least [Integral](https://docs.python.org/3.15/library/numbers.html#numbers.Integral) >= *x* |

For additional numeric operations see the [math](https://docs.python.org/3.15/library/math.html#module-math) and [cmath](https://docs.python.org/3.15/library/cmath.html#module-cmath)
modules.

## Bitwise Operations on Integer Types

Bitwise operations only make sense for integers. The result of bitwise
operations is calculated as though carried out in two's complement with an
infinite number of sign bits.

The priorities of the binary bitwise operations are all lower than the numeric
operations and higher than the comparisons; the unary operation `~` has the
same priority as the other unary numeric operations (`+` and `-`).

This table lists the bitwise operations sorted in ascending priority:

| Operation | Result | Notes |
| --- | --- | --- |
| `x \| y` | bitwise or of *x* and *y* | (4) |
| `x ^ y` | bitwise exclusive or of *x* and *y* | (4) |
| `x & y` | bitwise and of *x* and *y* | (4) |
| `x << n` | *x* shifted left by *n* bits | (1)(2) |
| `x >> n` | *x* shifted right by *n* bits | (1)(3) |
| `~x` | the bits of *x* inverted |  |

Notes:

1. Negative shift counts are illegal and cause a [ValueError](https://docs.python.org/3.15/builtins/exceptions.html#ValueError) to be raised.

2. A left shift by *n* bits is equivalent to multiplication by `pow(2, n)`.

3. A right shift by *n* bits is equivalent to floor division by `pow(2, n)`.

4. Performing these calculations with at least one extra sign extension bit in
   a finite two's complement representation (a working bit-width of
   `1 + max(x.bit_length(), y.bit_length())` or more) is sufficient to get the
   same result as if there were an infinite number of sign bits.

## Additional Methods on Integer Types

The int type implements the [numbers.Integral](https://docs.python.org/3.15/library/numbers.html#numbers.Integral) `abstract base
class`. In addition, it provides a few more methods:

- [`int.bit_length`](int.bit_length/README.md) — Return the number of bits necessary to represent an integer in binary, excluding the sign and leading zeros:
- [`int.bit_count`](int.bit_count/README.md) — Return the number of ones in the binary representation of the absolute value of the integer.
- [`int.to_bytes`](int.to_bytes/README.md) — Return an array of bytes representing an integer.
- [`int.from_bytes`](int.from_bytes/README.md) — Return the integer represented by the given array of bytes.
- [`int.as_integer_ratio`](int.as_integer_ratio/README.md) — Return a pair of integers whose ratio is equal to the original integer and has a positive denominator.
- [`int.is_integer`](int.is_integer/README.md) — Returns True.

## Additional Methods on Float

The float type implements the [numbers.Real](https://docs.python.org/3.15/library/numbers.html#numbers.Real) `abstract base
class`. float also has the following additional methods.

- [`float.from_number`](float.from_number/README.md) — Class method to return a floating-point number constructed from a number *x*.
- [`float.as_integer_ratio`](float.as_integer_ratio/README.md) — Return a pair of integers whose ratio is exactly equal to the original float.
- [`float.is_integer`](float.is_integer/README.md) — Return True if the float instance is finite with integral value, and False otherwise:

Two methods support conversion to
and from hexadecimal strings.  Since Python's floats are stored
internally as binary numbers, converting a float to or from a
*decimal* string usually involves a small rounding error.  In
contrast, hexadecimal strings allow exact representation and
specification of floating-point numbers.  This can be useful when
debugging, and in numerical work.

- [`float.hex`](float.hex/README.md) — Return a representation of a floating-point number as a hexadecimal string.
- [`float.fromhex`](float.fromhex/README.md) — Class method to return the float represented by a hexadecimal string *s*.

Note that [float.hex()](float.hex/README.md) is an instance method, while
[float.fromhex()](float.fromhex/README.md) is a class method.

A hexadecimal string takes the form:

```
[sign] ['0x'] integer ['.' fraction] ['p' exponent]
```

where the optional `sign` may be either `+` or `-`, `integer`
and `fraction` are strings of hexadecimal digits, and `exponent`
is a decimal integer with an optional leading sign.  Case is not
significant, and there must be at least one hexadecimal digit in
either the integer or the fraction.  This syntax is similar to the
syntax specified in section 6.4.4.2 of the C99 standard, and also to
the syntax used in Java 1.5 onwards.  In particular, the output of
[float.hex()](float.hex/README.md) is usable as a hexadecimal floating-point literal in
C or Java code, and hexadecimal strings produced by C's `%a` format
character or Java's `Double.toHexString` are accepted by
[float.fromhex()](float.fromhex/README.md).

Note that the exponent is written in decimal rather than hexadecimal,
and that it gives the power of 2 by which to multiply the coefficient.
For example, the hexadecimal string `0x3.a7p10` represents the
floating-point number `(3 + 10./16 + 7./16**2) * 2.0**10`, or
`3740.0`:

``` python
>>> float.fromhex('0x3.a7p10')
3740.0
```
> Code: [example_01.py](example_01.py)

Applying the reverse conversion to `3740.0` gives a different
hexadecimal string representing the same number:

``` python
>>> float.hex(3740.0)
'0x1.d380000000000p+11'
```
> Code: [example_02.py](example_02.py)

## Additional Methods on Complex

The [complex](../../built-in-functions/complex/README.md) type implements the [numbers.Complex](https://docs.python.org/3.15/library/numbers.html#numbers.Complex)
[abstract base class](https://docs.python.org/3.15/glossary.html#term-abstract-base-class).
[complex](../../built-in-functions/complex/README.md) also has the following additional methods.

- [`complex.from_number`](complex.from_number/README.md) — Class method to convert a number to a complex number.

## Hashing of numeric types

For numbers `x` and `y`, possibly of different types, it's a requirement
that `hash(x) == hash(y)` whenever `x == y` (see the [__hash__()](https://docs.python.org/3.15/reference/datamodel.html#object.__hash__)
method documentation for more details).  For ease of implementation and
efficiency across a variety of numeric types (including [int](../../built-in-functions/int/README.md),
[float](../../built-in-functions/float/README.md), [decimal.Decimal](https://docs.python.org/3.15/library/decimal.html#decimal.Decimal) and [fractions.Fraction](https://docs.python.org/3.15/library/fractions.html#fractions.Fraction))
Python's hash for numeric types is based on a single mathematical function
that's defined for any rational number, and hence applies to all instances of
[int](../../built-in-functions/int/README.md) and [fractions.Fraction](https://docs.python.org/3.15/library/fractions.html#fractions.Fraction), and all finite instances of
[float](../../built-in-functions/float/README.md) and [decimal.Decimal](https://docs.python.org/3.15/library/decimal.html#decimal.Decimal).  Essentially, this function is
given by reduction modulo `P` for a fixed prime `P`.  The value of `P` is
made available to Python as the [modulus](https://docs.python.org/3.15/library/sys.html#sys.hash_info.modulus) attribute of
[sys.hash_info](https://docs.python.org/3.15/library/sys.html#sys.hash_info).

> **CPython implementation detail:** Currently, the prime used is `P = 2**31 - 1` on machines with 32-bit C
> longs and `P = 2**61 - 1` on machines with 64-bit C longs.

Here are the rules in detail:

- If `x = m / n` is a nonnegative rational number and `n` is not divisible
  by `P`, define `hash(x)` as `m * invmod(n, P) % P`, where `invmod(n,
  P)` gives the inverse of `n` modulo `P`.

- If `x = m / n` is a nonnegative rational number and `n` is
  divisible by `P` (but `m` is not) then `n` has no inverse
  modulo `P` and the rule above doesn't apply; in this case define
  `hash(x)` to be the constant value `sys.hash_info.inf`.

- If `x = m / n` is a negative rational number define `hash(x)`
  as `-hash(-x)`.  If the resulting hash is `-1`, replace it with
  `-2`.

- The particular values `sys.hash_info.inf` and `-sys.hash_info.inf`
  are used as hash values for positive
  infinity or negative infinity (respectively).

- For a [complex](../../built-in-functions/complex/README.md) number `z`, the hash values of the real
  and imaginary parts are combined by computing `hash(z.real) +
  sys.hash_info.imag * hash(z.imag)`, reduced modulo
  `2**sys.hash_info.width` so that it lies in
  `range(-2**(sys.hash_info.width - 1), 2**(sys.hash_info.width -
  1))`.  Again, if the result is `-1`, it's replaced with `-2`.

To clarify the above rules, here's some example Python code,
equivalent to the built-in hash, for computing the hash of a rational
number, [float](../../built-in-functions/float/README.md), or [complex](../../built-in-functions/complex/README.md):

``` python
import sys, math

def hash_fraction(m, n):
    """Compute the hash of a rational number m / n.

    Assumes m and n are integers, with n positive.
    Equivalent to hash(fractions.Fraction(m, n)).

    """
    P = sys.hash_info.modulus
    # Remove common factors of P.  (Unnecessary if m and n already coprime.)
    while m % P == n % P == 0:
        m, n = m // P, n // P

    if n % P == 0:
        hash_value = sys.hash_info.inf
    else:
        # Fermat's Little Theorem: pow(n, P-1, P) is 1, so
        # pow(n, P-2, P) gives the inverse of n modulo P.
        hash_value = (abs(m) % P) * pow(n, P - 2, P) % P
    if m < 0:
        hash_value = -hash_value
    if hash_value == -1:
        hash_value = -2
    return hash_value

def hash_float(x):
    """Compute the hash of a float x."""

    if math.isnan(x):
        return object.__hash__(x)
    elif math.isinf(x):
        return sys.hash_info.inf if x > 0 else -sys.hash_info.inf
    else:
        return hash_fraction(*x.as_integer_ratio())

def hash_complex(z):
    """Compute the hash of a complex number z."""

    hash_value = hash_float(z.real) + sys.hash_info.imag * hash_float(z.imag)
    # do a signed reduction modulo 2**sys.hash_info.width
    M = 2**(sys.hash_info.width - 1)
    hash_value = (hash_value & (M - 1)) - (hash_value & M)
    if hash_value == -1:
        hash_value = -2
    return hash_value
```

[^1]: As a consequence, the list `[1, 2]` is considered equal to `[1.0, 2.0]`, and similarly for tuples.
