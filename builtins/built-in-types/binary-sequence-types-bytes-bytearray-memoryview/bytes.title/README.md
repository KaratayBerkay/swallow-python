## `bytes.title`

```
bytes.title()
bytearray.title()
```

Return a titlecased version of the binary sequence where words start with
an uppercase ASCII character and the remaining characters are lowercase.
Uncased byte values are left unmodified.

For example:

``` python
>>> b'Hello world'.title()
b'Hello World'
```
> Code: [example_01.py](example_01.py)

Lowercase ASCII characters are those byte values in the sequence
`b'abcdefghijklmnopqrstuvwxyz'`. Uppercase ASCII characters
are those byte values in the sequence `b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`.
All other byte values are uncased.

The algorithm uses a simple language-independent definition of a word as
groups of consecutive letters.  The definition works in many contexts but
it means that apostrophes in contractions and possessives form word
boundaries, which may not be the desired result:

``` python
>>> b"they're bill's friends from the UK".title()
b"They'Re Bill'S Friends From The Uk"
```
> Code: [example_02.py](example_02.py)

A workaround for apostrophes can be constructed using regular expressions:

``` python
>>> import re
>>> def titlecase(s):
...     return re.sub(rb"[A-Za-z]+('[A-Za-z]+)?",
...                   lambda mo: mo.group(0)[0:1].upper() +
...                              mo.group(0)[1:].lower(),
...                   s)
...
>>> titlecase(b"they're bill's friends.")
b"They're Bill's Friends."
```
> Code: [example_03.py](example_03.py)

> **Note**
>
> The bytearray version of this method does *not* operate in place - it
> always produces a new object, even if no changes were made.

## Çözümlü kısa örnek

ASCII bayt kurallarıyla çalış; dil bağımsız sözcük sınırları apostrofta da yeni başlık başlatabilir

```python
print(repr(b'ada ece'.title()))
# Sonuç: b'Ada Ece'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.78: bytes.title davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; dil bağımsız sözcük sınırları apostrofta da yeni başlık başlatabilir

```python
b"they're here".title()
b'a1b'.title()
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b"They'Re Here"`; `b'A1B'`.
- [ ] ASCII bayt kurallarıyla çalış; dil bağımsız sözcük sınırları apostrofta da yeni başlık başlatabilir
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytes.upper/README.md)
<!-- learning-task:end -->
