## `frozenset.intersection`

```
frozenset.intersection(*others)
set.intersection(*others)
```

## Çözümlü kısa örnek

Ortak üyeleri seç; yöntem iterable da kabul eder

```python
print(repr(sorted({1,2}.intersection({2,3}))))
# Sonuç: [2]
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.11.13: frozenset.intersection davranışını ayırt et**

#### Önce

[b:2.11](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ortak üyeleri seç; yöntem iterable da kabul eder

```python
sorted({1,2,3}.intersection([2,3],[3]))
sorted({1}.intersection({2}))
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `[3]`; `[]`.
- [ ] Ortak üyeleri seç; yöntem iterable da kabul eder

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../frozenset.difference/README.md)
<!-- learning-task:end -->
