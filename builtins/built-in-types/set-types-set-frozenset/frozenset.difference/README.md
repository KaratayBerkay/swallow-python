## `frozenset.difference`

```
frozenset.difference(*others)
set.difference(*others)
```

## Çözümlü kısa örnek

Solda olup diğerlerinde olmayan üyeleri seç

```python
print(repr(sorted({1,2,3}.difference({2}))))
# Sonuç: [1, 3]
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.11.15: frozenset.difference davranışını ayırt et**

#### Önce

[b:2.11](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; solda olup diğerlerinde olmayan üyeleri seç

```python
sorted({1,2,3}.difference([2],[3]))
sorted({1,2}.difference({1,2}))
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `[1]`; `[]`.
- [ ] Solda olup diğerlerinde olmayan üyeleri seç

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../frozenset.symmetric_difference/README.md)
<!-- learning-task:end -->
