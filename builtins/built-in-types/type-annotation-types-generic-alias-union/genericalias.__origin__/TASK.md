# Görev b:2.14.2: genericalias.__origin__ davranışını ayırt et

## Önce

[b:2.14](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; origin parametresiz asıl sınıftır

```python
dict[str,int].__origin__ is dict
list[list[int]].__origin__ is list
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `True`.
- [ ] Origin parametresiz asıl sınıftır

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
