# Görev b:2.10.60: bytes.isascii davranışını ayırt et

## Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; ASCII sınırı ile boş girdinin özel sonucunu göster

```python
b"".isascii()
b"\xff".isascii()
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `False`.
- [ ] ASCII bayt kurallarıyla çalış; ASCII sınırı ile boş girdinin özel sonucunu göster
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
