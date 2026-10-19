# Görev b:2.10.18: bytes.join davranışını ayırt et

## Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; ayırıcı öğeler arasına girer; öğeler metin olmalıdır

```python
b'|'.join([])
b'|'.join([b'a'])
b'|'.join([b'a',2])
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b''`; `b'a'`; `TypeError`.
- [ ] ASCII bayt kurallarıyla çalış; ayırıcı öğeler arasına girer; öğeler metin olmalıdır
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
