# Görev b:2.10.40: bytes.lstrip davranışını ayırt et

## Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; chars bir önek değil karakter kümesidir; yalnız solda çalışır

```python
b'abbaXba'.lstrip(b'ab')
b'abXab'.lstrip(b'ab')
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b'Xba'`; `b'Xab'`.
- [ ] ASCII bayt kurallarıyla çalış; chars bir önek değil karakter kümesidir; yalnız solda çalışır
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
