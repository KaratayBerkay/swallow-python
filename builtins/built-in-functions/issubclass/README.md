## `issubclass()`

```
issubclass(cls, classinfo, /)
```

Return `True` if *cls* is a subclass (direct, indirect, or [virtual](https://docs.python.org/3.15/glossary.html#term-abstract-base-class)) of *classinfo*.  A
class is considered a subclass of itself. *classinfo* may be a tuple of class
objects (or recursively, other such tuples)
or a [Union Type](https://docs.python.org/3.15/builtins/stdtypes.html#types-union), in which case return `True` if *cls* is a
subclass of any entry in *classinfo*.  In any other case, a [TypeError](https://docs.python.org/3.15/builtins/exceptions.html#TypeError)
exception is raised.

> *Changed in version 3.10:* *classinfo* can be a [Union Type](https://docs.python.org/3.15/builtins/stdtypes.html#types-union).

## Çözümlü kısa örnek

Sınıf ilişkisi denetiminde örnek yerine sınıf vermek gerekir.

```python
print(repr(issubclass(int,object)))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.39: issubclass davranışını ayırt et**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; sınıf ilişkisi denetiminde örnek yerine sınıf vermek gerekir.

```python
issubclass(bool,int)
issubclass(int,bool)
issubclass(3,int)
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `False`; `TypeError`.
- [ ] Sınıf ilişkisi denetiminde örnek yerine sınıf vermek gerekir.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../iter/README.md)
<!-- learning-task:end -->
