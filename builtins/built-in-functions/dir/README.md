## `dir()`

```
dir()
dir(object, /)
```

Without arguments, return the list of names in the current local scope.  With an
argument, attempt to return a list of valid attributes for that object.

If the object has a method named [__dir__()](https://docs.python.org/3.15/reference/datamodel.html#object.__dir__),
this method will be called and
must return the list of attributes. This allows objects that implement a custom
`__getattr__()` or `__getattribute__()` function
to customize the way
dir() reports their attributes.

If the object does not provide [__dir__()](https://docs.python.org/3.15/reference/datamodel.html#object.__dir__),
the function tries its best to gather information from the object's
[__dict__](https://docs.python.org/3.15/reference/datamodel.html#object.__dict__) attribute, if defined, and
from its type object.  The resulting list is not necessarily complete and may
be inaccurate when the object has a custom `__getattr__()`.

The default dir() mechanism behaves differently with different types of
objects, as it attempts to produce the most relevant, rather than complete,
information:

- If the object is a module object, the list contains the names of the module's
  attributes.

- If the object is a type or class object, the list contains the names of its
  attributes, and recursively of the attributes of its bases.

- Otherwise, the list contains the object's attributes' names, the names of its
  class's attributes, and recursively of the attributes of its class's base
  classes.

The resulting list is sorted alphabetically.  For example:

``` python
>>> import struct
>>> dir()   # show the names in the module namespace  # doctest: +SKIP
['__builtins__', '__name__', 'struct']
>>> dir(struct)   # show the names in the struct module # doctest: +SKIP
['Struct', '__all__', '__builtins__', '__doc__', '__file__',
 '__initializing__', '__loader__', '__name__', '__package__',
 '_clearcache', 'calcsize', 'error', 'pack', 'pack_into',
 'unpack', 'unpack_from']
>>> class Shape:
...     def __dir__(self):
...         return ['area', 'perimeter', 'location']
...
>>> s = Shape()
>>> dir(s)
['area', 'location', 'perimeter']
```

> **Note**
>
> Because dir() is supplied primarily as a convenience for use at an
> interactive prompt, it tries to supply an interesting set of names more
> than it tries to supply a rigorously or consistently defined set of names,
> and its detailed behavior may change across releases.  For example,
> metaclass attributes are not in the result list when the argument is a
> class.

## Çözümlü kısa örnek

Dir keşif için isim listesi verir; içerik türün davranışına göre değişebilir.

```python
class K: puan=4
o=K()
print(repr("puan" in dir(o)))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.19: dir davranışını ayırt et**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; dir keşif için isim listesi verir; içerik türün davranışına göre değişebilir.

```python
class K: puan=4
o=K()
"eksik" in dir(o)
dir(o)==sorted(dir(o))
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `False`; `True`.
- [ ] Dir keşif için isim listesi verir; içerik türün davranışına göre değişebilir.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../divmod/README.md)
<!-- learning-task:end -->
