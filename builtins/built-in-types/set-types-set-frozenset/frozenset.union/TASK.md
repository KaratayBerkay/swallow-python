# Görev b:2.11.11: frozenset.union davranışını ayırt et

## Önce

[b:2.11](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; bütün girdilerden tekrarsız üyeleri al

```python
sorted({1,2}.union([2,3],[4]))
sorted(set().union([]))
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `[1, 2, 3, 4]`; `[]`.
- [ ] Bütün girdilerden tekrarsız üyeleri al

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
