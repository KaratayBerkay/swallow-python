# Görev b:3.28: frozenset davranışını ayırt et

## Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; tekrarların silinmesiyle sonradan değiştirilememe özelliğini ayır.

```python
frozenset([1,2])==frozenset([2,1])
frozenset([1]).add(2)
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `AttributeError`.
- [ ] Tekrarların silinmesiyle sonradan değiştirilememe özelliğini ayır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
