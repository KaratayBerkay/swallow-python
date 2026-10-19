# Görev b:2.10.54: bytes.expandtabs davranışını ayırt et

## Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; tab sabit sayıda boşluk değil sonraki tab durağına ilerlemedir

```python
b'ab\tc'.expandtabs(4)
b'abcd\tx'.expandtabs(4)
b'a\nb\tc'.expandtabs(4)
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b'ab  c'`; `b'abcd    x'`; `b'a\nb   c'`.
- [ ] ASCII bayt kurallarıyla çalış; tab sabit sayıda boşluk değil sonraki tab durağına ilerlemedir
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
