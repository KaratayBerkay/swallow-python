## `bytes.isascii`

```
bytes.isascii()
bytearray.isascii()
```

Return `True` if the sequence is empty or all bytes in the sequence are ASCII,
`False` otherwise.
ASCII bytes are in the range 0-0x7F.

> *Added in version 3.7.*

## Çözümlü kısa örnek

ASCII bayt kurallarıyla çalış; aSCII sınırı ile boş girdinin özel sonucunu göster

```python
print(repr(b"abc".isascii()))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.60: bytes.isascii davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; ASCII sınırı ile boş girdinin özel sonucunu göster

```python
b"".isascii()
b"\xff".isascii()
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `False`.
- [ ] ASCII bayt kurallarıyla çalış; ASCII sınırı ile boş girdinin özel sonucunu göster
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytes.isdigit/README.md)
<!-- learning-task:end -->
