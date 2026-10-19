## `genericalias.__parameters__`

```
genericalias.__parameters__
```

This attribute is a lazily computed tuple (possibly empty) of unique type
variables found in `__args__`:

``` python
>>> from typing import TypeVar

>>> T = TypeVar('T')
>>> list[T].__parameters__
(~T,)
```
> Code: [example_01.py](example_01.py)

> **Note**
>
> A `GenericAlias` object with [typing.ParamSpec](https://docs.python.org/3.15/library/typing.html#typing.ParamSpec) parameters may not
> have correct `__parameters__` after substitution because
> [typing.ParamSpec](https://docs.python.org/3.15/library/typing.html#typing.ParamSpec) is intended primarily for static type checking.

## Çözümlü kısa örnek

Henüz bağlanmamış benzersiz type variablelar listelenir

```python
from typing import TypeVar
T=TypeVar("T")
print(repr(list[T].__parameters__ == (T,)))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.14.3: genericalias.__parameters__ davranışını ayırt et**

#### Önce

[b:2.14](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; henüz bağlanmamış benzersiz type variablelar listelenir

```python
from typing import TypeVar
T=TypeVar("T")
dict[T,T].__parameters__ == (T,)
list[int].__parameters__ == ()
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `True`.
- [ ] Henüz bağlanmamış benzersiz type variablelar listelenir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../genericalias.__unpacked__/README.md)
<!-- learning-task:end -->
