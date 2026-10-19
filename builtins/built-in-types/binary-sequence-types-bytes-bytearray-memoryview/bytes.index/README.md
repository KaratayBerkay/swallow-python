## `bytes.index`

```
bytes.index(sub[, start[, end]])
bytearray.index(sub[, start[, end]])
```

Like [find()](../bytes.find/README.md), but raise [ValueError](https://docs.python.org/3.15/builtins/exceptions.html#ValueError) when the
subsequence is not found.

The subsequence to search for may be any [bytes-like object](https://docs.python.org/3.15/glossary.html#term-bytes-like-object) or an
integer in the range 0 to 255.

> *Changed in version 3.3:* Also accept an integer in the range 0 to 255 as the subsequence.

## Çözümlü kısa örnek

ASCII bayt kurallarıyla çalış; arama başarısızlığı ValueError verir; -1 ile karıştırma

```python
print(repr(b'ababa'.index(b'ba')))
# Sonuç: 1
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.16: bytes.index davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; arama başarısızlığı ValueError verir; -1 ile karıştırma

```python
b'ababa'.index(b'ba',2)
b'ababa'.index(b'x')
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `3`; `ValueError`.
- [ ] ASCII bayt kurallarıyla çalış; arama başarısızlığı ValueError verir; -1 ile karıştırma
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytes.join/README.md)
<!-- learning-task:end -->
