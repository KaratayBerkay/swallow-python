# Görev b:2.11.13: frozenset.intersection davranışını ayırt et

## Önce

[b:2.11](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ortak üyeleri seç; yöntem iterable da kabul eder

```python
sorted({1,2,3}.intersection([2,3],[3]))
sorted({1}.intersection({2}))
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `[3]`; `[]`.
- [ ] Ortak üyeleri seç; yöntem iterable da kabul eder

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
