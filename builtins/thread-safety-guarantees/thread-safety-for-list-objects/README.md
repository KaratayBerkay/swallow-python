Reading a single element from a [list](../../built-in-types/sequence-types-list-tuple-range/list/README.md) is
[atomic](https://docs.python.org/3.15/glossary.html#term-atomic-operation):

``` python
lst[i]   # list.__getitem__
```

The following methods traverse the list and use [atomic](https://docs.python.org/3.15/glossary.html#term-atomic-operation)
reads of each item to perform their function. That means that they may
return results affected by concurrent modifications:

``` python
item in lst
lst.index(item)
lst.count(item)
```

All of the above operations avoid acquiring [per-object locks](https://docs.python.org/3.15/glossary.html#term-per-object-lock). They do not block concurrent modifications. Other
operations that hold a lock will not block these from observing intermediate
states.

All other operations from here on block using the [per-object lock](https://docs.python.org/3.15/glossary.html#term-per-object-lock).

Writing a single item via `lst[i] = x` is safe to call from multiple
threads and will not corrupt the list.

The following operations return new objects and appear
[atomic](https://docs.python.org/3.15/glossary.html#term-atomic-operation) to other threads:

``` python
lst1 + lst2    # concatenates two lists into a new list
x * lst        # repeats lst x times into a new list
lst.copy()     # returns a shallow copy of the list
```

The following methods that only operate on a single element with no shifting
required are [atomic](https://docs.python.org/3.15/glossary.html#term-atomic-operation):

``` python
lst.append(x)  # append to the end of the list, no shifting required
lst.pop()      # pop element from the end of the list, no shifting required
```

The [clear()](../../built-in-types/sequence-types-list-tuple-range/list.clear/README.md) method is also [atomic](https://docs.python.org/3.15/glossary.html#term-atomic-operation).
Other threads cannot observe elements being removed.

The [sort()](https://docs.python.org/3.15/builtins/stdtypes.html#list.sort) method is not [atomic](https://docs.python.org/3.15/glossary.html#term-atomic-operation).
Other threads cannot observe intermediate states during sorting, but the
list appears empty for the duration of the sort.

The following operations may allow [lock-free](https://docs.python.org/3.15/glossary.html#term-lock-free) operations to observe
intermediate states since they modify multiple elements in place:

``` python
lst.insert(idx, item)  # shifts elements
lst.pop(idx)           # idx not at the end of the list, shifts elements
lst *= x               # copies elements in place
```

The [remove()](../../built-in-types/sequence-types-list-tuple-range/list.remove/README.md) method may allow concurrent modifications since
element comparison may execute arbitrary Python code (via
[__eq__()](https://docs.python.org/3.15/reference/datamodel.html#object.__eq__)).

[extend()](../../built-in-types/sequence-types-list-tuple-range/list.extend/README.md) is safe to call from multiple threads.  However, its
guarantees depend on the iterable passed to it. If it is a [list](../../built-in-types/sequence-types-list-tuple-range/list/README.md), a
[tuple](../../built-in-types/sequence-types-list-tuple-range/tuple/README.md), a [set](../../built-in-types/set-types-set-frozenset/set/README.md), a [frozenset](../../built-in-types/set-types-set-frozenset/frozenset/README.md), a [dict](../../built-in-types/mapping-types-dict-frozendict/dict/README.md) or a
[dictionary view object](https://docs.python.org/3.15/builtins/stdtypes.html#dict-views) (but not their subclasses), the
`extend` operation is safe from concurrent modifications to the iterable.
Otherwise, an iterator is created which can be concurrently modified by
another thread.  The same applies to inplace concatenation of a list with
other iterables when using `lst += iterable`.

Similarly, assigning to a list slice with `lst[i:j] = iterable` is safe
to call from multiple threads, but `iterable` is only locked when it is
also a [list](../../built-in-types/sequence-types-list-tuple-range/list/README.md) (but not its subclasses).

Operations that involve multiple accesses, as well as iteration, are never
atomic. For example:

``` python
# NOT atomic: read-modify-write
lst[i] = lst[i] + 1

# NOT atomic: check-then-act
if lst:
    item = lst.pop()

# NOT thread-safe: iteration while modifying
for item in lst:
    process(item)  # another thread may modify lst
```

Consider external synchronization when sharing [list](../../built-in-types/sequence-types-list-tuple-range/list/README.md) instances
across threads.

<!-- learning-task:start -->
## Bölüm görevi

**Görev b:5.2: Eşzamanlılık iddiasını durum akışıyla sınayalım**

### Önce

[b:5](../README.md) ve bu sayfanın açıklama/örnekleri.

Bu görevde verilen durumların yazılı çözümü geçerlidir; ek çalışma ortamı veya harici araç kurulumu gerekmez.

### Tek görev

lst=[1] için A threadi if lst kontrolünü geçiyor; B pop ile öğeyi alıyor; A pop çağırıyor. Akışı çöz. Tek öğe okuma, append/pop(), üyelik/index/count taraması, sort, eleman kaydırmalı pop(0), extend(list) ve extend(özel iterable) garantilerini sınıflandır. Gerçek thread yarışı üretmek yerine verilen sıralamayı yazılı çöz; her garanti için bu sayfadaki koşulu belirt.

### Geçiş ölçütleri

- [ ] A son adımda IndexError alabilir; iki ayrı güvenli çağrı atomik bir check-then-act değildir.
- [ ] Okuma/append/pop() atomik; taramalar eşzamanlı değişiklik görebilir; sort atomik değildir, liste geçici boş görünür.
- [ ] Extend girdi türü ve kaydırmalı işlemlerin lock-free okuyuculara etkisi ayrılmıştır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../thread-safety-for-dict-objects/README.md)
<!-- learning-task:end -->
