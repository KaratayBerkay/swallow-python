## `slice()`

```
slice(stop, /)
slice(start, stop, step=None, /)
```

Return a [slice](https://docs.python.org/3.15/glossary.html#term-slice) object representing the set of indices specified by
`range(start, stop, step)`.  The *start* and *step* arguments default to
`None`.

Slice objects are also generated when [slicing syntax](https://docs.python.org/3.15/reference/expressions.html#slicings)
is used.  For example: `a[start:stop:step]` or `a[start:stop, i]`.

See [itertools.islice()](https://docs.python.org/3.15/library/itertools.html#itertools.islice) for an alternate version that returns an
[iterator](https://docs.python.org/3.15/glossary.html#term-iterator).

### slice.start, slice.stop, slice.step

These read-only attributes are set to the argument values
(or their default).  They have no other explicit functionality;
however, they are used by NumPy and other third-party packages.

> *Changed in version 3.12:* Slice objects are now [hashable](https://docs.python.org/3.15/glossary.html#term-hashable) (provided [start](https://docs.python.org/3.15/builtins/functions.html#slice.start),
> [stop](https://docs.python.org/3.15/builtins/functions.html#slice.stop), and [step](https://docs.python.org/3.15/builtins/functions.html#slice.step) are hashable).

## Çözümlü kısa örnek

Dilim nesnesi yalnız sınırları taşır; uygulandığı dizi seçilir.

```python
print(repr([0,1,2,3][slice(1,3)]))
# Sonuç: [1, 2]
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.63: slice davranışını ayırt et**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; dilim nesnesi yalnız sınırları taşır; uygulandığı dizi seçilir.

```python
[0,1,2,3,4][slice(None,None,-2)]
slice(2).start
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `[4, 2, 0]`; `None`.
- [ ] Dilim nesnesi yalnız sınırları taşır; uygulandığı dizi seçilir.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../sorted/README.md)
<!-- learning-task:end -->
