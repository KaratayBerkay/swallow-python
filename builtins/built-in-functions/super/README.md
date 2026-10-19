## `super()`

```
super()
super(type, object_or_type=None, /)
```

Return a proxy object that delegates method calls to a parent or sibling
class of *type*.  This is useful for accessing inherited methods that have
been overridden in a class.

The *object_or_type* determines the [method resolution order](https://docs.python.org/3.15/glossary.html#term-method-resolution-order)
to be searched.  The search starts from the class right after the
*type*.

For example, if [__mro__](https://docs.python.org/3.15/reference/datamodel.html#type.__mro__) of *object_or_type* is
`D -> B -> C -> A -> object` and the value of *type* is `B`,
then `super()` searches `C -> A -> object`.

The [__mro__](https://docs.python.org/3.15/reference/datamodel.html#type.__mro__) attribute of the class corresponding to
*object_or_type* lists the method resolution search order used by both
[getattr()](../getattr/README.md) and `super()`.  The attribute is dynamic and can change
whenever the inheritance hierarchy is updated.

If the second argument is omitted, the super object returned is unbound.  If
the second argument is an object, `isinstance(obj, type)` must be true.  If
the second argument is a type, `issubclass(type2, type)` must be true (this
is useful for classmethods).

When called directly within an ordinary method of a class, both arguments may
be omitted ("zero-argument `super()`"). In this case, *type* will be the
enclosing class, and *obj* will be the first argument of the immediately
enclosing function (typically `self`). (This means that zero-argument
`super()` will not work as expected within nested functions, including
generator expressions, which implicitly create nested functions.)

There are two typical use cases for *super*.  In a class hierarchy with
single inheritance, *super* can be used to refer to parent classes without
naming them explicitly, thus making the code more maintainable.  This use
closely parallels the use of *super* in other programming languages.

The second use case is to support cooperative multiple inheritance in a
dynamic execution environment.  This use case is unique to Python and is
not found in statically compiled languages or languages that only support
single inheritance.  This makes it possible to implement "diamond diagrams"
where multiple base classes implement the same method.  Good design dictates
that such implementations have the same calling signature in every case (because the
order of calls is determined at runtime, because that order adapts
to changes in the class hierarchy, and because that order can include
sibling classes that are unknown prior to runtime).

For both use cases, a typical superclass call looks like this:

``` python
class C(B):
    def method(self, arg):
        super().method(arg)    # This does the same thing as:
                               # super(C, self).method(arg)
```

In addition to method lookups, `super()` also works for attribute
lookups.  One possible use case for this is calling [descriptors](https://docs.python.org/3.15/glossary.html#term-descriptor)
in a parent or sibling class.

Note that `super()` is implemented as part of the binding process for
explicit dotted attribute lookups such as `super().__getitem__(name)`.
It does so by implementing its own [__getattribute__()](https://docs.python.org/3.15/reference/datamodel.html#object.__getattribute__) method
for searching
classes in a predictable order that supports cooperative multiple inheritance.
Accordingly, `super()` is undefined for implicit lookups using statements or
operators such as `super()[name]`.

Also note that, aside from the zero argument form, `super()` is not
limited to use inside methods.  The two argument form specifies the
arguments exactly and makes the appropriate references.  The zero
argument form only works inside a class definition, as the compiler fills
in the necessary details to correctly retrieve the class being defined,
as well as accessing the current instance for ordinary methods.

For practical suggestions on how to design cooperative classes using
`super()`, see [guide to using super()](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/).

> *Changed in version 3.14:*
>
> super
>
>  objects are now
>
> pickleable
>
>  and
>
> [copyable](https://docs.python.org/3.15/library/copy.html#module-copy).

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.68: super sözleşmesini uygula**

#### Önce

[t:9.5](../../../tutorial/09-classes/9.5-inheritance/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

`A -> object`, `B -> A`, `C -> A`, `D -> B, C` sınıflarını kur. Her sınıfın aynı adlı yöntemi kendi harfini kaydetsin ve A dışındakiler `super()` ile devam etsin. D örneğinde çağrı sırasını kanıtla.

#### Geçiş ölçütleri

- [ ] Sıra D, B, C, A olur; B içindeki super doğrudan A demek değildir.
- [ ] Arama D örneğinin MRO sırasına göre çağrının tanımlandığı sınıftan sonra sürer.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../type/README.md)
<!-- learning-task:end -->
