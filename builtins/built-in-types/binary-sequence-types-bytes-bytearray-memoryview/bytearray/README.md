## `bytearray`

```
bytearray(source=b'')
bytearray(source, encoding, errors='strict')
```

There is no dedicated literal syntax for bytearray objects, instead
they are always created by calling the constructor:

- Creating an empty instance: `bytearray()`

- Creating a zero-filled instance with a given length: `bytearray(10)`

- From an iterable of integers: `bytearray(range(20))`

- Copying existing binary data via the buffer protocol:  `bytearray(b'Hi!')`

As bytearray objects are mutable, they support the
[mutable](https://docs.python.org/3.15/builtins/stdtypes.html#typesseq-mutable) sequence operations in addition to the
common bytes and bytearray operations described in [Bytes and Bytearray Operations](https://docs.python.org/3.15/builtins/stdtypes.html#bytes-methods).

Also see the [bytearray](https://docs.python.org/3.15/builtins/functions.html#func-bytearray) built-in.

Since 2 hexadecimal digits correspond precisely to a single byte, hexadecimal
numbers are a commonly used format for describing binary data. Accordingly,
the bytearray type has an additional class method to read data in that format:

### fromhex(string,, /)

This bytearray class method returns a bytearray object, decoding
the given string object.  The string must contain two hexadecimal digits
per byte, with ASCII whitespace being ignored.

``` python
>>> bytearray.fromhex('2Ef0 F1f2  ')
bytearray(b'.\xf0\xf1\xf2')
```
> Code: [example_01.py](example_01.py)

> *Changed in version 3.7:* [bytearray.fromhex()](https://docs.python.org/3.15/builtins/stdtypes.html#bytearray.fromhex) now skips all ASCII whitespace in the string,
> not just spaces.

> *Changed in version 3.14:* [bytearray.fromhex()](https://docs.python.org/3.15/builtins/stdtypes.html#bytearray.fromhex) now accepts ASCII [bytes](../bytes/README.md) and
> [bytes-like objects](https://docs.python.org/3.15/glossary.html#term-bytes-like-object) as input.

A reverse conversion function exists to transform a bytearray object into its
hexadecimal representation.

### hex(*,, bytes_per_sep=1), hex(sep,, bytes_per_sep=1)

Return a string object containing two hexadecimal digits for each
byte in the instance.

``` python
>>> bytearray(b'\xf0\xf1\xf2').hex()
'f0f1f2'
```
> Code: [example_02.py](example_02.py)

> *Added in version 3.5.*

> *Changed in version 3.8:* Similar to [bytes.hex()](https://docs.python.org/3.15/builtins/stdtypes.html#bytes.hex), [bytearray.hex()](https://docs.python.org/3.15/builtins/stdtypes.html#bytearray.hex) now supports
> optional *sep* and *bytes_per_sep* parameters to insert separators
> between bytes in the hex output.

### resize(size,, /)

Resize the bytearray to contain *size* bytes. *size* must be
greater than or equal to 0.

If the bytearray needs to shrink, bytes beyond *size* are truncated.

If the bytearray needs to grow, all new bytes, those beyond *size*,
will be set to null bytes.

This is equivalent to:

``` python
>>> def resize(ba, size):
...     if len(ba) > size:
...         del ba[size:]
...     else:
...         ba += b'\0' * (size - len(ba))
```
> Code: [example_03.py](example_03.py)

Examples:

``` python
>>> shrink = bytearray(b'abc')
>>> shrink.resize(1)
>>> (shrink, len(shrink))
(bytearray(b'a'), 1)
>>> grow = bytearray(b'abc')
>>> grow.resize(5)
>>> (grow, len(grow))
(bytearray(b'abc\x00\x00'), 5)
```
> Code: [example_04.py](example_04.py)

> *Added in version 3.14.*

### take_bytes(n=None,, /)

Remove the first *n* bytes from the bytearray and return them as an immutable
[bytes](../bytes/README.md).
By default (if *n* is `None`), return all bytes and clear the bytearray.

If *n* is negative, index from the end and take the first [len()](../../../built-in-functions/len/README.md)
plus *n* bytes. If *n* is out of bounds, raise [IndexError](https://docs.python.org/3.15/builtins/exceptions.html#IndexError).

Taking less than the full length will leave remaining bytes in the
bytearray, which requires a copy. If the remaining bytes should be
discarded, use `resize()` or `del` to truncate
then `take_bytes()` without a size.

> **CPython implementation detail:** Taking all bytes is a zero-copy operation.

> *Added in version 3.15:* See the [What's New](https://docs.python.org/3.15/whatsnew/3.15.html#whatsnew315-bytearray-take-bytes) entry for
> common code patterns which can be optimized with
> [bytearray.take_bytes()](https://docs.python.org/3.15/builtins/stdtypes.html#bytearray.take_bytes).

## Çözümlü kısa örnek

Bytearray uzunluk, değer ve dönüştürme sözleşmelerini ayır

```python
print(repr(bytearray(2)))
# Sonuç: bytearray(b'\x00\x00')
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.2: bytearray davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

Sürüm: Python 3.15 veya üzeri. Daha eski yorumlayıcıda yalnız bu sürüme bağlı kısmı gerekçeli yazılı iz ile çözebilirsin; çalıştırma kanıtını bekleyen olarak kaydet.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; bytearray uzunluk, değer ve dönüştürme sözleşmelerini ayır

```python
bytearray([65,66])
bytes(bytearray(b"AB"))
bytearray([256])
```

Fromhex ve hex ile veriyi gidiş dönüş dönüştür. Python 3.14+ resize ile küçültmeyi ve sıfır baytlarla büyütmeyi göster. Python 3.15+ take_bytes için b"ABCD" üzerinde 2, -1, None ve sınır dışı n girdilerini yeni nesnelerde dene; dönüş bytes ile kalan bytearrayı kaydet.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `bytearray(b'AB')`; `b'AB'`; `ValueError`.
- [ ] Bytearray uzunluk, değer ve dönüştürme sözleşmelerini ayır
- [ ] Resize küçültmede sonu keser, büyütmede sıfır ekler; take_bytes(2) b"AB" alıp b"CD" bırakır, -1 ilk üç baytı alır, None hepsini alıp boşaltır; sınır dışı IndexError verir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../memoryview/README.md)
<!-- learning-task:end -->
