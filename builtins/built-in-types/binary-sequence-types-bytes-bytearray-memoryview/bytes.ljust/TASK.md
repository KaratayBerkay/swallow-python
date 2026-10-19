# Görev b:2.10.38: bytes.ljust davranışını ayırt et

## Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; genişlik küçülünce metin kesilmez; dolgu sağa eklenir

```python
b'ab'.ljust(1,b'.')
b'ab'.ljust(4,b'..')
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b'ab'`; `TypeError`.
- [ ] ASCII bayt kurallarıyla çalış; genişlik küçülünce metin kesilmez; dolgu sağa eklenir
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
