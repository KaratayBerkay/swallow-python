# Görev b:2.10.26: bytes.rfind davranışını ayırt et

## Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; sağdaki eşleşmenin özgün indeksi döner; bulunamazsa -1

```python
b'ababa'.rfind(b'ba',0,4)
b'abc'.rfind(b'x')
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `1`; `-1`.
- [ ] ASCII bayt kurallarıyla çalış; sağdaki eşleşmenin özgün indeksi döner; bulunamazsa -1
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
