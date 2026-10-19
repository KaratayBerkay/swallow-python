## `bytes.rstrip`

```
bytes.rstrip(bytes=None, /)
bytearray.rstrip(bytes=None, /)
```

Return a copy of the sequence with specified trailing bytes removed.  The
*bytes* argument is a binary sequence specifying the set of byte values to
be removed.  If omitted or `None`, the *bytes* argument defaults to
removing [ASCII whitespace](../bytes.isspace/README.md).
The *bytes* argument is not a suffix; rather,
all combinations of its values are stripped:

``` python
>>> b'   spacious   '.rstrip()
b'   spacious'
>>> b'mississippi'.rstrip(b'ipz')
b'mississ'
```
> Code: [example_01.py](example_01.py)

The binary sequence of byte values to remove may be any
[bytes-like object](https://docs.python.org/3.15/glossary.html#term-bytes-like-object). See [removesuffix()](../bytes.removesuffix/README.md) for a method
that will remove a single suffix string rather than all of a set of
characters.  For example:

``` python
>>> b'Monty Python'.rstrip(b' Python')
b'M'
>>> b'Monty Python'.removesuffix(b' Python')
b'Monty'
```
> Code: [example_02.py](example_02.py)

> **Note**
>
> The bytearray version of this method does *not* operate in place -
> it always produces a new object, even if no changes were made.

## Çözümlü kısa örnek

ASCII bayt kurallarıyla çalış; chars tek bir son ek değil karakter kümesidir

```python
print(repr(b' a  '.rstrip()))
# Sonuç: b' a'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.46: bytes.rstrip davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; chars tek bir son ek değil karakter kümesidir

```python
b'abXabba'.rstrip(b'ab')
b'abXba'.rstrip(b'ab')
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b'abX'`; `b'abX'`.
- [ ] ASCII bayt kurallarıyla çalış; chars tek bir son ek değil karakter kümesidir
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytes.split/README.md)
<!-- learning-task:end -->
