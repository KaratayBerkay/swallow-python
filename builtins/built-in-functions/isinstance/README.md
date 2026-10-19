## `isinstance()`

```
isinstance(object, classinfo, /)
```

Return `True` if the *object* argument is an instance of the *classinfo*
argument, or of a (direct, indirect, or `virtual`) subclass thereof.  If *object* is not
an object of the given type, the function always returns `False`.
If *classinfo* is a tuple of type objects (or recursively, other such
tuples) or a [Union Type](https://docs.python.org/3.15/builtins/stdtypes.html#types-union) of multiple types, return `True` if
*object* is an instance of any of the types.
If *classinfo* is not a type or tuple of types and such tuples,
a [TypeError](https://docs.python.org/3.15/builtins/exceptions.html#TypeError) exception is raised. [TypeError](https://docs.python.org/3.15/builtins/exceptions.html#TypeError) may not be
raised for an invalid type if an earlier check succeeds.

> *Changed in version 3.10:* *classinfo* can be a [Union Type](https://docs.python.org/3.15/builtins/stdtypes.html#types-union).

## Çözümlü kısa örnek

Alt sınıf ilişkisini tam tür eşitliğiyle karıştırma.

```python
print(repr(isinstance(3,int)))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.38: isinstance davranışını ayırt et**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; alt sınıf ilişkisini tam tür eşitliğiyle karıştırma.

```python
isinstance(True,int)
isinstance("x",(int,str))
type(True) is int
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `True`; `False`.
- [ ] Alt sınıf ilişkisini tam tür eşitliğiyle karıştırma.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../issubclass/README.md)
<!-- learning-task:end -->
