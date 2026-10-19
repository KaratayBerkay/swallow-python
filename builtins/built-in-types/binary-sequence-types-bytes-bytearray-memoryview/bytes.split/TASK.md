# Görev b:2.10.48: bytes.split davranışını ayırt et

## Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; sep verilmezse boşluklar birleşir; açık sep boş alanları korur

```python
b'  a  b  '.split()
b'a,,b,'.split(b',')
b''.split()
b''.split(b',')
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `[b'a', b'b']`; `[b'a', b'', b'b', b'']`; `[]`; `[b'']`.
- [ ] ASCII bayt kurallarıyla çalış; sep verilmezse boşluklar birleşir; açık sep boş alanları korur
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
