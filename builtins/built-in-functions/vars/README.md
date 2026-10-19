## `vars()`

```
vars()
vars(object, /)
```

Return the [__dict__](https://docs.python.org/3.15/reference/datamodel.html#object.__dict__) attribute for a module, class, instance,
or any other object with a `__dict__` attribute.

Objects such as modules and instances have an updateable [__dict__](https://docs.python.org/3.15/reference/datamodel.html#object.__dict__)
attribute; however, other objects may have write restrictions on their
`__dict__` attributes (for example, classes use a
[types.MappingProxyType](https://docs.python.org/3.15/library/types.html#types.MappingProxyType) to prevent direct dictionary updates).

Without an argument, vars() acts like [locals()](../locals/README.md).

A [TypeError](https://docs.python.org/3.15/builtins/exceptions.html#TypeError) exception is raised if an object is specified but
it doesn't have a [__dict__](https://docs.python.org/3.15/reference/datamodel.html#object.__dict__) attribute (for example, if
its class defines the `__slots__` attribute).

> *Changed in version 3.13:* The result of calling this function without an argument has been
> updated as described for the [locals()](../locals/README.md) builtin.

## Çözümlü kısa örnek

Nesnenin __dict__ eşlemesiyle nitelik erişimini bağla.

```python
class K: pass
o=K(); o.puan=4
print(repr(vars(o)["puan"]))
# Sonuç: 4
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.71: vars davranışını ayırt et**

#### Önce

[t:9.5](../../../tutorial/09-classes/9.5-inheritance/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; nesnenin __dict__ eşlemesiyle nitelik erişimini bağla.

```python
class K: pass
o=K(); o.puan=4
vars(o) is o.__dict__
vars(3)
```

Sınıf nesnesinin `vars(K)` sonucuna anahtar atamayı örneğin `vars(o)` sonucuna atamayla karşılaştır; bu farkı kaynakta belirtilen salt okunur eşlemeye bağla.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `TypeError`.
- [ ] Nesnenin __dict__ eşlemesiyle nitelik erişimini bağla.

- [ ] Örneğin dict alanı güncellenebilir; sınıfın mappingproxy alanına doğrudan atama TypeError verir.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../zip/README.md)
<!-- learning-task:end -->
