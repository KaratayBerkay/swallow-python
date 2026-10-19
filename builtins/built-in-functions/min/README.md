## `min()`

```
min(iterable, /, *, key=None)
min(iterable, /, *, default, key=None)
min(arg1, arg2, /, *args, key=None)
```

Return the smallest item in an iterable or the smallest of two or more
arguments.

If one positional argument is provided, it should be an [iterable](https://docs.python.org/3.15/glossary.html#term-iterable).
The smallest item in the iterable is returned.  If two or more positional
arguments are provided, the smallest of the positional arguments is
returned.

There are two optional keyword-only arguments. The *key* argument specifies
a one-argument ordering function like that used for [list.sort()](https://docs.python.org/3.15/builtins/stdtypes.html#list.sort). The
*default* argument specifies an object to return if the provided iterable is
empty. If the iterable is empty and *default* is not provided, a
[ValueError](https://docs.python.org/3.15/builtins/exceptions.html#ValueError) is raised.

If multiple items are minimal, the function returns the first one
encountered.  This is consistent with other sort-stability preserving tools
such as `sorted(iterable, key=keyfunc)[0]` and `heapq.nsmallest(1,
iterable, key=keyfunc)`.

> *Changed in version 3.4:* Added the *default* keyword-only parameter.

> *Changed in version 3.8:* The *key* can be `None`.

## Çözümlü kısa örnek

Boş iterable varsayılanıyla birden çok konumsal değeri ayır.

```python
print(repr(min([2,5,1])))
# Sonuç: 1
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.47: min davranışını ayırt et**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; boş iterable varsayılanıyla birden çok konumsal değeri ayır.

```python
min([],default=9)
min(5,2,7)
min([])
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `9`; `2`; `ValueError`.
- [ ] Boş iterable varsayılanıyla birden çok konumsal değeri ayır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../next/README.md)
<!-- learning-task:end -->
