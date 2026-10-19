# Görev b:2.10.32: bytes.startswith davranışını ayırt et

## Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; tuple seçenekleriyle başlangıç dilimini ayır

```python
b'ad.py'.startswith((b'x',b'ad'))
b'xxad'.startswith(b'ad',2)
b'abc'.startswith(b'z')
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `True`; `False`.
- [ ] ASCII bayt kurallarıyla çalış; tuple seçenekleriyle başlangıç dilimini ayır
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
