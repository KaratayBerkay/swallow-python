# Görev b:3.24: filter davranışını ayırt et

## Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; none filtresinde doğruluk sınanır; dönüş değeri iterator olduğundan tüketim ayrıdır.

```python
list(filter(None,[0,"",[],[0],2]))
list(filter(lambda x:x>2,[1,3,2,4]))
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `[[0], 2]`; `[3, 4]`.
- [ ] None filtresinde doğruluk sınanır; dönüş değeri iterator olduğundan tüketim ayrıdır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
