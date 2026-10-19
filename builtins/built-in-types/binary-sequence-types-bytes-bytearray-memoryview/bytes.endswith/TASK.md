# Görev b:2.10.12: bytes.endswith davranışını ayırt et

## Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; tuple seçenekleri ve dilim sınırları son ek denetimini belirler

```python
b'a.txt'.endswith((b'.py',b'.txt'))
b'abXY'.endswith(b'b',0,2)
b'abc'.endswith(b'z')
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `True`; `False`.
- [ ] ASCII bayt kurallarıyla çalış; tuple seçenekleri ve dilim sınırları son ek denetimini belirler
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
