# Görev b:2.10.50: bytes.strip davranışını ayırt et

## Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; chars önek/son ek değil karakter kümesidir; ortadaki karakter korunur

```python
b'abbaXba'.strip(b'ab')
b'abXabYab'.strip(b'ab')
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b'X'`; `b'XabY'`.
- [ ] ASCII bayt kurallarıyla çalış; chars önek/son ek değil karakter kümesidir; ortadaki karakter korunur
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
