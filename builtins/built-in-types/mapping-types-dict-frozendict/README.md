A [mapping](https://docs.python.org/3.15/glossary.html#term-mapping) object maps [hashable](https://docs.python.org/3.15/glossary.html#term-hashable) values to arbitrary objects.
There are currently two standard mapping types, the dictionary and
[frozendict](frozendict/README.md).
(For other containers see the built-in
[list](../sequence-types-list-tuple-range/list/README.md), [set](../set-types-set-frozenset/set/README.md), and [tuple](../sequence-types-list-tuple-range/tuple/README.md) classes, and the
[collections](https://docs.python.org/3.15/library/collections.html#module-collections) module.)
See [Time complexity of operations on built-in types](https://docs.python.org/3.15/builtins/time-complexity.html#time-complexity) for the costs of the various dictionary
operations.

A dictionary's keys are *almost* arbitrary values.  Values that are not
[hashable](https://docs.python.org/3.15/glossary.html#term-hashable), that is, values containing lists, dictionaries or other
mutable types (that are compared by value rather than by object identity) may
not be used as keys.
Values that compare equal (such as `1`, `1.0`, and `True`)
can be used interchangeably to index the same dictionary entry.

- [`dict`](dict/README.md) — Return a new dictionary initialized from an optional positional argument and a possibly empty set of keyword arguments.

> **See also**
>
> For detailed information on thread-safety guarantees for [dict](dict/README.md)
> objects, see [Thread safety for dict objects](https://docs.python.org/3.15/builtins/threadsafety.html#thread-safety-dict).

## Dictionary view objects

The objects returned by [dict.keys()](https://docs.python.org/3.15/builtins/stdtypes.html#dict.keys), [dict.values()](https://docs.python.org/3.15/builtins/stdtypes.html#dict.values) and
[dict.items()](https://docs.python.org/3.15/builtins/stdtypes.html#dict.items) are *view objects*.  They provide a dynamic view on the
dictionary's entries, which means that when the dictionary changes, the view
reflects these changes.

Dictionary views can be iterated over to yield their respective data, and
support membership tests:

### len(dictview)

Return the number of entries in the dictionary.

### iter(dictview)

Return an iterator over the keys, values or items (represented as tuples of
`(key, value)`) in the dictionary.

Keys and values are iterated over in insertion order.
This allows the creation of `(value, key)` pairs
using [zip()](../../built-in-functions/zip/README.md): `pairs = zip(d.values(), d.keys())`.  Another way to
create the same list is `pairs = [(v, k) for (k, v) in d.items()]`.

Iterating views while adding or deleting entries in the dictionary may raise
a [RuntimeError](https://docs.python.org/3.15/builtins/exceptions.html#RuntimeError) or fail to iterate over all entries.

> *Changed in version 3.7:* Dictionary order is guaranteed to be insertion order.

### x, in, dictview

Return `True` if *x* is in the underlying dictionary's keys, values or
items (in the latter case, *x* should be a `(key, value)` tuple).

### reversed(dictview)

Return a reverse iterator over the keys, values or items of the dictionary.
The view will be iterated in reverse order of the insertion.

> *Changed in version 3.8:* Dictionary views are now reversible.

### dictview.mapping

Return a [types.MappingProxyType](https://docs.python.org/3.15/library/types.html#types.MappingProxyType) that wraps the original
dictionary to which the view refers.

> *Added in version 3.10.*

Keys views are set-like since their entries are unique and [hashable](https://docs.python.org/3.15/glossary.html#term-hashable).
Items views also have set-like operations since the (key, value) pairs
are unique and the keys are hashable.
If all values in an items view are hashable as well,
then the items view can interoperate with other sets.
(Values views are not treated as set-like
since the entries are generally not unique.)  For set-like views, all of the
operations defined for the abstract base class [collections.abc.Set](https://docs.python.org/3.15/library/collections.abc.html#collections.abc.Set) are
available (for example, `==`, `<`, or `^`).  While using set operators,
set-like views accept any iterable as the other operand,
unlike sets which only accept sets as the input.

An example of dictionary view usage:

``` python
>>> dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
>>> keys = dishes.keys()
>>> values = dishes.values()

>>> # iteration
>>> n = 0
>>> for val in values:
...     n += val
...
>>> print(n)
504

>>> # keys and values are iterated over in the same order (insertion order)
>>> list(keys)
['eggs', 'sausage', 'bacon', 'spam']
>>> list(values)
[2, 1, 1, 500]

>>> # view objects are dynamic and reflect dict changes
>>> del dishes['eggs']
>>> del dishes['sausage']
>>> list(keys)
['bacon', 'spam']

>>> # set operations
>>> keys & {'eggs', 'bacon', 'salad'}
{'bacon'}
>>> keys ^ {'sausage', 'juice'} == {'juice', 'sausage', 'bacon', 'spam'}
True
>>> keys | ['juice', 'juice', 'juice'] == {'bacon', 'spam', 'juice'}
True

>>> # get back a read-only proxy for the original dictionary
>>> values.mapping
mappingproxy({'bacon': 1, 'spam': 500})
>>> values.mapping['spam']
500
```
> Code: [example_01.py](example_01.py)

## Frozen dictionaries

- [`frozendict`](frozendict/README.md) — Return a new frozen dictionary initialized from an optional positional argument and a possibly empty set of keyword arguments.

## Çözümlü kısa örnek

Anahtar eşitliği, hashability ve ekleme sırasını ayır

```python
print(repr({1:"a",True:"b"}))
# Sonuç: {1: 'b'}
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.12: Anahtarları ve canlı sözlük görünümlerini izle**

#### Önce

[b:2](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Bir sözlüğün anahtarlarını ve ondan alınan görünümleri aynı çalışma içinde incele. Her adımın sonucunu çalıştırmadan önce çıkar, sonra doğrula.

1. `list({"b":2,"a":1})` ve `{[1]:2}` denemelerini ayrı yap. Kaynaktaki `1`, `1.0`, `True` eşitliğinin aynı anahtarı nasıl etkilediğini açıkla.
2. `d={"Ada":7,"Ece":9}` kur; keys, values ve items görünümlerini sakla. Uzunluklarını, sıralı dolaşımlarını, ters dolaşımlarını ve üyelik testlerini karşılaştır. Ardından `d["Can"]=5` ve `del d["Ada"]` uygula; saklanan görünümlerde neyin değiştiğini göster.
3. Güncel keys görünümü ile `["Can","Deniz"]` arasında kesişim yap. Güncel items görünümünü `{("Ece",9)}` ile kesiştir. Values görünümüne aynı küme işlemini uygulamayı ayrı dene. `{"Ada":[7]}.items()` görünümünü `[]` ile birleştirmeyi de dene; değerlerin hashable olmasının neden önemli olduğunu açıkla.
4. Saklanan values görünümünün `mapping` alanını `proxy` adına bağla. Proxy üzerinden atama denemesini, asıl d üzerinde Ece değerini 10 yapmayla karşılaştır. Son olarak canlı görünüm üzerinde dolaşırken anahtar ekleme veya silmenin kaynakta neden güvenilir sayılmadığını yazılı açıkla; her değişikliğin mutlaka aynı hatayı vereceğini varsayma.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `['b', 'a']`; `TypeError`.
- [ ] Eşit sayısal anahtarlar tek girdiyi paylaşır; görünümler doğru sırayı, üyelik anlamını ve değişiklik sonrası Ece/Can girdilerini gösterir. Items görünümünde üye `(anahtar, değer)` çiftidir.
- [ ] Keys kesişimi `{"Can"}`, items kesişimi `{("Ece",9)}` olur. Görünüm operatörleri uygun iterable kabul eder; values küme benzeri değildir, hashlenemeyen item değeri de küme sonucuna konamaz. Son iki geçersiz deneme TypeError verir.
- [ ] Proxy üzerinden yazma TypeError verir; d üzerinden değişiklik proxyye yansır. Salt okunur proxy, bağımsız veya dondurulmuş bir snapshot sayılmamış.
- [ ] Görünüm üzerinde dolaşırken anahtar ekleme/silme hata veya eksik dolaşım üretebilir; güvenli bir tam dolaşım garantisi verilmemiş.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](frozendict/README.md)
<!-- learning-task:end -->

<!-- learning-milestone:start -->
### Klasör milestone görevi

**Milestone: Canlı ayarla dondurulmuş ayarı ayır**

#### Önce

Bu klasördeki bütün bölüm görevleri ve alt klasör milestone kontrolleri tamamlanmış olmalı. Sırayı [görev dizininden](../../../TASKS.md) kontrol et.

Sürüm farkında yalnız yeni özelliği gerekçeli yazılı iz ile inceleyebilirsin; çalıştırma kanıtını bekleyen olarak kaydet.

#### Tek görev

Dict ile varsayılan ayarlara kullanıcı ayarlarını sağ taraf önceliğiyle uygula. Python 3.15 frozendict ile dış eşlemeyi dondur; iç listeyi değiştirmenin etkisini, yeni eşleme üretimini ve hashability koşulunu göster. Eski snapshotın hangi düzeyde bağımsız olduğunu açıkla.

#### Geçiş ölçütleri

- [ ] Çakışma önceliği ve ekleme sırası korunur; eski dış eşleme yeni anahtar almaz.
- [ ] Frozendict derin dondurma değildir; hash için değerlerin de hashable olması gerekir.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../context-manager-types/README.md)
<!-- learning-milestone:end -->
