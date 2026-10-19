# Görev b:2.10.24: bytes.replace davranışını ayırt et

## Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; count sınırı ve özgün metnin korunmasını açıkla

```python
b'aaaa'.replace(b'aa',b'x',1)
b'abc'.replace(b'z',b'x')
b'abc'.replace(b'a',b'x',0)
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b'xaa'`; `b'abc'`; `b'abc'`.
- [ ] ASCII bayt kurallarıyla çalış; count sınırı ve özgün metnin korunmasını açıkla
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
