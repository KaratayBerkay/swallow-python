## `bytes.rfind`

```
bytes.rfind(sub[, start[, end]])
bytearray.rfind(sub[, start[, end]])
```

Return the highest index in the sequence where the subsequence *sub* is
found, such that *sub* is contained within `s[start:end]`.  Optional
arguments *start* and *end* are interpreted as in slice notation. Return
`-1` on failure.

The subsequence to search for may be any [bytes-like object](https://docs.python.org/3.15/glossary.html#term-bytes-like-object) or an
integer in the range 0 to 255.

> *Changed in version 3.3:* Also accept an integer in the range 0 to 255 as the subsequence.

## Çözümlü kısa örnek

ASCII bayt kurallarıyla çalış; sağdaki eşleşmenin özgün indeksi döner; bulunamazsa -1

```python
print(repr(b'ababa'.rfind(b'ba')))
# Sonuç: 3
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.26: bytes.rfind davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; sağdaki eşleşmenin özgün indeksi döner; bulunamazsa -1

```python
b'ababa'.rfind(b'ba',0,4)
b'abc'.rfind(b'x')
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `1`; `-1`.
- [ ] ASCII bayt kurallarıyla çalış; sağdaki eşleşmenin özgün indeksi döner; bulunamazsa -1
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytes.rindex/README.md)
<!-- learning-task:end -->
