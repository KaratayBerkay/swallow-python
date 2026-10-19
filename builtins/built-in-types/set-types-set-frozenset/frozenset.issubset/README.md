## `frozenset.issubset`

```
frozenset.issubset(other, /)
set.issubset(other, /)
```

## Çözümlü kısa örnek

Alt küme eşit kümeyi de kapsar

```python
print(repr({1}.issubset({1,2})))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.11.7: frozenset.issubset davranışını ayırt et**

#### Önce

[b:2.11](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; alt küme eşit kümeyi de kapsar

```python
{1,2}.issubset([1,2])
{1,3}.issubset({1,2})
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `False`.
- [ ] Alt küme eşit kümeyi de kapsar

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../frozenset.issuperset/README.md)
<!-- learning-task:end -->
