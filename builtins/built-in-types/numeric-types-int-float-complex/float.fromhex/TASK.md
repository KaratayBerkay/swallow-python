# Görev b:2.4.11: float.fromhex davranışını ayırt et

## Önce

[b:2.4](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; p sonrası üs iki tabanındadır

```python
float.fromhex("  -0x1p-1 ")
float.fromhex("gecersiz")
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `-0.5`; `ValueError`.
- [ ] p sonrası üs iki tabanındadır

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
