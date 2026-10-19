# Görev b:3.72: zip davranışını ayırt et

## Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; varsayılan kısa girdide durma ile strict tüketim hatasını ayır.

```python
list(zip([1,2],["a"]))
list(zip([1,2],["a"],strict=True))
list(zip())
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `[(1, 'a')]`; `ValueError`; `[]`.
- [ ] Varsayılan kısa girdide durma ile strict tüketim hatasını ayır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
