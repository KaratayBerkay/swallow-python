## `bytes`

```
bytes(source=b'')
bytes(source, encoding, errors='strict')
```

Firstly, the syntax for bytes literals is largely the same as that for string
literals, except that a `b` prefix is added:

- Single quotes: `b'still allows embedded "double" quotes'`

- Double quotes: `b"still allows embedded 'single' quotes"`

- Triple quoted: `b'''3 single quotes'''`, `b"""3 double quotes"""`

Only ASCII characters are permitted in bytes literals (regardless of the
declared source code encoding). Any binary values over 127 must be entered
into bytes literals using the appropriate escape sequence.

As with string literals, bytes literals may also use a `r` prefix to disable
processing of escape sequences. See [String and Bytes literals](https://docs.python.org/3.15/reference/lexical_analysis.html#strings) for more about the various
forms of bytes literal, including supported escape sequences.

While bytes literals and representations are based on ASCII text, bytes
objects actually behave like immutable sequences of integers, with each
value in the sequence restricted such that `0 <= x < 256` (attempts to
violate this restriction will trigger [ValueError](https://docs.python.org/3.15/builtins/exceptions.html#ValueError)). This is done
deliberately to emphasise that while many binary formats include ASCII based
elements and can be usefully manipulated with some text-oriented algorithms,
this is not generally the case for arbitrary binary data (blindly applying
text processing algorithms to binary data formats that are not ASCII
compatible will usually lead to data corruption).

In addition to the literal forms, bytes objects can be created in a number of
other ways:

- A zero-filled bytes object of a specified length: `bytes(10)`

- From an iterable of integers: `bytes(range(20))`

- Copying existing binary data via the buffer protocol:  `bytes(obj)`

Also see the [bytes](https://docs.python.org/3.15/builtins/functions.html#func-bytes) built-in.

Since 2 hexadecimal digits correspond precisely to a single byte, hexadecimal
numbers are a commonly used format for describing binary data. Accordingly,
the bytes type has an additional class method to read data in that format:

### fromhex(string,, /)

This bytes class method returns a bytes object, decoding the
given string object.  The string must contain two hexadecimal digits per
byte, with ASCII whitespace being ignored.

``` python
>>> bytes.fromhex('2Ef0 F1f2  ')
b'.\xf0\xf1\xf2'
```
> Code: [example_01.py](example_01.py)

> *Changed in version 3.7:* [bytes.fromhex()](https://docs.python.org/3.15/builtins/stdtypes.html#bytes.fromhex) now skips all ASCII whitespace in the string,
> not just spaces.

> *Changed in version 3.14:* [bytes.fromhex()](https://docs.python.org/3.15/builtins/stdtypes.html#bytes.fromhex) now accepts ASCII bytes and
> [bytes-like objects](https://docs.python.org/3.15/glossary.html#term-bytes-like-object) as input.

A reverse conversion function exists to transform a bytes object into its
hexadecimal representation.

### hex(*,, bytes_per_sep=1), hex(sep,, bytes_per_sep=1)

Return a string object containing two hexadecimal digits for each
byte in the instance.

``` python
>>> b'\xf0\xf1\xf2'.hex()
'f0f1f2'
```
> Code: [example_02.py](example_02.py)

If you want to make the hex string easier to read, you can specify a
single character separator *sep* parameter to include in the output.
By default, this separator will be included between each byte.
A second optional *bytes_per_sep* parameter controls the spacing.
Positive values calculate the separator position from the right,
negative values from the left.

``` python
>>> value = b'\xf0\xf1\xf2'
>>> value.hex('-')
'f0-f1-f2'
>>> value.hex('_', 2)
'f0_f1f2'
>>> b'UUDDLRLRAB'.hex(' ', -4)
'55554444 4c524c52 4142'
```
> Code: [example_03.py](example_03.py)

> *Added in version 3.5.*

> *Changed in version 3.8:* [bytes.hex()](https://docs.python.org/3.15/builtins/stdtypes.html#bytes.hex) now supports optional *sep* and *bytes_per_sep*
> parameters to insert separators between bytes in the hex output.

## Çözümlü kısa örnek

ASCII literal, hex dönüşüm ve değişmezliği bağla

```python
print(repr(b"A"[0]))
# Sonuç: 65
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.1: bytes davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII literal, hex dönüşüm ve değişmezliği bağla

```python
bytes.fromhex("41 42")
b"AB".hex()
b"AB"=="AB"
```

Fromhex ile boşluk içeren hex metni ve hatalı tek hex basamağını dene. Hex için ayırıcı ve bytes_per_sep seçeneğini kullan. Binary `%` biçimlendirmede ASCII sayıyla %b girdisini göster; Unicode metni doğrudan binary alana vermenin sınırını açıkla.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b'AB'`; `'4142'`; `False`.
- [ ] ASCII literal, hex dönüşüm ve değişmezliği bağla
- [ ] Hatalı hex ValueError; biçimlendirme sonucu bytes; bytes ile str kendiliğinden birbirine dönüşmez.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytearray/README.md)
<!-- learning-task:end -->
