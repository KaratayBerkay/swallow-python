## `filter()`

```
filter(function, iterable, /)
```

Construct an iterator from those elements of *iterable* for which *function*
is true.  *iterable* may be either a sequence, a container which
supports iteration, or an iterator.  If *function* is `None`, the identity
function is assumed, that is, all elements of *iterable* that are false are
removed.

Note that `filter(function, iterable)` is equivalent to the generator
expression `(item for item in iterable if function(item))` if function is
not `None` and `(item for item in iterable if item)` if function is
`None`.

See [itertools.filterfalse()](https://docs.python.org/3.15/library/itertools.html#itertools.filterfalse) for the complementary function that returns
elements of *iterable* for which *function* is false.

## Çözümlü kısa örnek

None filtresinde doğruluk sınanır; dönüş değeri iterator olduğundan tüketim ayrıdır.

```python
print(repr(list(filter(None,[0,1]))))
# Sonuç: [1]
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.24: filter davranışını ayırt et**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; none filtresinde doğruluk sınanır; dönüş değeri iterator olduğundan tüketim ayrıdır.

```python
list(filter(None,[0,"",[],[0],2]))
list(filter(lambda x:x>2,[1,3,2,4]))
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `[[0], 2]`; `[3, 4]`.
- [ ] None filtresinde doğruluk sınanır; dönüş değeri iterator olduğundan tüketim ayrıdır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../float/README.md)
<!-- learning-task:end -->
