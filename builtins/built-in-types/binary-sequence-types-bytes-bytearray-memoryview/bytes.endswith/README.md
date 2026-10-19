## `bytes.endswith`

```
bytes.endswith(suffix[, start[, end]])
bytearray.endswith(suffix[, start[, end]])
```

Return `True` if the binary data ends with the specified *suffix*,
otherwise return `False`.  *suffix* can also be a tuple of suffixes to
look for.  With optional *start*, test beginning at that position.  With
optional *end*, stop comparing at that position.

The suffix(es) to search for may be any [bytes-like object](https://docs.python.org/3.15/glossary.html#term-bytes-like-object).

## Çözümlü kısa örnek

ASCII bayt kurallarıyla çalış; tuple seçenekleri ve dilim sınırları son ek denetimini belirler

```python
print(repr(b'a.py'.endswith(b'.py')))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.12: bytes.endswith davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; tuple seçenekleri ve dilim sınırları son ek denetimini belirler

```python
b'a.txt'.endswith((b'.py',b'.txt'))
b'abXY'.endswith(b'b',0,2)
b'abc'.endswith(b'z')
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `True`; `False`.
- [ ] ASCII bayt kurallarıyla çalış; tuple seçenekleri ve dilim sınırları son ek denetimini belirler
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytes.find/README.md)
<!-- learning-task:end -->
