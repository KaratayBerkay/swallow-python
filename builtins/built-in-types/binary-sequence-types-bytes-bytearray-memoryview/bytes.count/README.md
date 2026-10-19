## `bytes.count`

```
bytes.count(sub[, start[, end]])
bytearray.count(sub[, start[, end]])
```

Return the number of non-overlapping occurrences of subsequence *sub* in
the range [*start*, *end*].  Optional arguments *start* and *end* are
interpreted as in slice notation.

The subsequence to search for may be any [bytes-like object](https://docs.python.org/3.15/glossary.html#term-bytes-like-object) or an
integer in the range 0 to 255.

If *sub* is empty, returns the number of empty slices between characters
which is the length of the bytes object plus one.

> *Changed in version 3.3:* Also accept an integer in the range 0 to 255 as the subsequence.

## Çözümlü kısa örnek

ASCII bayt kurallarıyla çalış; örtüşen eşleşmeler sayılmaz; boş aranan metnin sınırlarını açıkla

```python
print(repr(b'aba'.count(b'a')))
# Sonuç: 2
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.4: bytes.count davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; örtüşen eşleşmeler sayılmaz; boş aranan metnin sınırlarını açıkla

```python
b'aaaa'.count(b'aa')
b'abc'.count(b'')
b'ababa'.count(b'a',1,4)
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `2`; `4`; `1`.
- [ ] ASCII bayt kurallarıyla çalış; örtüşen eşleşmeler sayılmaz; boş aranan metnin sınırlarını açıkla
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytes.removeprefix/README.md)
<!-- learning-task:end -->
