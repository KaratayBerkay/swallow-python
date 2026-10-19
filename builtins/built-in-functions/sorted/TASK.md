# Görev b:3.64: sorted davranışını ayırt et

## Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; yeni liste üretimini, stabil sıralamayı ve kaynağın korunmasını açıkla.

```python
sorted([("a",2),("b",1),("c",2)],key=lambda x:x[1])
sorted([1,"x"])
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `[('b', 1), ('a', 2), ('c', 2)]`; `TypeError`.
- [ ] Yeni liste üretimini, stabil sıralamayı ve kaynağın korunmasını açıkla.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
