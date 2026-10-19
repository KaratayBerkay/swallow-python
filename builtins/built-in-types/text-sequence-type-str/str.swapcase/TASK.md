# Görev b:2.9.44: str.swapcase davranışını ayırt et

## Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; unicode case dönüşümü her zaman tersinir değildir

```python
"Groß".swapcase()
"ß".swapcase().swapcase()=="ß"
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `'gROSS'`; `False`.
- [ ] Unicode case dönüşümü her zaman tersinir değildir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
