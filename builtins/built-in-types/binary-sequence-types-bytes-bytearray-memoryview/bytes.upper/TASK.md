# Görev b:2.10.80: bytes.upper davranışını ayırt et

## Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; yalnız ASCII harfler büyür; bytearray sürümü de yeni nesne üretir.

```python
b"a\xff1!".upper()
bytearray(b"ada").upper()
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b'A\xff1!'`; `bytearray(b'ADA')`.
- [ ] Yalnız ASCII harfler büyür; bytearray sürümü de yeni nesne üretir.
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
