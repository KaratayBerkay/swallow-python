# Görev b:2.10: binary-sequence-types-bytes-bytearray-memoryview davranışını ayırt et

## Önce

[b:2](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; binary indeks tamsayı verir; dilim binary dizidir

```python
b"AB"[0:1]
bytes([0,255])
bytes([256])
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b'A'`; `b'\x00\xff'`; `ValueError`.
- [ ] Binary indeks tamsayı verir; dilim binary dizidir

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
