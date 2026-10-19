# Görev b:2.10.78: bytes.title davranışını ayırt et

## Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; dil bağımsız sözcük sınırları apostrofta da yeni başlık başlatabilir

```python
b"they're here".title()
b'a1b'.title()
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b"They'Re Here"`; `b'A1B'`.
- [ ] ASCII bayt kurallarıyla çalış; dil bağımsız sözcük sınırları apostrofta da yeni başlık başlatabilir
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
