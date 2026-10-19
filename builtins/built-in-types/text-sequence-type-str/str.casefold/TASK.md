# Görev b:2.9.5: str.casefold davranışını ayırt et

## Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; unicode casefold, lower ile aynı dönüşüm değildir

```python
"GROSS".casefold()
"Groß".casefold()
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `'gross'`; `'gross'`.
- [ ] Unicode casefold, lower ile aynı dönüşüm değildir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
