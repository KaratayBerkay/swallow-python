# Görev b:3.57: repr davranışını ayırt et

## Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; temsil kaçışlarını gerçek satır sonuyla karıştırma.

```python
repr("a\nb")
str("a\nb")==repr("a\nb")
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `"'a\\nb'"`; `False`.
- [ ] Temsil kaçışlarını gerçek satır sonuyla karıştırma.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
