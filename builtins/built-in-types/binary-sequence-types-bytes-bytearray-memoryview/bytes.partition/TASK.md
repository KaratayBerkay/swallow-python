# Görev b:2.10.22: bytes.partition davranışını ayırt et

## Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; i̇lk eşleşmede üç parça döner; bulunmama sabit üçlüdür

```python
b'a=b=c'.partition(b'=')
b'abc'.partition(b'=')
b'abc'.partition(b'')
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `(b'a', b'=', b'b=c')`; `(b'abc', b'', b'')`; `ValueError`.
- [ ] ASCII bayt kurallarıyla çalış; i̇lk eşleşmede üç parça döner; bulunmama sabit üçlüdür
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
