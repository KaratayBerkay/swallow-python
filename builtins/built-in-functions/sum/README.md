## `sum()`

```
sum(iterable, /, start=0)
```

Sums *start* and the items of an *iterable* from left to right and returns the
total.  The *iterable*'s items are normally numbers, and the start value is not
allowed to be a string.

For some use cases, there are good alternatives to sum().
The preferred, fast way to concatenate a sequence of strings is by calling
`''.join(sequence)`.  To add floating-point values with extended precision,
see [math.fsum()](https://docs.python.org/3.15/library/math.html#math.fsum).  To concatenate a series of iterables, consider using
[itertools.chain()](https://docs.python.org/3.15/library/itertools.html#itertools.chain).

> *Changed in version 3.8:* The *start* parameter can be specified as a keyword argument.

> *Changed in version 3.12:* that gives higher accuracy and better commutativity on most builds.

> *Changed in version 3.14:* Added specialization for summation of complexes,
> using same algorithm as for summation of floats.

## Çözümlü kısa örnek

Başlangıç değeri boş iterable için de kullanılır; metin birleştirme ayrı işlemdir.

```python
print(repr(sum([2,3])))
# Sonuç: 5
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.67: sum davranışını ayırt et**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; başlangıç değeri boş iterable için de kullanılır; metin birleştirme ayrı işlemdir.

```python
sum([],10)
sum([2,3],10)
sum(["a","b"],"")
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `10`; `15`; `TypeError`.
- [ ] Başlangıç değeri boş iterable için de kullanılır; metin birleştirme ayrı işlemdir.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../super/README.md)
<!-- learning-task:end -->
