# Görev b:3.45: max davranışını ayırt et

## Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; boş iterable varsayılanıyla eşit anahtarlarda ilk karşılaşılma kuralını ayır.

```python
max([],default=0)
max(["aa","bb","c"],key=len)
max([])
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `0`; `'aa'`; `ValueError`.
- [ ] Boş iterable varsayılanıyla eşit anahtarlarda ilk karşılaşılma kuralını ayır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
