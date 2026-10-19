These are the Boolean operations, ordered by ascending priority:

| Operation | Result | Notes |
| --- | --- | --- |
| `x or y` | if *x* is true, then *x*, else *y* | (1) |
| `x and y` | if *x* is false, then *x*, else *y* | (2) |
| `not x` | if *x* is false, then `True`, else `False` | (3) |

Notes:

1. This is a short-circuit operator, so it only evaluates the second
   argument if the first one is false.

2. This is a short-circuit operator, so it only evaluates the second
   argument if the first one is true.

3. `not` has a lower priority than non-Boolean operators, so `not a == b` is
   interpreted as `not (a == b)`, and `a == not b` is a syntax error.

## Çözümlü kısa örnek

And/or operand döndürür; not bool döndürür

```python
print(repr(0 or 7))
# Sonuç: 7
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.2: boolean-operations-and-or-not davranışını ayırt et**

#### Önce

[b:2](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; and/or operand döndürür; not bool döndürür

```python
[] or "yedek"
"ad" and 9
not [0]
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `'yedek'`; `9`; `False`.
- [ ] And/or operand döndürür; not bool döndürür

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../comparisons/README.md)
<!-- learning-task:end -->
