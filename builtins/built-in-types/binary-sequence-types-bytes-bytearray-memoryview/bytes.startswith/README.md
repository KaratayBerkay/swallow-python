## `bytes.startswith`

```
bytes.startswith(prefix[, start[, end]])
bytearray.startswith(prefix[, start[, end]])
```

Return `True` if the binary data starts with the specified *prefix*,
otherwise return `False`.  *prefix* can also be a tuple of prefixes to
look for.  With optional *start*, test beginning at that position.  With
optional *end*, stop comparing at that position.

The prefix(es) to search for may be any [bytes-like object](https://docs.python.org/3.15/glossary.html#term-bytes-like-object).

## Çözümlü kısa örnek

ASCII bayt kurallarıyla çalış; tuple seçenekleriyle başlangıç dilimini ayır

```python
print(repr(b'ad.py'.startswith(b'ad')))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.32: bytes.startswith davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; tuple seçenekleriyle başlangıç dilimini ayır

```python
b'ad.py'.startswith((b'x',b'ad'))
b'xxad'.startswith(b'ad',2)
b'abc'.startswith(b'z')
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `True`; `False`.
- [ ] ASCII bayt kurallarıyla çalış; tuple seçenekleriyle başlangıç dilimini ayır
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytes.translate/README.md)
<!-- learning-task:end -->
