A set object is an unordered collection of distinct [hashable](https://docs.python.org/3.15/glossary.html#term-hashable) objects.
Common uses include membership testing, removing duplicates from a sequence, and
computing mathematical operations such as intersection, union, difference, and
symmetric difference.
(For other containers see the built-in [dict](../mapping-types-dict-frozendict/dict/README.md), [list](../sequence-types-list-tuple-range/list/README.md),
and [tuple](../sequence-types-list-tuple-range/tuple/README.md) classes, and the [collections](https://docs.python.org/3.15/library/collections.html#module-collections) module.)
See [Time complexity of operations on built-in types](https://docs.python.org/3.15/builtins/time-complexity.html#time-complexity) for the costs of the various set operations.

Like other collections, sets support `x in set`, `len(set)`, and `for x in
set`.  Being an unordered collection, sets do not record element position or
order of insertion.  Accordingly, sets do not support indexing, slicing, or
other sequence-like behavior.

There are currently two built-in set types, [set](set/README.md) and [frozenset](set/README.md).
The [set](set/README.md) type is mutable --- the contents can be changed using methods
like [add()](set.add/README.md) and [remove()](set.remove/README.md).
Since it is mutable, it has no hash value and cannot be used as
either a dictionary key or as an element of another set.
The [frozenset](set/README.md) type is immutable and [hashable](https://docs.python.org/3.15/glossary.html#term-hashable) ---
its contents cannot be altered after it is created;
it can therefore be used as a dictionary key or as an element of another set.

Non-empty sets (not frozensets) can be created by placing a comma-separated list
of elements within braces, for example: `{'jack', 'sjoerd'}`, in addition to the
[set](set/README.md) constructor.

The constructors for both classes work the same:

- [`set`](set/README.md) — Return a new set or frozenset object whose elements are taken from *iterable*.
- [`frozenset`](frozenset/README.md) — Documented together with set.

Sets can be created by several means:

- Use a comma-separated list of elements within braces: `{'jack', 'sjoerd'}`

- Use a set comprehension: `{c for c in 'abracadabra' if c not in 'abc'}`

- Use the type constructor: `set()`, `set('foobar')`, `set(['a', 'b', 'foo'])`

Instances of [set](set/README.md) and [frozenset](set/README.md) provide the following
operations:

### len(s)

Return the number of elements in set *s* (cardinality of *s*).

### x, in, s

Test *x* for membership in *s*.

### x, not, in, s

Test *x* for non-membership in *s*.

- [`frozenset.isdisjoint`](frozenset.isdisjoint/README.md) — Return True if the set has no elements in common with *other*.
- [`set.isdisjoint`](set.isdisjoint/README.md) — Documented together with frozenset.isdisjoint.
- [`frozenset.issubset`](frozenset.issubset/README.md)
- [`set.issubset`](set.issubset/README.md) — Documented together with frozenset.issubset.

### set, <=, other

Test whether every element in the set is in *other*.

### set, <, other

Test whether the set is a proper subset of *other*, that is,
`set <= other and set != other`.

- [`frozenset.issuperset`](frozenset.issuperset/README.md)
- [`set.issuperset`](set.issuperset/README.md) — Documented together with frozenset.issuperset.

### set, >=, other

Test whether every element in *other* is in the set.

### set, >, other

Test whether the set is a proper superset of *other*, that is, `set >=
other and set != other`.

- [`frozenset.union`](frozenset.union/README.md)
- [`set.union`](set.union/README.md) — Documented together with frozenset.union.

### set, |, other, |, ...

Return a new set with elements from the set and all others.

- [`frozenset.intersection`](frozenset.intersection/README.md)
- [`set.intersection`](set.intersection/README.md) — Documented together with frozenset.intersection.

### set, &, other, &, ...

Return a new set with elements common to the set and all others.

- [`frozenset.difference`](frozenset.difference/README.md)
- [`set.difference`](set.difference/README.md) — Documented together with frozenset.difference.

### set, -, other, -, ...

Return a new set with elements in the set that are not in the others.

- [`frozenset.symmetric_difference`](frozenset.symmetric_difference/README.md)
- [`set.symmetric_difference`](set.symmetric_difference/README.md) — Documented together with frozenset.symmetric_difference.

### set, ^, other

Return a new set with elements in either the set or *other* but not both.

- [`frozenset.copy`](frozenset.copy/README.md) — Return a shallow copy of the set.
- [`set.copy`](set.copy/README.md) — Documented together with frozenset.copy.

Note, the non-operator versions of [union()](frozenset.union/README.md),
[intersection()](frozenset.intersection/README.md), [difference()](frozenset.difference/README.md), [symmetric_difference()](frozenset.symmetric_difference/README.md), [issubset()](frozenset.issubset/README.md), and
[issuperset()](frozenset.issuperset/README.md) methods will accept any iterable as an argument.  In
contrast, their operator based counterparts require their arguments to be
sets.  This precludes error-prone constructions like `set('abc') & 'cbs'`
in favor of the more readable `set('abc').intersection('cbs')`.

Both [set](set/README.md) and [frozenset](set/README.md) support set to set comparisons. Two
sets are equal if and only if every element of each set is contained in the
other (each is a subset of the other). A set is less than another set if and
only if the first set is a proper subset of the second set (is a subset, but
is not equal). A set is greater than another set if and only if the first set
is a proper superset of the second set (is a superset, but is not equal).

Instances of [set](set/README.md) are compared to instances of [frozenset](set/README.md)
based on their members.  For example, `set('abc') == frozenset('abc')`
returns `True` and so does `set('abc') in set([frozenset('abc')])`.

The subset and equality comparisons do not generalize to a total ordering
function.  For example, any two nonempty disjoint sets are not equal and are not
subsets of each other, so *all* of the following return `False`: `a<b`,
`a==b`, or `a>b`.

Since sets only define partial ordering (subset relationships), the output of
the [list.sort()](https://docs.python.org/3.15/builtins/stdtypes.html#list.sort) method is undefined for lists of sets.

Set elements, like dictionary keys, must be [hashable](https://docs.python.org/3.15/glossary.html#term-hashable).

Binary operations that mix [set](set/README.md) instances with [frozenset](set/README.md)
return the type of the first operand.  For example: `frozenset('ab') |
set('bc')` returns an instance of [frozenset](set/README.md).

The following table lists operations available for [set](set/README.md) that do not
apply to immutable instances of [frozenset](set/README.md):

- [`set.update`](set.update/README.md)

### set, |=, other, |, ...

Update the set, adding elements from all others.

- [`set.intersection_update`](set.intersection_update/README.md)

### set, &=, other, &, ...

Update the set, keeping only elements found in it and all others.

- [`set.difference_update`](set.difference_update/README.md)

### set, -=, other, |, ...

Update the set, removing elements found in others.

- [`set.symmetric_difference_update`](set.symmetric_difference_update/README.md)

### set, ^=, other

Update the set, keeping only elements found in either set, but not in both.

- [`set.add`](set.add/README.md) — Add element *elem* to the set.
- [`set.remove`](set.remove/README.md) — Remove element *elem* from the set.
- [`set.discard`](set.discard/README.md) — Remove element *elem* from the set if it is present.
- [`set.pop`](set.pop/README.md) — Remove and return an arbitrary element from the set.
- [`set.clear`](set.clear/README.md) — Remove all elements from the set.

Note, the non-operator versions of the [update()](set.update/README.md),
[intersection_update()](set.intersection_update/README.md), [difference_update()](set.difference_update/README.md), and
[symmetric_difference_update()](set.symmetric_difference_update/README.md) methods will accept any iterable as an
argument.

Note, the *elem* argument to the [__contains__()](https://docs.python.org/3.15/reference/datamodel.html#object.__contains__),
[remove()](set.remove/README.md), and
[discard()](set.discard/README.md) methods may be a set.  To support searching for an equivalent
frozenset, a temporary one is created from *elem*.

Sets and frozensets are [generic](https://docs.python.org/3.15/library/typing.html#generics) over the type of their elements.

> **See also**
>
> For detailed information on thread-safety guarantees for [set](set/README.md)
> objects, see [Thread safety for set objects](https://docs.python.org/3.15/builtins/threadsafety.html#thread-safety-set).

## Çözümlü kısa örnek

Tekrar silme, üyelik ve sıra bağımsızlığını bağla

```python
print(repr(sorted(set([3,1,3]))))
# Sonuç: [1, 3]
```

<!-- learning-task:start -->
#### Bölüm görevi

**Görev b:2.11: set-types-set-frozenset davranışını ayırt et**

##### Önce

[b:2](../README.md) ve bu sayfanın açıklama/örnekleri.

##### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; tekrar silme, üyelik ve sıra bağımsızlığını bağla

```python
{1,2}=={2,1}
{1,2} < {2,3}
{1,2} <= {1,2,3}
```

##### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `False`; `True`.
- [ ] Tekrar silme, üyelik ve sıra bağımsızlığını bağla

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](set/README.md)
<!-- learning-task:end -->

<!-- learning-milestone:start -->
#### Klasör milestone görevi

**Milestone: Üyelik politikasını küme cebiriyle kur**

##### Önce

Bu klasördeki bütün bölüm görevleri ve alt klasör milestone kontrolleri tamamlanmış olmalı. Sırayı [görev dizininden](../../../TASKS.md) kontrol et.

##### Tek görev

İzinli, istenen ve engelli kullanıcı kümelerinden kabul edilenleri, reddedilenleri ve yalnız bir listede bulunanları üret. Kaynak kümeleri koruyan sürüm ile çalışma kümesini yerinde güncelleyen sürümü karşılaştır. İç içe küme gerekiyorsa frozenset kullan.

##### Geçiş ölçütleri

- [ ] Kesişim/fark/simetrik fark doğru seçilmiştir; çıktı sırasına bağlı hata yoktur.
- [ ] Yeni sonuç ile yerinde güncelleme ayrılır; hashable öğe gereği açıklanır; boş ve tam çakışan kümeler denenir.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../mapping-types-dict-frozendict/README.md)
<!-- learning-milestone:end -->
