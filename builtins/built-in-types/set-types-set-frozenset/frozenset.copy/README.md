## `frozenset.copy`

```
frozenset.copy()
set.copy()
```

Return a shallow copy of the set.

## Çözümlü kısa örnek

Kopya eşit üyeler taşır; frozenset kopyası aynı nesne olabilir

```python
s=frozenset({1,2})
print(repr(frozenset({1,2}).copy()==frozenset({1,2})))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.11.19: frozenset.copy davranışını ayırt et**

#### Önce

[b:2.11](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; kopya eşit üyeler taşır; frozenset kopyası aynı nesne olabilir

```python
s=frozenset({1,2})
s.copy() is s
{1,2}.copy()=={2,1}
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `True`.
- [ ] Kopya eşit üyeler taşır; frozenset kopyası aynı nesne olabilir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../set.update/README.md)
<!-- learning-task:end -->
