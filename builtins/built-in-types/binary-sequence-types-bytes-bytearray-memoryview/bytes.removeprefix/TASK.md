# Görev b:2.10.6: bytes.removeprefix davranışını ayırt et

## Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; yalnız tam bir önek kaldırılır; karakter kümesi gibi davranmaz

```python
b'ababa'.removeprefix(b'ab')
b'baX'.removeprefix(b'ab')
b'abc'.removeprefix(b'')
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b'aba'`; `b'baX'`; `b'abc'`.
- [ ] ASCII bayt kurallarıyla çalış; yalnız tam bir önek kaldırılır; karakter kümesi gibi davranmaz
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
