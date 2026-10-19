# Görev b:2.10.44: bytes.rsplit davranışını ayırt et

## Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; maxsplit sağdaki ayrımları sınırlar; sonuç sırası ters dönmez

```python
b'a b c'.rsplit(None,1)
b'a,,b'.rsplit(b',',1)
b''.rsplit(b',')
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `[b'a b', b'c']`; `[b'a,', b'b']`; `[b'']`.
- [ ] ASCII bayt kurallarıyla çalış; maxsplit sağdaki ayrımları sınırlar; sonuç sırası ters dönmez
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
