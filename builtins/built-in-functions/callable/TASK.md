# Görev b:3.12: callable davranışını ayırt et

## Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; çağrılabilir olma, her argümanla başarılı çağrı garantisi değildir.

```python
callable(7)
callable(lambda x:x)
(lambda x:x)()
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `False`; `True`; `TypeError`.
- [ ] Çağrılabilir olma, her argümanla başarılı çağrı garantisi değildir.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
