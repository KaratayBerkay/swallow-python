## `divmod()`

```
divmod(a, b, /)
```

Take two (non-complex) numbers as arguments and return a pair of numbers
consisting of their quotient and remainder when using integer division.  With
mixed operand types, the rules for binary arithmetic operators apply.  For
integers, the result is the same as `(a // b, a % b)`. For floating-point
numbers the result is `(q, a % b)`, where *q* is usually `math.floor(a /
b)` but may be 1 less than that.  In any case `q * b + a % b` is very
close to *a*, if `a % b` is non-zero it has the same sign as *b*, and `0
<= abs(a % b) < abs(b)`.

## Çözümlü kısa örnek

Negatif sayılarda bölüm aşağı yuvarlanır; bölüm ve kalan özgün sayıyı yeniden kurar.

```python
print(repr(divmod(9,4)))
# Sonuç: (2, 1)
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.20: divmod davranışını ayırt et**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; negatif sayılarda bölüm aşağı yuvarlanır; bölüm ve kalan özgün sayıyı yeniden kurar.

```python
divmod(-9,4)
divmod(9,0)
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `(-3, 3)`; `ZeroDivisionError`.
- [ ] Negatif sayılarda bölüm aşağı yuvarlanır; bölüm ve kalan özgün sayıyı yeniden kurar.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../enumerate/README.md)
<!-- learning-task:end -->
