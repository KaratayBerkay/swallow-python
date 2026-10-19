## `@staticmethod`

```
staticmethod
```

Transform a method into a static method.

A static method does not receive an implicit first argument. To declare a static
method, use this idiom:

``` python
class C:
    @staticmethod
    def f(arg1, arg2, argN): ...
```

The `@staticmethod` form is a function [decorator](https://docs.python.org/3.15/glossary.html#term-decorator) -- see
[Function definitions](https://docs.python.org/3.15/reference/compound_stmts.html#function) for details.

A static method can be called either on the class (such as `C.f()`) or on
an instance (such as `C().f()`).
Moreover, the static method [descriptor](https://docs.python.org/3.15/glossary.html#term-descriptor) is also callable, so it can
be used in the class definition (such as `f()`).

Static methods in Python are similar to those found in Java or C++. Also, see
[classmethod](../classmethod/README.md) for a variant that is useful for creating alternate class
constructors.

Like all decorators, it is also possible to call `staticmethod` as
a regular function and do something with its result.  This is needed
in some cases where you need a reference to a function from a class
body and you want to avoid the automatic transformation to instance
method.  For these cases, use this idiom:

``` python
def regular_function():
    ...

class C:
    method = staticmethod(regular_function)
```

For more information on static methods, see [The standard type hierarchy](https://docs.python.org/3.15/reference/datamodel.html#types).

> *Changed in version 3.10:* Static methods now inherit the method attributes
> ([__module__](https://docs.python.org/3.15/reference/datamodel.html#function.__module__), [__name__](https://docs.python.org/3.15/reference/datamodel.html#function.__name__),
> [__qualname__](https://docs.python.org/3.15/reference/datamodel.html#function.__qualname__), [__doc__](https://docs.python.org/3.15/reference/datamodel.html#function.__doc__) and
> [__annotations__](https://docs.python.org/3.15/reference/datamodel.html#function.__annotations__)), have a new `__wrapped__` attribute,
> and are now callable as regular functions.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.65: staticmethod sözleşmesini uygula**

#### Önce

[t:9.5](../../../tutorial/09-classes/9.5-inheritance/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

`Donustur` sınıfına iki sayının toplamını veren bir staticmethod ekle. Sınıftan ve örnekten çağır. Aynı parametre listesine sıradan yöntem dekoratörsüz bırakılırsa örnek üzerinden neden farklı bağlandığını açıkla.

#### Geçiş ölçütleri

- [ ] Her iki staticmethod çağrısı aynı sonucu üretir; self veya cls örtük eklenmez.
- [ ] Örnek üzerinden normal yöntemde örtük ilk argüman farkı gösterilmiştir.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../sum/README.md)
<!-- learning-task:end -->
