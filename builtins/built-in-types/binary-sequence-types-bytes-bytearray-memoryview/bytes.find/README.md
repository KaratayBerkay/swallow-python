## `bytes.find`

```
bytes.find(sub[, start[, end]])
bytearray.find(sub[, start[, end]])
```

Return the lowest index in the data where the subsequence *sub* is found,
such that *sub* is contained in the slice `s[start:end]`.  Optional
arguments *start* and *end* are interpreted as in slice notation.  Return
`-1` if *sub* is not found.

The subsequence to search for may be any [bytes-like object](https://docs.python.org/3.15/glossary.html#term-bytes-like-object) or an
integer in the range 0 to 255.

> **Note**
>
> The find() method should be used only if you need to know the
> position of *sub*.  To check if *sub* is a substring or not, use the
> `in` operator:
>
> ``` python
> >>> b'Py' in b'Python'
> True
> ```
> > Code: [example_01.py](example_01.py)

> *Changed in version 3.3:* Also accept an integer in the range 0 to 255 as the subsequence.

## Çözümlü kısa örnek

ASCII bayt kurallarıyla çalış; bulunamama -1 olur; bulunan indeks özgün metne aittir

```python
print(repr(b'ababa'.find(b'ba')))
# Sonuç: 1
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.14: bytes.find davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; bulunamama -1 olur; bulunan indeks özgün metne aittir

```python
b'ababa'.find(b'ba',2)
b'ababa'.find(b'x')
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `3`; `-1`.
- [ ] ASCII bayt kurallarıyla çalış; bulunamama -1 olur; bulunan indeks özgün metne aittir
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytes.index/README.md)
<!-- learning-task:end -->
