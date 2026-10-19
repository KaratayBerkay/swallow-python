# Görev b:2.7.3: range davranışını ayırt et

## Önce

[b:2.7](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; range uç sınırı dışlar; negatif adım ve boş aralık kuralları geçerlidir

```python
list(range(6,0,-2))
list(range(1,1))
range(0,3,0)
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `[6, 4, 2]`; `[]`; `ValueError`.
- [ ] Range uç sınırı dışlar; negatif adım ve boş aralık kuralları geçerlidir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
