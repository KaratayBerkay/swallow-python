CPython has a global limit for converting between [int](../../built-in-functions/int/README.md) and [str](../text-sequence-type-str/str/README.md)
to mitigate denial of service attacks. This limit *only* applies to decimal or
other non-power-of-two number bases. Hexadecimal, octal, and binary conversions
are unlimited. The limit can be configured.

The [int](../../built-in-functions/int/README.md) type in CPython is an arbitrary length number stored in binary
form (commonly known as a "bignum"). There exists no algorithm that can convert
a string to a binary integer or a binary integer to a string in linear time,
*unless* the base is a power of 2. Even the best known algorithms for base 10
have sub-quadratic complexity. Converting a large value such as `int('1' *
500_000)` can take over a second on a fast CPU.

Limiting conversion size offers a practical way to avoid [CVE-2020-10735](https://www.cve.org/CVERecord?id=CVE-2020-10735).

The limit is applied to the number of digit characters in the input or output
string when a non-linear conversion algorithm would be involved.  Underscores
and the sign are not counted towards the limit.

When an operation would exceed the limit, a [ValueError](https://docs.python.org/3.15/builtins/exceptions.html#ValueError) is raised:

``` python
>>> import sys
>>> sys.set_int_max_str_digits(4300)  # Illustrative, this is the default.
>>> _ = int('2' * 5432)
Traceback (most recent call last):
...
ValueError: Exceeds the limit (4300 digits) for integer string conversion: value has 5432 digits; use sys.set_int_max_str_digits() to increase the limit
>>> i = int('2' * 4300)
>>> len(str(i))
4300
>>> i_squared = i*i
>>> len(str(i_squared))
Traceback (most recent call last):
...
ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
>>> len(hex(i_squared))
7144
>>> assert int(hex(i_squared), base=16) == i*i  # Hexadecimal is unlimited.
```
> Code: [example_01.py](example_01.py)

The default limit is 4300 digits as provided in
[sys.int_info.default_max_str_digits](https://docs.python.org/3.15/library/sys.html#sys.int_info).
The lowest limit that can be configured is 640 digits as provided in
[sys.int_info.str_digits_check_threshold](https://docs.python.org/3.15/library/sys.html#sys.int_info).

Verification:

``` python
>>> import sys
>>> assert sys.int_info.default_max_str_digits == 4300, sys.int_info
>>> assert sys.int_info.str_digits_check_threshold == 640, sys.int_info
>>> msg = int('578966293710682886880994035146873798396722250538762761564'
...           '9252925514383915483333812743580549779436104706260696366600'
...           '571186405732').to_bytes(53, 'big')
...
```
> Code: [example_02.py](example_02.py)

> *Added in version 3.11.*

## Affected APIs

The limitation only applies to potentially slow conversions between [int](../../built-in-functions/int/README.md)
and [str](../text-sequence-type-str/str/README.md) or [bytes](../binary-sequence-types-bytes-bytearray-memoryview/bytes/README.md):

- `int(string)` with default base 10.

- `int(string, base)` for all bases that are not a power of 2.

- `str(integer)`.

- `repr(integer)`.

- any other string conversion to base 10, for example `f"{integer}"`,
  `"{}".format(integer)`, or `b"%d" % integer`.

The limitations do not apply to functions with a linear algorithm:

- `int(string, base)` with base 2, 4, 8, 16, or 32.

- [int.from_bytes()](../numeric-types-int-float-complex/int.from_bytes/README.md) and [int.to_bytes()](../numeric-types-int-float-complex/int.to_bytes/README.md).

- [hex()](../../built-in-functions/hex/README.md), [oct()](../../built-in-functions/oct/README.md), [bin()](../../built-in-functions/bin/README.md).

- [Format specification mini-language](https://docs.python.org/3.15/library/string.html#formatspec) for hex, octal, and binary numbers.

- [str](../text-sequence-type-str/str/README.md) to [float](../../built-in-functions/float/README.md).

- [str](../text-sequence-type-str/str/README.md) to [decimal.Decimal](https://docs.python.org/3.15/library/decimal.html#decimal.Decimal).

## Configuring the limit

Before Python starts up you can use an environment variable or an interpreter
command line flag to configure the limit:

- [PYTHONINTMAXSTRDIGITS](https://docs.python.org/3.15/using/cmdline.html#envvar-PYTHONINTMAXSTRDIGITS), e.g.
  `PYTHONINTMAXSTRDIGITS=640 python3` to set the limit to 640 or
  `PYTHONINTMAXSTRDIGITS=0 python3` to disable the limitation.

- [-X int_max_str_digits](https://docs.python.org/3.15/using/cmdline.html#cmdoption-X), e.g.
  `python3 -X int_max_str_digits=640`

- `sys.flags.int_max_str_digits` contains the value of
  [PYTHONINTMAXSTRDIGITS](https://docs.python.org/3.15/using/cmdline.html#envvar-PYTHONINTMAXSTRDIGITS) or [-X int_max_str_digits](https://docs.python.org/3.15/using/cmdline.html#cmdoption-X).
  If both the env var and the `-X` option are set, the `-X` option takes
  precedence. A value of *-1* indicates that both were unset, thus a value of
  `sys.int_info.default_max_str_digits` was used during initialization.

From code, you can inspect the current limit and set a new one using these
[sys](https://docs.python.org/3.15/library/sys.html#module-sys) APIs:

- [sys.get_int_max_str_digits()](https://docs.python.org/3.15/library/sys.html#sys.get_int_max_str_digits) and [sys.set_int_max_str_digits()](https://docs.python.org/3.15/library/sys.html#sys.set_int_max_str_digits) are
  a getter and setter for the interpreter-wide limit. Subinterpreters have
  their own limit.

Information about the default and minimum can be found in [sys.int_info](https://docs.python.org/3.15/library/sys.html#sys.int_info):

- [sys.int_info.default_max_str_digits](https://docs.python.org/3.15/library/sys.html#sys.int_info) is the compiled-in
  default limit.

- [sys.int_info.str_digits_check_threshold](https://docs.python.org/3.15/library/sys.html#sys.int_info) is the lowest
  accepted value for the limit (other than 0 which disables it).

> *Added in version 3.11.*

> **Caution**
>
> Setting a low limit *can* lead to problems. While rare, code exists that
> contains integer constants in decimal in their source that exceed the
> minimum threshold. A consequence of setting the limit is that Python source
> code containing decimal integer literals longer than the limit will
> encounter an error during parsing, usually at startup time or import time or
> even at installation time - anytime an up to date `.pyc` does not already
> exist for the code. A workaround for source that contains such large
> constants is to convert them to `0x` hexadecimal form as it has no limit.
>
> Test your application thoroughly if you use a low limit. Ensure your tests
> run with the limit set early via the environment or flag so that it applies
> during startup and even during any installation step that may invoke Python
> to precompile `.py` sources to `.pyc` files.

## Recommended configuration

The default `sys.int_info.default_max_str_digits` is expected to be
reasonable for most applications. If your application requires a different
limit, set it from your main entry point using Python version agnostic code as
these APIs were added in security patch releases in versions before 3.12.

Example:

``` python
>>> import sys
>>> if hasattr(sys, "set_int_max_str_digits"):
...     upper_bound = 68000
...     lower_bound = 4004
...     current_limit = sys.get_int_max_str_digits()
...     if current_limit == 0 or current_limit > upper_bound:
...         sys.set_int_max_str_digits(upper_bound)
...     elif current_limit < lower_bound:
...         sys.set_int_max_str_digits(lower_bound)
```
> Code: [example_03.py](example_03.py)

If you need to disable it entirely, set it to `0`.
