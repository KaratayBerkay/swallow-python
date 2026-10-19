# Görev b:2.4.10: float.hex davranışını ayırt et

## Önce

[b:2.4](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; hex gösterim saklanan değerin kayıpsız gösterimidir

```python
(-2.25).hex()
float.fromhex((0.1).hex())==0.1
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `'-0x1.2000000000000p+1'`; `True`.
- [ ] Hex gösterim saklanan değerin kayıpsız gösterimidir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
