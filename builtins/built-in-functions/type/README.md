## `type()`

```
type(object, /)
type(name, bases, dict, /, **kwargs)
```

With one argument, return the type of an *object*.  The return value is a
type object and generally the same object as returned by
[object.__class__](https://docs.python.org/3.15/reference/datamodel.html#object.__class__).

The [isinstance()](../isinstance/README.md) built-in function is recommended for testing the type
of an object, because it takes subclasses into account.

With three arguments, return a new type object.  This is essentially a
dynamic form of the `class` statement. The *name* string is
the class name and becomes the [__name__](https://docs.python.org/3.15/reference/datamodel.html#type.__name__) attribute.
The *bases* tuple contains the base classes and becomes the
[__bases__](https://docs.python.org/3.15/reference/datamodel.html#type.__bases__) attribute; if empty, [object](../object/README.md), the
ultimate base of all classes, is added.  The *dict* dictionary contains
attribute and method definitions for the class body; it may be copied
or wrapped before becoming the [__dict__](https://docs.python.org/3.15/reference/datamodel.html#type.__dict__) attribute.
The following two statements create identical type objects:

``` python
>>> class X:
...     a = 1
...
>>> X = type('X', (), dict(a=1))
```
> Code: [example_01.py](example_01.py)

See also:

- [Documentation on attributes and methods on classes](https://docs.python.org/3.15/reference/datamodel.html#class-attrs-and-methods).

- [Type Objects](https://docs.python.org/3.15/builtins/stdtypes.html#bltin-type-objects)

Keyword arguments provided to the three argument form are passed to the
appropriate metaclass machinery (usually [__init_subclass__()](https://docs.python.org/3.15/reference/datamodel.html#object.__init_subclass__))
in the same way that keywords in a class
definition (besides *metaclass*) would.

Unlike a `class` statement, the three argument form does not
call the metaclass `__prepare__` method (see [Preparing the class namespace](https://docs.python.org/3.15/reference/datamodel.html#prepare)).  Use
[types.new_class()](https://docs.python.org/3.15/library/types.html#types.new_class) to dynamically create a class using the
appropriate metaclass.

See also [Customizing class creation](https://docs.python.org/3.15/reference/datamodel.html#class-customization).

> *Changed in version 3.6:* Subclasses of type which don't override `type.__new__` may no
> longer use the one-argument form to get the type of an object.

> *Changed in version 3.15:* *dict* can now be a [frozendict](../frozendict/README.md).

## Çözümlü kısa örnek

Tek argüman türü bulur; üç argüman sınıf oluşturur.

```python
print(repr(type(3) is int))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.70: type davranışını ayırt et**

#### Önce

[t:9.5](../../../tutorial/09-classes/9.5-inheritance/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; tek argüman türü bulur; üç argüman sınıf oluşturur.

```python
type(True) is int
type("K",(),{"puan":4})().puan
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `False`; `4`.
- [ ] Tek argüman türü bulur; üç argüman sınıf oluşturur.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../vars/README.md)
<!-- learning-task:end -->
