# Görev b:2.10.8: bytes.removesuffix davranışını ayırt et

## Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; tam son ek yalnız bir kez kaldırılır; boş ek metni silmez

```python
b'ababa'.removesuffix(b'ba')
b'abc'.removesuffix(b'')
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b'aba'`; `b'abc'`.
- [ ] ASCII bayt kurallarıyla çalış; tam son ek yalnız bir kez kaldırılır; boş ek metni silmez
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
