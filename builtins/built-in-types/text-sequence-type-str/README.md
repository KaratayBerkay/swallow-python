Textual data in Python is handled with [str](str/README.md) objects, or strings.
Strings are immutable
[sequences](https://docs.python.org/3.15/builtins/stdtypes.html#typesseq) of Unicode code points.  String literals are
written in a variety of ways:

- Single quotes: `'allows embedded "double" quotes'`

- Double quotes: `"allows embedded 'single' quotes"`

- Triple quoted: `'''Three single quotes'''`, `"""Three double quotes"""`

Triple quoted strings may span multiple lines - all associated whitespace will
be included in the string literal.

String literals that are part of a single expression and have only whitespace
between them will be implicitly converted to a single string literal. That
is, `("spam " "eggs") == "spam eggs"`.

See [String and Bytes literals](https://docs.python.org/3.15/reference/lexical_analysis.html#strings) for more about the various forms of string literal,
including supported [escape sequences](https://docs.python.org/3.15/reference/lexical_analysis.html#escape-sequences), and the `r` ("raw") prefix that
disables most escape sequence processing.

Strings may also be created from other objects using the [str](str/README.md)
constructor.

Since there is no separate "character" type, indexing a string produces
strings of length 1. That is, for a non-empty string *s*, `s[0] == s[0:1]`.

There is also no mutable string type, but [str.join()](str.join/README.md) or
[io.StringIO](https://docs.python.org/3.15/library/io.html#io.StringIO) can be used to efficiently construct strings from
multiple fragments.

> *Changed in version 3.3:* For backwards compatibility with the Python 2 series, the `u` prefix is
> once again permitted on string literals. It has no effect on the meaning
> of string literals and cannot be combined with the `r` prefix.

- [`str`](str/README.md) — Return a string version of *object*.

## String Methods

Strings implement all of the [common](https://docs.python.org/3.15/builtins/stdtypes.html#typesseq-common) sequence
operations, along with the additional methods described below.

Strings also support two styles of string formatting, one providing a large
degree of flexibility and customization (see [str.format()](str.format/README.md),
[Format string syntax](https://docs.python.org/3.15/library/string.html#formatstrings) and [Custom string formatting](https://docs.python.org/3.15/library/string.html#string-formatting)) and the other based on C
`printf` style formatting that handles a narrower range of types and is
slightly harder to use correctly, but is often faster for the cases it can
handle ([printf-style String Formatting](https://docs.python.org/3.15/builtins/stdtypes.html#old-string-formatting)).

The [Text Processing Services](https://docs.python.org/3.15/library/text.html#textservices) section of the standard library covers a number of
other modules that provide various text related utilities (including regular
expression support in the [re](https://docs.python.org/3.15/library/re.html#module-re) module).

- [`str.capitalize`](str.capitalize/README.md) — Return a copy of the string with its first character capitalized and the rest lowercased.
- [`str.casefold`](str.casefold/README.md) — Return a casefolded copy of the string.
- [`str.center`](str.center/README.md) — Return centered in a string of length *width*.
- [`str.count`](str.count/README.md) — Return the number of non-overlapping occurrences of substring *sub* in the range [*start*, *end*].
- [`str.encode`](str.encode/README.md) — Return the string encoded to bytes.
- [`str.endswith`](str.endswith/README.md) — Return True if the string ends with the specified *suffix*, otherwise return False.
- [`str.expandtabs`](str.expandtabs/README.md) — Return a copy of the string where all tab characters are replaced by one or more spaces, depending on the current column and the given tab size.
- [`str.find`](str.find/README.md) — Return the lowest index in the string where substring *sub* is found within the slice s[start:end].
- [`str.format`](str.format/README.md) — Perform a string formatting operation.
- [`str.format_map`](str.format_map/README.md) — Similar to str.format(**mapping), except that mapping is used directly and not copied to a dict.
- [`str.index`](str.index/README.md) — Like find(), but raise ValueError when the substring is not found.
- [`str.isalnum`](str.isalnum/README.md) — Return True if all characters in the string are alphanumeric and there is at least one character, False otherwise.
- [`str.isalpha`](str.isalpha/README.md) — Return True if all characters in the string are alphabetic and there is at least one character, False otherwise.
- [`str.isascii`](str.isascii/README.md) — Return True if the string is empty or all characters in the string are ASCII, False otherwise.
- [`str.isdecimal`](str.isdecimal/README.md) — Return True if all characters in the string are decimal characters and there is at least one character, False otherwise.
- [`str.isdigit`](str.isdigit/README.md) — Return True if all characters in the string are digits and there is at least one character, False otherwise.
- [`str.isidentifier`](str.isidentifier/README.md) — Return True if the string is a valid identifier according to the language definition, section Names (identifiers and keywords).
- [`str.islower`](str.islower/README.md) — Return True if all cased characters [^1] in the string are lowercase and there is at least one cased character, False otherwise.
- [`str.isnumeric`](str.isnumeric/README.md) — Return True if all characters in the string are numeric characters, and there is at least one character, False otherwise.
- [`str.isprintable`](str.isprintable/README.md) — Return True if all characters in the string are printable, False if it contains at least one non-printable character.
- [`str.isspace`](str.isspace/README.md) — Return True if there are only whitespace characters in the string and there is at least one character, False otherwise.
- [`str.istitle`](str.istitle/README.md) — Return True if the string is a titlecased string and there is at least one character, for example uppercase characters may only follow uncased…
- [`str.isupper`](str.isupper/README.md) — Return True if all cased characters [^1] in the string are uppercase and there is at least one cased character, False otherwise.
- [`str.join`](str.join/README.md) — Return a string which is the concatenation of the strings in *iterable*.
- [`str.ljust`](str.ljust/README.md) — Return the string left justified in a string of length *width*.
- [`str.lower`](str.lower/README.md) — Return a copy of the string with all the cased characters [^1] converted to lowercase.
- [`str.lstrip`](str.lstrip/README.md) — Return a copy of the string with leading characters removed.
- [`str.maketrans`](str.maketrans/README.md) — This static method returns a translation table usable for str.translate().
- [`str.partition`](str.partition/README.md) — Split the string at the first occurrence of *sep*, and return a 3-tuple containing the part before the separator, the separator itself, and the…
- [`str.removeprefix`](str.removeprefix/README.md) — If the string starts with the *prefix* string, return string[len(prefix):].
- [`str.removesuffix`](str.removesuffix/README.md) — If the string ends with the *suffix* string and that *suffix* is not empty, return string[:-len(suffix)].
- [`str.replace`](str.replace/README.md) — Return a copy of the string with all occurrences of substring *old* replaced by *new*.
- [`str.rfind`](str.rfind/README.md) — Return the highest index in the string where substring *sub* is found, such that *sub* is contained within s[start:end].
- [`str.rindex`](str.rindex/README.md) — Like rfind() but raises ValueError when the substring *sub* is not found.
- [`str.rjust`](str.rjust/README.md) — Return the string right justified in a string of length *width*.
- [`str.rpartition`](str.rpartition/README.md) — Split the string at the last occurrence of *sep*, and return a 3-tuple containing the part before the separator, the separator itself, and the…
- [`str.rsplit`](str.rsplit/README.md) — Return a list of the words in the string, using *sep* as the delimiter string.
- [`str.rstrip`](str.rstrip/README.md) — Return a copy of the string with trailing characters removed.
- [`str.split`](str.split/README.md) — Return a list of the words in the string, using *sep* as the delimiter string.
- [`str.splitlines`](str.splitlines/README.md) — Return a list of the lines in the string, breaking at line boundaries.
- [`str.startswith`](str.startswith/README.md) — Return True if string starts with the *prefix*, otherwise return False.
- [`str.strip`](str.strip/README.md) — Return a copy of the string with the leading and trailing characters removed.
- [`str.swapcase`](str.swapcase/README.md) — Return a copy of the string with uppercase characters converted to lowercase and vice versa.
- [`str.title`](str.title/README.md) — Return a titlecased version of the string where words start with an uppercase character and the remaining characters are lowercase.
- [`str.translate`](str.translate/README.md) — Return a copy of the string in which each character has been mapped through the given translation table.
- [`str.upper`](str.upper/README.md) — Return a copy of the string with all the cased characters [^1] converted to uppercase.
- [`str.zfill`](str.zfill/README.md) — Return a copy of the string left filled with ASCII '0' digits to make a string of length *width*.

## Formatted String Literals (f-strings)

> *Added in version 3.6.*

> *Changed in version 3.7:* The `await` and `async for` can be used in expressions
> within f-strings.

> *Changed in version 3.8:* Added the debug specifier (`=`)

> *Changed in version 3.12:* Many restrictions on expressions within f-strings have been removed.
> Notably, nested strings, comments, and backslashes are now permitted.

An f-string (formally a formatted string literal) is
a string literal that is prefixed with `f` or `F`.
This type of string literal allows embedding the results of arbitrary Python
expressions within *replacement fields*, which are delimited by curly
brackets (`{}`).
Each replacement field must contain an expression, optionally followed by:

- a *debug specifier* -- an equal sign (`=`);

- a *conversion specifier* -- `!s`, `!r` or `!a`; and/or

- a *format specifier* prefixed with a colon (`:`).

See the [Lexical Analysis section on f-strings](https://docs.python.org/3.15/reference/lexical_analysis.html#f-strings) for details
on the syntax of these fields.

### Debug specifier

> *Added in version 3.8.*

If a debug specifier -- an equal sign (`=`) -- appears after the replacement
field expression, the resulting f-string will contain the expression's source,
the equal sign, and the value of the expression.
This is often useful for debugging:

``` python
>>> number = 14.3
>>> f'{number=}'
'number=14.3'
>>> f'{ number  -  4  = }'
' number  -  4  = 10.3'
```
> Code: [example_01.py](example_01.py)

Whitespace before, inside and after the expression, as well as whitespace
after the equal sign, is significant --- it is retained in the result:

### Conversion specifier

By default, the value of a replacement field expression is converted to
a string using [str()](../../built-in-functions/str/README.md):

``` python
>>> from fractions import Fraction
>>> one_third = Fraction(1, 3)
>>> f'{one_third}'
'1/3'
>>> f'{one_third = }'
'one_third = Fraction(1, 3)'
>>> str(one_third)
'1/3'
>>> repr(one_third)
'Fraction(1, 3)'

>>> f'{one_third!s} is {one_third!r}'
'1/3 is Fraction(1, 3)'

>>> string = "¡kočka 😸!"
>>> ascii(string)
"'\\xa1ko\\u010dka \\U0001f638!'"

>>> f'{string = !a}'
"string = '\\xa1ko\\u010dka \\U0001f638!'"
```
> Code: [example_02.py](example_02.py)

When a debug specifier but no format specifier is used, the default conversion
instead uses [repr()](../../built-in-functions/repr/README.md):

The conversion can be specified explicitly using one of these specifiers:

- `!s` for [str()](../../built-in-functions/str/README.md)

- `!r` for [repr()](../../built-in-functions/repr/README.md)

- `!a` for [ascii()](../../built-in-functions/ascii/README.md)

For example:

### Format specifier

After the expression has been evaluated, and possibly converted using an
explicit conversion specifier, it is formatted using the [format()](../../built-in-functions/format/README.md) function.
If the replacement field includes a *format specifier* introduced by a colon
(`:`), the specifier is passed to [format()](../../built-in-functions/format/README.md) as the second argument.
The result of [format()](../../built-in-functions/format/README.md) is then used as the final value for the
replacement field. For example:

``` python
>>> from fractions import Fraction
>>> one_third = Fraction(1, 3)
>>> f'{one_third:.6f}'
'0.333333'
>>> f'{one_third:_^+10}'
'___+1/3___'
>>> f'{one_third!r:_^20}'
'___Fraction(1, 3)___'
>>> f'{one_third = :~>10}~'
'one_third = ~~~~~~~1/3~'
```
> Code: [example_03.py](example_03.py)

## Template String Literals (t-strings)

A t-string (formally a template string literal) is
a string literal that is prefixed with `t` or `T`.

These strings follow the same syntax and evaluation rules as
[formatted string literals](https://docs.python.org/3.15/builtins/stdtypes.html#stdtypes-fstrings),
with the following differences:

- Rather than evaluating to a `str` object, template string literals evaluate
  to a [string.templatelib.Template](https://docs.python.org/3.15/library/string.templatelib.html#string.templatelib.Template) object.

- The [format()](../../built-in-functions/format/README.md) protocol is not used.
  Instead, the format specifier and conversions (if any) are passed to
  a new [Interpolation](https://docs.python.org/3.15/library/string.templatelib.html#string.templatelib.Interpolation) object that is created
  for each evaluated expression.
  It is up to code that processes the resulting [Template](https://docs.python.org/3.15/library/string.templatelib.html#string.templatelib.Template)
  object to decide how to handle format specifiers and conversions.

- Format specifiers containing nested replacement fields are evaluated eagerly,
  prior to being passed to the [Interpolation](https://docs.python.org/3.15/library/string.templatelib.html#string.templatelib.Interpolation) object.
  For instance, an interpolation of the form `{amount:.{precision}f}` will
  evaluate the inner expression `{precision}` to determine the value of the
  `format_spec` attribute.
  If `precision` were to be `2`, the resulting format specifier
  would be `'.2f'`.

- When the equals sign `'='` is provided in an interpolation expression,
  the text of the expression is appended to the literal string that precedes
  the relevant interpolation.
  This includes the equals sign and any surrounding whitespace.
  The `Interpolation` instance for the expression will be created as
  normal, except that [conversion](https://docs.python.org/3.15/library/string.templatelib.html#string.templatelib.Interpolation.conversion) will
  be set to '`r`' ([repr()](../../built-in-functions/repr/README.md)) by default.
  If an explicit conversion or format specifier is provided,
  this will override the default behaviour.

## ``printf``-style String Formatting

> **Note**
>
> The formatting operations described here exhibit a variety of quirks that
> lead to a number of common errors (such as failing to display tuples and
> dictionaries correctly).
>
> Using [formatted string literals](https://docs.python.org/3.15/reference/lexical_analysis.html#f-strings), the [str.format()](str.format/README.md)
> interface, or [string.Template](https://docs.python.org/3.15/library/string.html#string.Template) may help avoid these errors.
> Each of these alternatives provides their own trade-offs and benefits of
> simplicity, flexibility, and/or extensibility.

String objects have one unique built-in operation: the `%` operator (modulo).
This is also known as the string *formatting* or *interpolation* operator.
Given `format % values` (where *format* is a string), `%` conversion
specifications in *format* are replaced with zero or more elements of *values*.
The effect is similar to using the `sprintf` function in the C language.
For example:

``` python
>>> print('%s has %d quote types.' % ('Python', 2))
Python has 2 quote types.
```
> Code: [example_04.py](example_04.py)

If *format* requires a single argument, *values* may be a single non-tuple
object. [^1]  Otherwise, *values* must be a tuple with exactly the number of
items specified by the format string, or a single mapping object (for example, a
dictionary).

A conversion specifier contains two or more characters and has the following
components, which must occur in this order:

1. The `'%'` character, which marks the start of the specifier.

2. Mapping key (optional), consisting of a parenthesised sequence of characters
   (for example, `(somename)`).

3. Conversion flags (optional), which affect the result of some conversion
   types.

4. Minimum field width (optional).  If specified as an `'*'` (asterisk), the
   actual width is read from the next element of the tuple in *values*, and the
   object to convert comes after the minimum field width and optional precision.

5. Precision (optional), given as a `'.'` (dot) followed by the precision.  If
   specified as `'*'` (an asterisk), the actual precision is read from the next
   element of the tuple in *values*, and the value to convert comes after the
   precision.

6. Length modifier (optional).

7. Conversion type.

When the right argument is a dictionary (or other mapping type), then the
formats in the string *must* include a parenthesised mapping key into that
dictionary inserted immediately after the `'%'` character. The mapping key
selects the value to be formatted from the mapping.  For example:

``` python
>>> print('%(language)s has %(number)03d quote types.' %
...       {'language': "Python", "number": 2})
Python has 002 quote types.
```
> Code: [example_05.py](example_05.py)

In this case no `*` specifiers may occur in a format (since they require a
sequential parameter list).

The conversion flag characters are:

| Flag | Meaning |
| --- | --- |
| `'#'` | The value conversion will use the "alternate form" (where defined below). |
| `'0'` | The conversion will be zero padded for numeric values. |
| `'-'` | The converted value is left adjusted (overrides the `'0'` conversion if both are given). |
| `' '` | (a space) A blank should be left before a positive number (or empty string) produced by a signed conversion. |
| `'+'` | A sign character (`'+'` or `'-'`) will precede the conversion (overrides a "space" flag). |

A length modifier (`h`, `l`, or `L`) may be present, but is ignored as it
is not necessary for Python -- so e.g. `%ld` is identical to `%d`.

The conversion types are:

| Conversion | Meaning | Notes |
| --- | --- | --- |
| `'d'` | Signed integer decimal. |  |
| `'i'` | Signed integer decimal. |  |
| `'o'` | Signed octal value. | (1) |
| `'u'` | Obsolete type -- it is identical to `'d'`. | (6) |
| `'x'` | Signed hexadecimal (lowercase). | (2) |
| `'X'` | Signed hexadecimal (uppercase). | (2) |
| `'e'` | Floating-point exponential format (lowercase). | (3) |
| `'E'` | Floating-point exponential format (uppercase). | (3) |
| `'f'` | Floating-point decimal format. | (3) |
| `'F'` | Floating-point decimal format. | (3) |
| `'g'` | Floating-point format. Uses lowercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise. | (4) |
| `'G'` | Floating-point format. Uses uppercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise. | (4) |
| `'c'` | Single character (accepts integer or single character string). |  |
| `'r'` | String (converts any Python object using [repr()](../../built-in-functions/repr/README.md)). | (5) |
| `'s'` | String (converts any Python object using [str()](../../built-in-functions/str/README.md)). | (5) |
| `'a'` | String (converts any Python object using [ascii()](../../built-in-functions/ascii/README.md)). | (5) |
| `'%'` | No argument is converted, results in a `'%'` character in the result. |  |

For floating-point formats, the result should be correctly rounded to a given
precision `p` of digits after the decimal point.  The rounding mode matches
that of the [round()](../../built-in-functions/round/README.md) builtin.

Notes:

1. The alternate form causes a leading octal specifier (`'0o'`) to be
   inserted before the first digit.

2. The alternate form causes a leading `'0x'` or `'0X'` (depending on whether
   the `'x'` or `'X'` format was used) to be inserted before the first digit.

3. The alternate form causes the result to always contain a decimal point, even if
   no digits follow it.

   The precision determines the number of digits after the decimal point and
   defaults to 6.

4. The alternate form causes the result to always contain a decimal point, and
   trailing zeroes are not removed as they would otherwise be.

   The precision determines the number of significant digits before and after the
   decimal point and defaults to 6.

5. If precision is `N`, the output is truncated to `N` characters.

6. See [PEP 237](https://peps.python.org/pep-237/).

Since Python strings have an explicit length, `%s` conversions do not assume
that `'\0'` is the end of the string.

> *Changed in version 3.1:* `%f` conversions for numbers whose absolute value is over 1e50 are no
> longer replaced by `%g` conversions.

[^1]: To format only a tuple you should therefore provide a singleton tuple whose only element is the tuple to be formatted.

## Çözümlü kısa örnek

Unicode karakteriyle bayt dizisi aynı nesne değildir

```python
print(repr("İ"[0]))
# Sonuç: 'İ'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9: text-sequence-type-str davranışını ayırt et**

#### Önce

[b:2](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; unicode karakteriyle bayt dizisi aynı nesne değildir

```python
len("İ")
"a" "b"
"ab"[0:9]
```

Aynı çalışmaya `%` biçimlendirmeyle ad ve puan yerleştirmeyi, `%%` ile literal yüzdeyi, yanlış sayıda alan verilmesi hatasını ekle. Metin içine yerleştirmeyle özgün Unicode metni değiştirmeyi ayır.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `1`; `'ab'`; `'ab'`.
- [ ] Unicode karakteriyle bayt dizisi aynı nesne değildir
- [ ] Biçimlendirme yeni str verir; literal yüzde kaçışı ve argüman sayısı uyuşmazlığı açıklanır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](str/README.md)
<!-- learning-task:end -->

<!-- learning-milestone:start -->
### Klasör milestone görevi

**Milestone: Satır tabanlı metni çözümle**

#### Önce

Bu klasördeki bütün bölüm görevleri ve alt klasör milestone kontrolleri tamamlanmış olmalı. Sırayı [görev dizininden](../../../TASKS.md) kontrol et.

#### Tek görev

`"  Ada:7\nEce:9\nAda:8\n"` metnini splitlines ile satırlara ayır; kenar boşluklarını temizle; partition ile ad ve puanı çıkar. Boş ad, ayırıcısız satır ve boş metin girdilerini açıkça ele al. Yinelenen adların son değerini kullanıp adlara göre sıralı `ad=puan` metnini join ile üret; özgün metni koru.

#### Geçiş ölçütleri

- [ ] Örnek çıktı Ada=8 ve Ece=9 satırlarıdır; hatalı satırların davranışı tutarlı seçilmiştir.
- [ ] Split/partition/strip/join seçimleri ve str değişmezliği açıklanmıştır; tüm yöntemleri gereksiz yere kullanma şartı yoktur.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../binary-sequence-types-bytes-bytearray-memoryview/README.md)
<!-- learning-milestone:end -->
