# Görev b:2.10.82: bytes.zfill davranışını ayırt et

## Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; sıfırlar işaretten sonra eklenir; kısa genişlik kesmez

```python
b'-7'.zfill(4)
b'+7'.zfill(4)
b'123'.zfill(2)
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b'-007'`; `b'+007'`; `b'123'`.
- [ ] ASCII bayt kurallarıyla çalış; sıfırlar işaretten sonra eklenir; kısa genişlik kesmez
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
