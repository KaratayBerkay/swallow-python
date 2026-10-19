## `range`

```
range(stop, /)
range(start, stop, step=1, /)
```

The arguments to the range constructor must be integers (either built-in
[int](../../../built-in-functions/int/README.md) or any object that implements the [__index__()](https://docs.python.org/3.15/reference/datamodel.html#object.__index__) special
method).  If the *step* argument is omitted, it defaults to `1`.
If the *start* argument is omitted, it defaults to `0`.
If *step* is zero, [ValueError](https://docs.python.org/3.15/builtins/exceptions.html#ValueError) is raised.

For a positive *step*, the contents of a range `r` are determined by the
formula `r[i] = start + step*i` where `i >= 0` and
`r[i] < stop`.

For a negative *step*, the contents of the range are still determined by
the formula `r[i] = start + step*i`, but the constraints are `i >= 0`
and `r[i] > stop`.

A range object will be empty if `r[0]` does not meet the value
constraint. Ranges do support negative indices, but these are interpreted
as indexing from the end of the sequence determined by the positive
indices.

Ranges containing absolute values larger than [sys.maxsize](https://docs.python.org/3.15/library/sys.html#sys.maxsize) are
permitted but some features (such as [len()](../../../built-in-functions/len/README.md)) may raise
[OverflowError](https://docs.python.org/3.15/builtins/exceptions.html#OverflowError).

Range examples:

``` python
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list(range(0, 30, 5))
[0, 5, 10, 15, 20, 25]
>>> list(range(0, 10, 3))
[0, 3, 6, 9]
>>> list(range(0, -10, -1))
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
>>> list(range(0))
[]
>>> list(range(1, 0))
[]
```
> Code: [example_01.py](example_01.py)

Ranges implement all of the [common](https://docs.python.org/3.15/builtins/stdtypes.html#typesseq-common) sequence operations
except concatenation and repetition (due to the fact that range objects can
only represent sequences that follow a strict pattern and repetition and
concatenation will usually violate that pattern).

### start

The value of the *start* parameter (or `0` if the parameter was
not supplied)

### stop

The value of the *stop* parameter

### step

The value of the *step* parameter (or `1` if the parameter was
not supplied)

## Çözümlü kısa örnek

Range uç sınırı dışlar; negatif adım ve boş aralık kuralları geçerlidir

```python
print(repr(list(range(3))))
# Sonuç: [0, 1, 2]
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.7.3: range davranışını ayırt et**

#### Önce

[b:2.7](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; range uç sınırı dışlar; negatif adım ve boş aralık kuralları geçerlidir

```python
list(range(6,0,-2))
list(range(1,1))
range(0,3,0)
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `[6, 4, 2]`; `[]`; `ValueError`.
- [ ] Range uç sınırı dışlar; negatif adım ve boş aralık kuralları geçerlidir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../sequence.count/README.md)
<!-- learning-task:end -->
