# Görev b:2.10.76: bytes.swapcase davranışını ayırt et

## Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII case dönüşümü dışındaki baytlar korunur ve çift swapcase özgün veriyi verir.

```python
b"aB\xff".swapcase()
b"aB\xff".swapcase().swapcase()==b"aB\xff"
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b'Ab\xff'`; `True`.
- [ ] ASCII case dönüşümü dışındaki baytlar korunur ve çift swapcase özgün veriyi verir.
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
