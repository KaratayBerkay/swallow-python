## `frozenset.issuperset`

```
frozenset.issuperset(other, /)
set.issuperset(other, /)
```

## Çözümlü kısa örnek

Üst küme ilişkisini argüman sırasıyla bağla

```python
print(repr({1,2}.issuperset({1})))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.11.9: frozenset.issuperset davranışını ayırt et**

#### Önce

[b:2.11](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; üst küme ilişkisini argüman sırasıyla bağla

```python
{1,2}.issuperset([1,2])
{1}.issuperset({1,2})
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `False`.
- [ ] Üst küme ilişkisini argüman sırasıyla bağla

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../frozenset.union/README.md)
<!-- learning-task:end -->
