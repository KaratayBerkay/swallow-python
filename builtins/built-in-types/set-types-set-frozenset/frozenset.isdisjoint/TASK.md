# Görev b:2.11.5: frozenset.isdisjoint davranışını ayırt et

## Önce

[b:2.11](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ortak öğe yokluğu boş kümeyi de kapsar

```python
{1,2}.isdisjoint([2,3])
set().isdisjoint({1})
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `False`; `True`.
- [ ] Ortak öğe yokluğu boş kümeyi de kapsar

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
