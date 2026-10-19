The [len()](../../built-in-functions/len/README.md) function is lock-free and [atomic](https://docs.python.org/3.15/glossary.html#term-atomic-operation).

The following read operation is lock-free. It does not block concurrent
modifications and may observe intermediate states from operations that
hold the per-object lock:

``` python
elem in s    # set.__contains__
```

This operation may compare elements using [__eq__()](https://docs.python.org/3.15/reference/datamodel.html#object.__eq__), which can
execute arbitrary Python code. During such comparisons, the set may be
modified by another thread. For built-in types like [str](../../built-in-types/text-sequence-type-str/str/README.md),
[int](https://docs.python.org/3.15/builtins/functions.html#int), and [float](https://docs.python.org/3.15/builtins/functions.html#float), `__eq__()` does not release the
underlying lock during comparisons and this is not a concern.

All other operations from here on hold the per-object lock.

Adding or removing a single element is safe to call from multiple threads
and will not corrupt the set:

``` python
s.add(elem)      # add element
s.remove(elem)   # remove element, raise if missing
s.discard(elem)  # remove element if present
s.pop()          # remove and return arbitrary element
```

These operations also compare elements, so the same [__eq__()](https://docs.python.org/3.15/reference/datamodel.html#object.__eq__)
considerations as above apply.

The [copy()](../../built-in-types/set-types-set-frozenset/set.copy/README.md) method returns a new object and holds the per-object lock
for the duration so that it is always atomic.

The [clear()](../../built-in-types/set-types-set-frozenset/set.clear/README.md) method holds the lock for its duration. Other
threads cannot observe elements being removed.

The following operations only accept [set](../../built-in-types/set-types-set-frozenset/set/README.md) or [frozenset](../../built-in-types/set-types-set-frozenset/frozenset/README.md)
as operands and always lock both objects:

``` python
s |= other                   # other must be set/frozenset
s &= other                   # other must be set/frozenset
s -= other                   # other must be set/frozenset
s ^= other                   # other must be set/frozenset
s & other                    # other must be set/frozenset
s | other                    # other must be set/frozenset
s - other                    # other must be set/frozenset
s ^ other                    # other must be set/frozenset
```

[set.update()](../../built-in-types/set-types-set-frozenset/set.update/README.md), [set.union()](../../built-in-types/set-types-set-frozenset/set.union/README.md), [set.intersection()](../../built-in-types/set-types-set-frozenset/set.intersection/README.md) and
[set.difference()](../../built-in-types/set-types-set-frozenset/set.difference/README.md) can take multiple iterables as arguments. They all
iterate through all the passed iterables and do the following:

> - [set.update()](../../built-in-types/set-types-set-frozenset/set.update/README.md) and [set.union()](../../built-in-types/set-types-set-frozenset/set.union/README.md) lock both objects only when
>   the other operand is a [set](../../built-in-types/set-types-set-frozenset/set/README.md), [frozenset](../../built-in-types/set-types-set-frozenset/frozenset/README.md), or [dict](../../built-in-types/mapping-types-dict-frozendict/dict/README.md).
>
> - [set.intersection()](../../built-in-types/set-types-set-frozenset/set.intersection/README.md) and [set.difference()](../../built-in-types/set-types-set-frozenset/set.difference/README.md) always try to lock
>   all objects.

[set.symmetric_difference()](../../built-in-types/set-types-set-frozenset/set.symmetric_difference/README.md) tries to lock both objects.

The update variants of the above methods also have some differences between
them:

> - [set.difference_update()](../../built-in-types/set-types-set-frozenset/set.difference_update/README.md) and [set.intersection_update()](../../built-in-types/set-types-set-frozenset/set.intersection_update/README.md) try
>   to lock all objects one-by-one.
>
> - [set.symmetric_difference_update()](../../built-in-types/set-types-set-frozenset/set.symmetric_difference_update/README.md) only locks the arguments if it is
>   of type [set](../../built-in-types/set-types-set-frozenset/set/README.md), [frozenset](../../built-in-types/set-types-set-frozenset/frozenset/README.md), or [dict](../../built-in-types/mapping-types-dict-frozendict/dict/README.md).

The following methods always try to lock both objects:

``` python
s.isdisjoint(other)          # both locked
s.issubset(other)            # both locked
s.issuperset(other)          # both locked
```

Operations that involve multiple accesses, as well as iteration, are never
atomic:

``` python
# NOT atomic: check-then-act
if elem in s:
      s.remove(elem)

# NOT thread-safe: iteration while modifying
for elem in s:
      process(elem)  # another thread may modify s
```

Consider external synchronization when sharing [set](../../built-in-types/set-types-set-frozenset/set/README.md) instances
across threads.  See [Python support for free threading](https://docs.python.org/3.15/howto/free-threading-python.html#freethreading-python-howto) for more information.

<!-- learning-task:start -->
## Bölüm görevi

**Görev b:5.4: Eşzamanlılık iddiasını durum akışıyla sınayalım**

### Önce

[b:5](../README.md) ve bu sayfanın açıklama/örnekleri.

Bu görevde verilen durumların yazılı çözümü geçerlidir; ek çalışma ortamı veya harici araç kurulumu gerekmez.

### Tek görev

s={1} için A üyelik kontrolünü geçiyor; B remove(1) yapıyor; A remove(1) yapıyor. Sonucu, discard seçeneğiyle karşılaştır. Len, membership, copy, operatörler ve iterable alan yöntemlerde iki tarafın kilitlenme koşullarını ayır. Gerçek thread yarışı üretmek yerine verilen sıralamayı yazılı çöz; her garanti için bu sayfadaki koşulu belirt.

### Geçiş ölçütleri

- [ ] İkinci remove KeyError verebilir; discard eksik üyede hata vermez, bütün algoritmaya atomiklik kazandırmaz.
- [ ] Len atomik, üyelik eşzamanlı değişimi görebilir; yöntem/operatör ve argüman türü garantileri farklıdır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../thread-safety-for-bytearray-objects/README.md)
<!-- learning-task:end -->
