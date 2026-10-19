## `bytes.rindex`

```
bytes.rindex(sub[, start[, end]])
bytearray.rindex(sub[, start[, end]])
```

Like [rfind()](../bytes.rfind/README.md) but raises [ValueError](https://docs.python.org/3.15/builtins/exceptions.html#ValueError) when the
subsequence *sub* is not found.

The subsequence to search for may be any [bytes-like object](https://docs.python.org/3.15/glossary.html#term-bytes-like-object) or an
integer in the range 0 to 255.

> *Changed in version 3.3:* Also accept an integer in the range 0 to 255 as the subsequence.

## Çözümlü kısa örnek

ASCII bayt kurallarıyla çalış; sağdan arama bulunamazsa ValueError verir

```python
print(repr(b'ababa'.rindex(b'ba')))
# Sonuç: 3
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.28: bytes.rindex davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; sağdan arama bulunamazsa ValueError verir

```python
b'ababa'.rindex(b'ba',0,4)
b'abc'.rindex(b'x')
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `1`; `ValueError`.
- [ ] ASCII bayt kurallarıyla çalış; sağdan arama bulunamazsa ValueError verir
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytes.rpartition/README.md)
<!-- learning-task:end -->
