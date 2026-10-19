## `round()`

```
round(number, ndigits=None)
```

Return *number* rounded to *ndigits* precision after the decimal
point.  If *ndigits* is omitted or is `None`, it returns the
nearest integer to its input.

For the built-in types supporting round(), values are rounded to the
closest multiple of 10 to the power minus *ndigits*; if two multiples are
equally close, rounding is done toward the even choice (so, for example,
both `round(0.5)` and `round(-0.5)` are `0`, and `round(1.5)` is
`2`).  Any integer value is valid for *ndigits* (positive, zero, or
negative).  The return value is an integer if *ndigits* is omitted or
`None`.
Otherwise, the return value has the same type as *number*.

For a general Python object `number`, `round` delegates to
`number.__round__`.

> **Note**
>
> The behavior of round() for floats can be surprising: for example,
> `round(2.675, 2)` gives `2.67` instead of the expected `2.68`.
> This is not a bug: it's a result of the fact that most decimal fractions
> can't be represented exactly as a float.  See [Floating-Point Arithmetic:  Issues and Limitations](https://docs.python.org/3.15/tutorial/floatingpoint.html#tut-fp-issues) for
> more information.

## Çözümlü kısa örnek

Eşit uzaklıkta çift komşuya yuvarlamayı ve ikili temsil etkisini açıkla.

```python
print(repr(round(1.5)))
# Sonuç: 2
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.59: round davranışını ayırt et**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; eşit uzaklıkta çift komşuya yuvarlamayı ve ikili temsil etkisini açıkla.

```python
round(2.5)
round(-2.5)
round(2.675,2)
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `2`; `-2`; `2.67`.
- [ ] Eşit uzaklıkta çift komşuya yuvarlamayı ve ikili temsil etkisini açıkla.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../set/README.md)
<!-- learning-task:end -->
