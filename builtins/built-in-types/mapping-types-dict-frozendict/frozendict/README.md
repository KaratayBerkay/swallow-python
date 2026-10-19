## `frozendict`

```
frozendict(**kwargs)
frozendict(mapping, /, **kwargs)
frozendict(iterable, /, **kwargs)
```

Return a new frozen dictionary initialized from an optional positional
argument and a possibly empty set of keyword arguments.

A frozendict has a similar API to the [dict](../dict/README.md) API, with the
following differences:

- [dict](../dict/README.md) has more methods than frozendict:

  > - `__delitem__()`
  >
  > - `__setitem__()`
  >
  > - [clear()](https://docs.python.org/3.15/builtins/stdtypes.html#dict.clear)
  >
  > - [pop()](https://docs.python.org/3.15/builtins/stdtypes.html#dict.pop)
  >
  > - [popitem()](https://docs.python.org/3.15/builtins/stdtypes.html#dict.popitem)
  >
  > - [setdefault()](https://docs.python.org/3.15/builtins/stdtypes.html#dict.setdefault)
  >
  > - [update()](https://docs.python.org/3.15/builtins/stdtypes.html#dict.update)

- A frozendict can be hashed with `hash(frozendict)` if all keys and
  values can be hashed.

- `frozendict |= other` does not modify the frozendict in-place but
  creates a new frozen dictionary.

frozendict is not a [dict](../dict/README.md) subclass but inherits directly
from `object`.

Like dictionaries, frozendicts are [generic](https://docs.python.org/3.15/library/typing.html#generics) over two types,
signifying (respectively) the types of the frozendict's keys and values.

### fromkeys(iterable,, value=None,, /)

Similar to [dict.fromkeys()](https://docs.python.org/3.15/builtins/stdtypes.html#dict.fromkeys), but call again the type constructor
with an initialized frozendict if the type is a
frozendict subclass or if the constructor returned a
frozendict.

> *Added in version 3.15.*

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.12.1: Değişmez eşlemenin sınırını göster**

#### Önce

[b:2.12](../README.md) ve bu sayfanın açıklama/örnekleri.

Sürüm: Python 3.15 veya üzeri. Daha eski yorumlayıcıda yalnız bu sürüme bağlı kısmı gerekçeli yazılı iz ile çözebilirsin; çalıştırma kanıtını bekleyen olarak kaydet.

#### Tek görev

`f=frozendict(a=[1]); once=f` ile başla. `f["a"].append(2)`, f içine yeni anahtar atama, `hash(f)` ve `f |= {"b":3}` işlemlerini ayrı ayrı incele. Sonuncudan önceki ve sonraki kimlikleri karşılaştır. Ayrıca hashable değerli bir frozendict ile hash dene.

#### Geçiş ölçütleri

- [ ] İç liste değişebilir; shallow değişmezlik derin dondurma değildir.
- [ ] Anahtar atama TypeError, hash(f) TypeError; hashable anahtar ve değerler hash için gerekir.
- [ ] |= yeni frozendict üretir; once eski eşlemeyi tutar; frozendict dict alt sınıfı değildir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../dict/README.md)
<!-- learning-task:end -->
