## `frozenset.symmetric_difference`

```
frozenset.symmetric_difference(other, /)
set.symmetric_difference(other, /)
```

## Çözümlü kısa örnek

Yalnız bir tarafta bulunan öğeler kalır

```python
print(repr(sorted({1,2}.symmetric_difference({2,3}))))
# Sonuç: [1, 3]
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.11.17: frozenset.symmetric_difference davranışını ayırt et**

#### Önce

[b:2.11](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; yalnız bir tarafta bulunan öğeler kalır

```python
sorted({1,2}.symmetric_difference([1,2]))
sorted(set().symmetric_difference({4}))
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `[]`; `[4]`.
- [ ] Yalnız bir tarafta bulunan öğeler kalır

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../frozenset.copy/README.md)
<!-- learning-task:end -->
