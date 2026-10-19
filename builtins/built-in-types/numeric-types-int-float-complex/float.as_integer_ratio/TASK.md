# Görev b:2.4.8: float.as_integer_ratio davranışını ayırt et

## Önce

[b:2.4](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; oran saklanan floatı tam ifade eder; özel değerler hata verir

```python
(-1.25).as_integer_ratio()
float("inf").as_integer_ratio()
float("nan").as_integer_ratio()
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `(-5, 4)`; `OverflowError`; `ValueError`.
- [ ] Oran saklanan floatı tam ifade eder; özel değerler hata verir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
