## `str`

```
str(*, encoding='utf-8', errors='strict')
str(object)
str(object, encoding, errors='strict')
str(object, *, errors)
```

Return a [string](https://docs.python.org/3.15/builtins/stdtypes.html#textseq) version of *object*.  If *object* is not
provided, returns the empty string.  Otherwise, the behavior of `str()`
depends on whether *encoding* or *errors* is given, as follows.

If neither *encoding* nor *errors* is given, `str(object)` returns
[type(object).__str__(object)](https://docs.python.org/3.15/reference/datamodel.html#object.__str__),
which is the "informal" or nicely
printable string representation of *object*.  For string objects, this is
the string itself.  If *object* does not have a [__str__()](https://docs.python.org/3.15/reference/datamodel.html#object.__str__)
method, then [str()](../../../built-in-functions/str/README.md) falls back to returning
[repr(object)](../../../built-in-functions/repr/README.md).

If at least one of *encoding* or *errors* is given, *object* should be a
[bytes-like object](https://docs.python.org/3.15/glossary.html#term-bytes-like-object) (e.g. [bytes](../../binary-sequence-types-bytes-bytearray-memoryview/bytes/README.md) or [bytearray](../../binary-sequence-types-bytes-bytearray-memoryview/bytearray/README.md)).  In
this case, if *object* is a [bytes](../../binary-sequence-types-bytes-bytearray-memoryview/bytes/README.md) (or [bytearray](../../binary-sequence-types-bytes-bytearray-memoryview/bytearray/README.md)) object,
then `str(bytes, encoding, errors)` is equivalent to
[bytes.decode(encoding, errors)](../../binary-sequence-types-bytes-bytearray-memoryview/bytes.decode/README.md).  Otherwise, the bytes
object underlying the buffer object is obtained before calling
[bytes.decode()](../../binary-sequence-types-bytes-bytearray-memoryview/bytes.decode/README.md).  See [Binary Sequence Types — bytes, bytearray, memoryview](https://docs.python.org/3.15/builtins/stdtypes.html#binaryseq) and
[Buffer Protocol](https://docs.python.org/3.15/c-api/buffer.html#bufferobjects) for information on buffer objects.

Passing a [bytes](../../binary-sequence-types-bytes-bytearray-memoryview/bytes/README.md) object to [str()](../../../built-in-functions/str/README.md) without the *encoding*
or *errors* arguments falls under the first case of returning the informal
string representation (see also the [-b](https://docs.python.org/3.15/using/cmdline.html#cmdoption-b) command-line option to
Python).  For example:

``` python
>>> str(b'Zoot!')
"b'Zoot!'"
```
> Code: [example_01.py](example_01.py)

For more information on the `str` class and its methods, see
[Text Sequence Type — str](https://docs.python.org/3.15/builtins/stdtypes.html#textseq) and the [String Methods](https://docs.python.org/3.15/builtins/stdtypes.html#string-methods) section below.  To output
formatted strings, see the [f-strings](https://docs.python.org/3.15/reference/lexical_analysis.html#f-strings) and [Format string syntax](https://docs.python.org/3.15/library/string.html#formatstrings)
sections.  In addition, see the [Text Processing Services](https://docs.python.org/3.15/library/text.html#stringservices) section.

## Çözümlü kısa örnek

Nesne temsilini bayt çözümlemeyle karıştırma

```python
print(repr(str(12)))
# Sonuç: '12'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.1: str davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; nesne temsilini bayt çözümlemeyle karıştırma

```python
str(b"ab")
str(b"ab","utf-8")
str(b"\xff","utf-8")
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `"b'ab'"`; `'ab'`; `UnicodeDecodeError`.
- [ ] Nesne temsilini bayt çözümlemeyle karıştırma

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.join/README.md)
<!-- learning-task:end -->
