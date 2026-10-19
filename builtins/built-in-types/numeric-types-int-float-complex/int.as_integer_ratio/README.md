## `int.as_integer_ratio`

```
int.as_integer_ratio()
```

Return a pair of integers whose ratio is equal to the original
integer and has a positive denominator.  The integer ratio of integers
(whole numbers) is always the integer as the numerator and `1` as the
denominator.

> *Added in version 3.8.*

## Çözümlü kısa örnek

Tamsayının paydası birdir

```python
print(repr((4).as_integer_ratio()))
# Sonuç: (4, 1)
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.4.5: int.as_integer_ratio davranışını ayırt et**

#### Önce

[b:2.4](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; tamsayının paydası birdir

```python
(-7).as_integer_ratio()
(0).as_integer_ratio()
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `(-7, 1)`; `(0, 1)`.
- [ ] Tamsayının paydası birdir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../int.is_integer/README.md)
<!-- learning-task:end -->
