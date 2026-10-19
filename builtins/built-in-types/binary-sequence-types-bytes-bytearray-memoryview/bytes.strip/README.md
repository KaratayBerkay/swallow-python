## `bytes.strip`

```
bytes.strip(bytes=None, /)
bytearray.strip(bytes=None, /)
```

Return a copy of the sequence with specified leading and trailing bytes
removed. The *bytes* argument is a binary sequence specifying the set of
byte values to be removed.  If omitted or `None`, the *bytes*
argument defaults to removing [ASCII whitespace](../bytes.isspace/README.md).
The *bytes* argument is
not a prefix or suffix; rather, all combinations of its values are
stripped:

``` python
>>> b'   spacious   '.strip()
b'spacious'
>>> b'www.example.com'.strip(b'cmowz.')
b'example'
```
> Code: [example_01.py](example_01.py)

The binary sequence of byte values to remove may be any
[bytes-like object](https://docs.python.org/3.15/glossary.html#term-bytes-like-object).

> **Note**
>
> The bytearray version of this method does *not* operate in place -
> it always produces a new object, even if no changes were made.

## Çözümlü kısa örnek

ASCII bayt kurallarıyla çalış; chars önek/son ek değil karakter kümesidir; ortadaki karakter korunur

```python
print(repr(b' a '.strip()))
# Sonuç: b'a'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.50: bytes.strip davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; chars önek/son ek değil karakter kümesidir; ortadaki karakter korunur

```python
b'abbaXba'.strip(b'ab')
b'abXabYab'.strip(b'ab')
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b'X'`; `b'XabY'`.
- [ ] ASCII bayt kurallarıyla çalış; chars önek/son ek değil karakter kümesidir; ortadaki karakter korunur
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytes.capitalize/README.md)
<!-- learning-task:end -->
