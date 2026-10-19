## `frozenset.isdisjoint`

```
frozenset.isdisjoint(other, /)
set.isdisjoint(other, /)
```

Return `True` if the set has no elements in common with *other*.  Sets are
disjoint if and only if their intersection is the empty set.

## Çözümlü kısa örnek

Ortak öğe yokluğu boş kümeyi de kapsar

```python
print(repr({1}.isdisjoint({2})))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.11.5: frozenset.isdisjoint davranışını ayırt et**

#### Önce

[b:2.11](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ortak öğe yokluğu boş kümeyi de kapsar

```python
{1,2}.isdisjoint([2,3])
set().isdisjoint({1})
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `False`; `True`.
- [ ] Ortak öğe yokluğu boş kümeyi de kapsar

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../frozenset.issubset/README.md)
<!-- learning-task:end -->
