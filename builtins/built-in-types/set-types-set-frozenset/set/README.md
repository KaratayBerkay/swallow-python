## `set`

```
set(iterable=(), /)
frozenset(iterable=(), /)
```

Return a new set or frozenset object whose elements are taken from
*iterable*.  The elements of a set must be [hashable](https://docs.python.org/3.15/glossary.html#term-hashable).  To
represent sets of sets, the inner sets must be frozenset
objects.  If *iterable* is not specified, a new empty set is
returned.

## Çözümlü kısa örnek

Küme öğeleri hashable olmalıdır; boş küme dict değildir

```python
print(repr(set() == set([])))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.11.1: set davranışını ayırt et**

#### Önce

[b:2.11](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; küme öğeleri hashable olmalıdır; boş küme dict değildir

```python
type({}) is set
{frozenset({1}),frozenset({2})}=={frozenset({2}),frozenset({1})}
set([[1]])
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `False`; `True`; `TypeError`.
- [ ] Küme öğeleri hashable olmalıdır; boş küme dict değildir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../set.add/README.md)
<!-- learning-task:end -->
