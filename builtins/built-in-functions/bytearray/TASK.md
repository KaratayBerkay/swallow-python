# Görev b:3.10: bytearray davranışını ayırt et

## Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; uzunlukla oluşturmayı verilen bayt değerleriyle oluşturmayla karıştırma.

```python
bytearray(3)
bytearray([0,255])
bytearray([256])
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `bytearray(b'\x00\x00\x00')`; `bytearray(b'\x00\xff')`; `ValueError`.
- [ ] Uzunlukla oluşturmayı verilen bayt değerleriyle oluşturmayla karıştırma.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
