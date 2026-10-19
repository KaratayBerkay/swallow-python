## `frozenset.union`

```
frozenset.union(*others)
set.union(*others)
```

## Çözümlü kısa örnek

Bütün girdilerden tekrarsız üyeleri al

```python
print(repr(sorted({1}.union({2}))))
# Sonuç: [1, 2]
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.11.11: frozenset.union davranışını ayırt et**

#### Önce

[b:2.11](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; bütün girdilerden tekrarsız üyeleri al

```python
sorted({1,2}.union([2,3],[4]))
sorted(set().union([]))
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `[1, 2, 3, 4]`; `[]`.
- [ ] Bütün girdilerden tekrarsız üyeleri al

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../frozenset.intersection/README.md)
<!-- learning-task:end -->
