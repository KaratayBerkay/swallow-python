## `int()`

```
int(number=0, /)
int(string, /, base=10)
```

Return an integer object constructed from a number or a string, or return
`0` if no arguments are given.

Examples:

``` python
>>> int(123.45)
123
>>> int('123')
123
>>> int('   -12_345\n')
-12345
>>> int('FACE', 16)
64206
>>> int('0xface', 0)
64206
>>> int('01110011', base=2)
115
```
> Code: [example_01.py](example_01.py)

If the argument defines [__int__()](https://docs.python.org/3.15/reference/datamodel.html#object.__int__),
`int(x)` returns `x.__int__()`.  If the argument defines
[__index__()](https://docs.python.org/3.15/reference/datamodel.html#object.__index__), it returns `x.__index__()`.
For floating-point numbers, this truncates towards zero.

If the argument is not a number or if *base* is given, then it must be a string,
[bytes](../bytes/README.md), or [bytearray](../bytearray/README.md) instance representing an integer
in radix *base*.  Optionally, the string can be preceded by `+` or `-`
(with no space in between), have leading zeros, be surrounded by whitespace,
and have single underscores interspersed between digits.

A base-n integer string contains digits, each representing a value from 0 to
n-1. The values 0--9 can be represented by any Unicode decimal digit. The
values 10--35 can be represented by `a` to `z` (or `A` to `Z`). The
default *base* is 10. The allowed bases are 0 and 2--36. Base-2, -8, and -16
strings can be optionally prefixed with `0b`/`0B`, `0o`/`0O`, or
`0x`/`0X`, as with integer literals in code.  For base 0, the string is
interpreted in a similar way to an [integer literal in code](https://docs.python.org/3.15/reference/lexical_analysis.html#integers),
in that the actual base is 2, 8, 10, or 16 as determined by the prefix. Base
0 also disallows leading zeros: `int('010', 0)` is not legal, while
`int('010')` and `int('010', 8)` are.

The integer type is described in [Numeric Types — int, float, complex](https://docs.python.org/3.15/builtins/stdtypes.html#typesnumeric).

> *Changed in version 3.4:* If *base* is not an instance of int and the *base* object has a
> [base.__index__](https://docs.python.org/3.15/reference/datamodel.html#object.__index__) method, that method is called
> to obtain an integer for the base.  Previous versions used
> [base.__int__](https://docs.python.org/3.15/reference/datamodel.html#object.__int__) instead of [base.__index__](https://docs.python.org/3.15/reference/datamodel.html#object.__index__).

> *Changed in version 3.6:* Grouping digits with underscores as in code literals is allowed.

> *Changed in version 3.7:* The first parameter is now positional-only.

> *Changed in version 3.8:* Falls back to [__index__()](https://docs.python.org/3.15/reference/datamodel.html#object.__index__) if [__int__()](https://docs.python.org/3.15/reference/datamodel.html#object.__int__) is not defined.

> *Changed in version 3.11:* int string inputs and string representations can be limited to
> help avoid denial of service attacks. A [ValueError](https://docs.python.org/3.15/builtins/exceptions.html#ValueError) is raised when
> the limit is exceeded while converting a string to an int or
> when converting an int into a string would exceed the limit.
> See the [integer string conversion length limitation](https://docs.python.org/3.15/builtins/stdtypes.html#int-max-str-digits) documentation.

> *Changed in version 3.14:* `int()` no longer delegates to the [__trunc__()](https://docs.python.org/3.15/reference/datamodel.html#object.__trunc__) method.

## Çözümlü kısa örnek

Metni tabana göre yorumlama ile floatı sıfıra doğru kesmeyi ayır.

```python
print(repr(int("12")))
# Sonuç: 12
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.37: int davranışını ayırt et**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; metni tabana göre yorumlama ile floatı sıfıra doğru kesmeyi ayır.

```python
int("101",2)
int(-3.9)
int("1.2")
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `5`; `-3`; `ValueError`.
- [ ] Metni tabana göre yorumlama ile floatı sıfıra doğru kesmeyi ayır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../isinstance/README.md)
<!-- learning-task:end -->
