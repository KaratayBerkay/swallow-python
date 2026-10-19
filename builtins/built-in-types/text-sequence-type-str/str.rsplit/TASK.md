# Görev b:2.9.38: str.rsplit davranışını ayırt et

## Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; maxsplit sağdaki ayrımları sınırlar; sonuç sırası ters dönmez

```python
"a b c".rsplit(None,1)
"a,,b".rsplit(",",1)
"".rsplit(",")
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `['a b', 'c']`; `['a,', 'b']`; `['']`.
- [ ] Maxsplit sağdaki ayrımları sınırlar; sonuç sırası ters dönmez

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
