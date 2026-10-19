## `float.as_integer_ratio`

```
float.as_integer_ratio()
```

Return a pair of integers whose ratio is exactly equal to the
original float. The ratio is in lowest terms and has a positive denominator.  Raises
[OverflowError](https://docs.python.org/3.15/builtins/exceptions.html#OverflowError) on infinities and a [ValueError](https://docs.python.org/3.15/builtins/exceptions.html#ValueError) on
NaNs.

## Çözümlü kısa örnek

Oran saklanan floatı tam ifade eder; özel değerler hata verir

```python
print(repr((0.5).as_integer_ratio()))
# Sonuç: (1, 2)
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.4.8: float.as_integer_ratio davranışını ayırt et**

#### Önce

[b:2.4](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; oran saklanan floatı tam ifade eder; özel değerler hata verir

```python
(-1.25).as_integer_ratio()
float("inf").as_integer_ratio()
float("nan").as_integer_ratio()
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `(-5, 4)`; `OverflowError`; `ValueError`.
- [ ] Oran saklanan floatı tam ifade eder; özel değerler hata verir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../float.is_integer/README.md)
<!-- learning-task:end -->
