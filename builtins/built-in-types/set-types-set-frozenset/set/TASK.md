# Görev b:2.11.1: set davranışını ayırt et

## Önce

[b:2.11](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; küme öğeleri hashable olmalıdır; boş küme dict değildir

```python
type({}) is set
{frozenset({1}),frozenset({2})}=={frozenset({2}),frozenset({1})}
set([[1]])
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `False`; `True`; `TypeError`.
- [ ] Küme öğeleri hashable olmalıdır; boş küme dict değildir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
