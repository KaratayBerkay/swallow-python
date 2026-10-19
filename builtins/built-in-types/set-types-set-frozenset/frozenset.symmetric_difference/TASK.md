# Görev b:2.11.17: frozenset.symmetric_difference davranışını ayırt et

## Önce

[b:2.11](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; yalnız bir tarafta bulunan öğeler kalır

```python
sorted({1,2}.symmetric_difference([1,2]))
sorted(set().symmetric_difference({4}))
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `[]`; `[4]`.
- [ ] Yalnız bir tarafta bulunan öğeler kalır

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
