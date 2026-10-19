# Görev b:2.10.4: bytes.count davranışını ayırt et

## Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; örtüşen eşleşmeler sayılmaz; boş aranan metnin sınırlarını açıkla

```python
b'aaaa'.count(b'aa')
b'abc'.count(b'')
b'ababa'.count(b'a',1,4)
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `2`; `4`; `1`.
- [ ] ASCII bayt kurallarıyla çalış; örtüşen eşleşmeler sayılmaz; boş aranan metnin sınırlarını açıkla
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
