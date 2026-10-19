# Görev b:3.11: bytes davranışını ayırt et

## Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; bytes değişmezdir; tamsayı uzunluk, iterable ise öğe değerleri verir.

```python
bytes(2)
bytes("İ", "utf-8")
bytes([256])
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b'\x00\x00'`; `b'\xc4\xb0'`; `ValueError`.
- [ ] Bytes değişmezdir; tamsayı uzunluk, iterable ise öğe değerleri verir.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
