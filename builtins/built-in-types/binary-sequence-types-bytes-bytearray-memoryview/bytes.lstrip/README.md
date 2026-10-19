## `bytes.lstrip`

```
bytes.lstrip(bytes=None, /)
bytearray.lstrip(bytes=None, /)
```

Return a copy of the sequence with specified leading bytes removed.  The
*bytes* argument is a binary sequence specifying the set of byte values to
be removed.  If omitted or `None`, the *bytes* argument defaults
to removing [ASCII whitespace](../bytes.isspace/README.md).
The *bytes* argument is not a prefix;
rather, all combinations of its values are stripped:

``` python
>>> b'   spacious   '.lstrip()
b'spacious   '
>>> b'www.example.com'.lstrip(b'cmowz.')
b'example.com'
```
> Code: [example_01.py](example_01.py)

The binary sequence of byte values to remove may be any
[bytes-like object](https://docs.python.org/3.15/glossary.html#term-bytes-like-object). See [removeprefix()](../bytes.removeprefix/README.md) for a method
that will remove a single prefix string rather than all of a set of
characters.  For example:

``` python
>>> b'Arthur: three!'.lstrip(b'Arthur: ')
b'ee!'
>>> b'Arthur: three!'.removeprefix(b'Arthur: ')
b'three!'
```
> Code: [example_02.py](example_02.py)

> **Note**
>
> The bytearray version of this method does *not* operate in place -
> it always produces a new object, even if no changes were made.

## Çözümlü kısa örnek

ASCII bayt kurallarıyla çalış; chars bir önek değil karakter kümesidir; yalnız solda çalışır

```python
print(repr(b'  a  '.lstrip()))
# Sonuç: b'a  '
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.40: bytes.lstrip davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; chars bir önek değil karakter kümesidir; yalnız solda çalışır

```python
b'abbaXba'.lstrip(b'ab')
b'abXab'.lstrip(b'ab')
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b'Xba'`; `b'Xab'`.
- [ ] ASCII bayt kurallarıyla çalış; chars bir önek değil karakter kümesidir; yalnız solda çalışır
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytes.rjust/README.md)
<!-- learning-task:end -->
