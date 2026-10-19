The core built-in types for manipulating binary data are [bytes](bytes/README.md) and
[bytearray](bytearray/README.md). They are supported by [memoryview](memoryview/README.md) which uses
the [buffer protocol](https://docs.python.org/3.15/c-api/buffer.html#bufferobjects) to access the memory of other
binary objects without needing to make a copy.

The [array](https://docs.python.org/3.15/library/array.html#module-array) module supports efficient storage of basic data types like
32-bit integers and IEEE754 double-precision floating values.

## Bytes Objects

Bytes objects are immutable sequences of single bytes. Since many major
binary protocols are based on the ASCII text encoding, bytes objects offer
several methods that are only valid when working with ASCII compatible
data and are closely related to string objects in a variety of other ways.

- [`bytes`](bytes/README.md) — Firstly, the syntax for bytes literals is largely the same as that for string literals, except that a b prefix is added:

Since bytes objects are sequences of integers (akin to a tuple), for a bytes
object *b*, `b[0]` will be an integer, while `b[0:1]` will be a bytes
object of length 1.  (This contrasts with text strings, where both indexing
and slicing will produce a string of length 1)

The representation of bytes objects uses the literal format (`b'...'`)
since it is often more useful than e.g. `bytes([46, 46, 46])`.  You can
always convert a bytes object into a list of integers using `list(b)`.

## Bytearray Objects

[bytearray](bytearray/README.md) objects are a mutable counterpart to [bytes](bytes/README.md)
objects.

- [`bytearray`](bytearray/README.md) — There is no dedicated literal syntax for bytearray objects, instead they are always created by calling the constructor:

Since bytearray objects are sequences of integers (akin to a list), for a
bytearray object *b*, `b[0]` will be an integer, while `b[0:1]` will be
a bytearray object of length 1.  (This contrasts with text strings, where
both indexing and slicing will produce a string of length 1)

The representation of bytearray objects uses the bytes literal format
(`bytearray(b'...')`) since it is often more useful than e.g.
`bytearray([46, 46, 46])`.  You can always convert a bytearray object into
a list of integers using `list(b)`.

> **See also**
>
> For detailed information on thread-safety guarantees for [bytearray](bytearray/README.md)
> objects, see [Thread safety for bytearray objects](https://docs.python.org/3.15/builtins/threadsafety.html#thread-safety-bytearray).

## Bytes and Bytearray Operations

Both bytes and bytearray objects support the [common](https://docs.python.org/3.15/builtins/stdtypes.html#typesseq-common)
sequence operations. They interoperate not just with operands of the same
type, but with any [bytes-like object](https://docs.python.org/3.15/glossary.html#term-bytes-like-object). Due to this flexibility, they can be
freely mixed in operations without causing errors. However, the return type
of the result may depend on the order of operands.

> **Note**
>
> The methods on bytes and bytearray objects don't accept strings as their
> arguments, just as the methods on strings don't accept bytes as their
> arguments.  For example, you have to write:
>
> ``` python
> a = "abc"
> b = a.replace("a", "f")
> ```
>
> and:
>
> ``` python
> a = b"abc"
> b = a.replace(b"a", b"f")
> ```

Some bytes and bytearray operations assume the use of ASCII compatible
binary formats, and hence should be avoided when working with arbitrary
binary data. These restrictions are covered below.

> **Note**
>
> Using these ASCII based operations to manipulate binary data that is not
> stored in an ASCII based format may lead to data corruption.

The following methods on bytes and bytearray objects can be used with
arbitrary binary data.

- [`bytes.count`](bytes.count/README.md) — Return the number of non-overlapping occurrences of subsequence *sub* in the range [*start*, *end*].
- [`bytearray.count`](bytearray.count/README.md) — Documented together with bytes.count.
- [`bytes.removeprefix`](bytes.removeprefix/README.md) — If the binary data starts with the *prefix* string, return bytes[len(prefix):].
- [`bytearray.removeprefix`](bytearray.removeprefix/README.md) — Documented together with bytes.removeprefix.
- [`bytes.removesuffix`](bytes.removesuffix/README.md) — If the binary data ends with the *suffix* string and that *suffix* is not empty, return bytes[:-len(suffix)].
- [`bytearray.removesuffix`](bytearray.removesuffix/README.md) — Documented together with bytes.removesuffix.
- [`bytes.decode`](bytes.decode/README.md) — Return the bytes decoded to a str.
- [`bytearray.decode`](bytearray.decode/README.md) — Documented together with bytes.decode.
- [`bytes.endswith`](bytes.endswith/README.md) — Return True if the binary data ends with the specified *suffix*, otherwise return False.
- [`bytearray.endswith`](bytearray.endswith/README.md) — Documented together with bytes.endswith.
- [`bytes.find`](bytes.find/README.md) — Return the lowest index in the data where the subsequence *sub* is found, such that *sub* is contained in the slice s[start:end].
- [`bytearray.find`](bytearray.find/README.md) — Documented together with bytes.find.
- [`bytes.index`](bytes.index/README.md) — Like find(), but raise ValueError when the subsequence is not found.
- [`bytearray.index`](bytearray.index/README.md) — Documented together with bytes.index.
- [`bytes.join`](bytes.join/README.md) — Return a bytes or bytearray object which is the concatenation of the binary data sequences in *iterable*.
- [`bytearray.join`](bytearray.join/README.md) — Documented together with bytes.join.
- [`bytes.maketrans`](bytes.maketrans/README.md) — This static method returns a translation table usable for bytes.translate() that will map each character in *from* into the character at the same…
- [`bytearray.maketrans`](bytearray.maketrans/README.md) — Documented together with bytes.maketrans.
- [`bytes.partition`](bytes.partition/README.md) — Split the sequence at the first occurrence of *sep*, and return a 3-tuple containing the part before the separator, the separator itself or its…
- [`bytearray.partition`](bytearray.partition/README.md) — Documented together with bytes.partition.
- [`bytes.replace`](bytes.replace/README.md) — Return a copy of the sequence with all occurrences of subsequence *old* replaced by *new*.
- [`bytearray.replace`](bytearray.replace/README.md) — Documented together with bytes.replace.
- [`bytes.rfind`](bytes.rfind/README.md) — Return the highest index in the sequence where the subsequence *sub* is found, such that *sub* is contained within s[start:end].
- [`bytearray.rfind`](bytearray.rfind/README.md) — Documented together with bytes.rfind.
- [`bytes.rindex`](bytes.rindex/README.md) — Like rfind() but raises ValueError when the subsequence *sub* is not found.
- [`bytearray.rindex`](bytearray.rindex/README.md) — Documented together with bytes.rindex.
- [`bytes.rpartition`](bytes.rpartition/README.md) — Split the sequence at the last occurrence of *sep*, and return a 3-tuple containing the part before the separator, the separator itself or its…
- [`bytearray.rpartition`](bytearray.rpartition/README.md) — Documented together with bytes.rpartition.
- [`bytes.startswith`](bytes.startswith/README.md) — Return True if the binary data starts with the specified *prefix*, otherwise return False.
- [`bytearray.startswith`](bytearray.startswith/README.md) — Documented together with bytes.startswith.
- [`bytes.translate`](bytes.translate/README.md) — Return a copy of the bytes or bytearray object where all bytes occurring in the optional argument *delete* are removed, and the remaining bytes…
- [`bytearray.translate`](bytearray.translate/README.md) — Documented together with bytes.translate.

The following methods on bytes and bytearray objects have default behaviours
that assume the use of ASCII compatible binary formats, but can still be used
with arbitrary binary data by passing appropriate arguments. Note that all of
the bytearray methods in this section do *not* operate in place, and instead
produce new objects.

- [`bytes.center`](bytes.center/README.md) — Return a copy of the object centered in a sequence of length *width*.
- [`bytearray.center`](bytearray.center/README.md) — Documented together with bytes.center.
- [`bytes.ljust`](bytes.ljust/README.md) — Return a copy of the object left justified in a sequence of length *width*.
- [`bytearray.ljust`](bytearray.ljust/README.md) — Documented together with bytes.ljust.
- [`bytes.lstrip`](bytes.lstrip/README.md) — Return a copy of the sequence with specified leading bytes removed.
- [`bytearray.lstrip`](bytearray.lstrip/README.md) — Documented together with bytes.lstrip.
- [`bytes.rjust`](bytes.rjust/README.md) — Return a copy of the object right justified in a sequence of length *width*.
- [`bytearray.rjust`](bytearray.rjust/README.md) — Documented together with bytes.rjust.
- [`bytes.rsplit`](bytes.rsplit/README.md) — Split the binary sequence into subsequences of the same type, using *sep* as the delimiter string.
- [`bytearray.rsplit`](bytearray.rsplit/README.md) — Documented together with bytes.rsplit.
- [`bytes.rstrip`](bytes.rstrip/README.md) — Return a copy of the sequence with specified trailing bytes removed.
- [`bytearray.rstrip`](bytearray.rstrip/README.md) — Documented together with bytes.rstrip.
- [`bytes.split`](bytes.split/README.md) — Split the binary sequence into subsequences of the same type, using *sep* as the delimiter string.
- [`bytearray.split`](bytearray.split/README.md) — Documented together with bytes.split.
- [`bytes.strip`](bytes.strip/README.md) — Return a copy of the sequence with specified leading and trailing bytes removed.
- [`bytearray.strip`](bytearray.strip/README.md) — Documented together with bytes.strip.

The following methods on bytes and bytearray objects assume the use of ASCII
compatible binary formats and should not be applied to arbitrary binary data.
Note that all of the bytearray methods in this section do *not* operate in
place, and instead produce new objects.

- [`bytes.capitalize`](bytes.capitalize/README.md) — Return a copy of the sequence with each byte interpreted as an ASCII character, and the first byte capitalized and the rest lowercased.
- [`bytearray.capitalize`](bytearray.capitalize/README.md) — Documented together with bytes.capitalize.
- [`bytes.expandtabs`](bytes.expandtabs/README.md) — Return a copy of the sequence where all ASCII tab characters are replaced by one or more ASCII spaces, depending on the current column and the…
- [`bytearray.expandtabs`](bytearray.expandtabs/README.md) — Documented together with bytes.expandtabs.
- [`bytes.isalnum`](bytes.isalnum/README.md) — Return True if all bytes in the sequence are alphabetical ASCII characters or ASCII decimal digits and the sequence is not empty, False otherwise.
- [`bytearray.isalnum`](bytearray.isalnum/README.md) — Documented together with bytes.isalnum.
- [`bytes.isalpha`](bytes.isalpha/README.md) — Return True if all bytes in the sequence are alphabetic ASCII characters and the sequence is not empty, False otherwise.
- [`bytearray.isalpha`](bytearray.isalpha/README.md) — Documented together with bytes.isalpha.
- [`bytes.isascii`](bytes.isascii/README.md) — Return True if the sequence is empty or all bytes in the sequence are ASCII, False otherwise.
- [`bytearray.isascii`](bytearray.isascii/README.md) — Documented together with bytes.isascii.
- [`bytes.isdigit`](bytes.isdigit/README.md) — Return True if all bytes in the sequence are ASCII decimal digits and the sequence is not empty, False otherwise.
- [`bytearray.isdigit`](bytearray.isdigit/README.md) — Documented together with bytes.isdigit.
- [`bytes.islower`](bytes.islower/README.md) — Return True if there is at least one lowercase ASCII character in the sequence and no uppercase ASCII characters, False otherwise.
- [`bytearray.islower`](bytearray.islower/README.md) — Documented together with bytes.islower.
- [`bytes.isspace`](bytes.isspace/README.md) — Return True if all bytes in the sequence are ASCII whitespace and the sequence is not empty, False otherwise.
- [`bytearray.isspace`](bytearray.isspace/README.md) — Documented together with bytes.isspace.
- [`bytes.istitle`](bytes.istitle/README.md) — Return True if the sequence is ASCII titlecase and the sequence is not empty, False otherwise.
- [`bytearray.istitle`](bytearray.istitle/README.md) — Documented together with bytes.istitle.
- [`bytes.isupper`](bytes.isupper/README.md) — Return True if there is at least one uppercase alphabetic ASCII character in the sequence and no lowercase ASCII characters, False otherwise.
- [`bytearray.isupper`](bytearray.isupper/README.md) — Documented together with bytes.isupper.
- [`bytes.lower`](bytes.lower/README.md) — Return a copy of the sequence with all the uppercase ASCII characters converted to their corresponding lowercase counterpart.
- [`bytearray.lower`](bytearray.lower/README.md) — Documented together with bytes.lower.
- [`bytes.splitlines`](bytes.splitlines/README.md) — Return a list of the lines in the binary sequence, breaking at ASCII line boundaries.
- [`bytearray.splitlines`](bytearray.splitlines/README.md) — Documented together with bytes.splitlines.
- [`bytes.swapcase`](bytes.swapcase/README.md) — Return a copy of the sequence with all the lowercase ASCII characters converted to their corresponding uppercase counterpart and vice-versa.
- [`bytearray.swapcase`](bytearray.swapcase/README.md) — Documented together with bytes.swapcase.
- [`bytes.title`](bytes.title/README.md) — Return a titlecased version of the binary sequence where words start with an uppercase ASCII character and the remaining characters are lowercase.
- [`bytearray.title`](bytearray.title/README.md) — Documented together with bytes.title.
- [`bytes.upper`](bytes.upper/README.md) — Return a copy of the sequence with all the lowercase ASCII characters converted to their corresponding uppercase counterpart.
- [`bytearray.upper`](bytearray.upper/README.md) — Documented together with bytes.upper.
- [`bytes.zfill`](bytes.zfill/README.md) — Return a copy of the sequence left filled with ASCII b'0' digits to make a sequence of length *width*.
- [`bytearray.zfill`](bytearray.zfill/README.md) — Documented together with bytes.zfill.

## ``printf``-style Bytes Formatting

> **Note**
>
> The formatting operations described here exhibit a variety of quirks that
> lead to a number of common errors (such as failing to display tuples and
> dictionaries correctly).  If the value being printed may be a tuple or
> dictionary, wrap it in a tuple.

Bytes objects (`bytes`/`bytearray`) have one unique built-in operation:
the `%` operator (modulo).
This is also known as the bytes *formatting* or *interpolation* operator.
Given `format % values` (where *format* is a bytes object), `%` conversion
specifications in *format* are replaced with zero or more elements of *values*.
The effect is similar to using the `sprintf` function in the C language.

If *format* requires a single argument, *values* may be a single non-tuple
object. [^1]  Otherwise, *values* must be a tuple with exactly the number of
items specified by the format bytes object, or a single mapping object (for
example, a dictionary).

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
formats in the bytes object *must* include a parenthesised mapping key into that
dictionary inserted immediately after the `'%'` character. The mapping key
selects the value to be formatted from the mapping.  For example:

``` python
>>> print(b'%(language)s has %(number)03d quote types.' %
...       {b'language': b"Python", b"number": 2})
b'Python has 002 quote types.'
```
> Code: [example_01.py](example_01.py)

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
| `'u'` | Obsolete type -- it is identical to `'d'`. | (8) |
| `'x'` | Signed hexadecimal (lowercase). | (2) |
| `'X'` | Signed hexadecimal (uppercase). | (2) |
| `'e'` | Floating-point exponential format (lowercase). | (3) |
| `'E'` | Floating-point exponential format (uppercase). | (3) |
| `'f'` | Floating-point decimal format. | (3) |
| `'F'` | Floating-point decimal format. | (3) |
| `'g'` | Floating-point format. Uses lowercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise. | (4) |
| `'G'` | Floating-point format. Uses uppercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise. | (4) |
| `'c'` | Single byte (accepts integer or single byte objects). |  |
| `'b'` | Bytes (any object that follows the [buffer protocol](https://docs.python.org/3.15/c-api/buffer.html#bufferobjects) or has [__bytes__()](https://docs.python.org/3.15/reference/datamodel.html#object.__bytes__)). | (5) |
| `'s'` | `'s'` is an alias for `'b'` and should only be used for Python2/3 code bases. | (6) |
| `'a'` | Bytes (converts any Python object using `repr(obj).encode('ascii', 'backslashreplace')`). | (5) |
| `'r'` | `'r'` is an alias for `'a'` and should only be used for Python2/3 code bases. | (7) |
| `'%'` | No argument is converted, results in a `'%'` character in the result. |  |

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

6. `b'%s'` is deprecated, but will not be removed during the 3.x series.

7. `b'%r'` is deprecated, but will not be removed during the 3.x series.

8. See [PEP 237](https://peps.python.org/pep-237/).

> **Note**
>
> The bytearray version of this method does *not* operate in place - it
> always produces a new object, even if no changes were made.

> **See also**
>
> [PEP 461](https://peps.python.org/pep-461/) - Adding % formatting to bytes and bytearray

> *Added in version 3.5.*

## Memory Views

[memoryview](memoryview/README.md) objects allow Python code to access the internal data
of an object that supports the [buffer protocol](https://docs.python.org/3.15/c-api/buffer.html#bufferobjects) without
copying.

- [`memoryview`](memoryview/README.md) — Create a memoryview that references *object*.

For information on the thread safety of [memoryview](memoryview/README.md) objects in
the [free-threaded build](https://docs.python.org/3.15/glossary.html#term-free-threaded-build), see [Thread safety for memoryview objects](https://docs.python.org/3.15/builtins/threadsafety.html#thread-safety-memoryview).

[^1]: To format only a tuple you should therefore provide a singleton tuple whose only element is the tuple to be formatted.
