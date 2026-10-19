### 9.3.2. Class Objects

Class objects support two kinds of operations: attribute references and instantiation.

*Attribute references* use the standard syntax used for all attribute references in Python: `obj.name`. Valid attribute names are all the names that were in the class's namespace when the class object was created. So, if the class definition looked like this:

``` python
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
```
> Code: [f.py](f.py)

then `MyClass.i` and `MyClass.f` are valid attribute references, returning an integer and a function object, respectively. Class attributes can also be assigned to, so you can change the value of `MyClass.i` by assignment. `__doc__` is also a valid attribute, returning the docstring belonging to the class: `"A simple example class"`.

Class *instantiation* uses function notation. Just pretend that the class object is a parameterless function that returns a new instance of the class. For example (assuming the above class):

``` python
x = MyClass()
```
> Code: [x.py](x.py)

creates a new *instance* of the class and assigns this object to the local variable `x`.

The instantiation operation ("calling" a class object) creates an empty object. Many classes like to create objects with instances customized to a specific initial state. Therefore a class may define a special method named `__init__()`, like this:

``` python
def __init__(self):
    self.data = []
```
> Code: [init.py](init.py)

When a class defines an `__init__()` method, class instantiation automatically invokes `__init__()` for the newly created class instance. So in this example, a new, initialized instance can be obtained by:

``` python
x = MyClass()
```
> Code: [x_2.py](x_2.py)

Of course, the `__init__()` method may have arguments for greater flexibility. In that case, arguments given to the class instantiation operator are passed on to `__init__()`. For example,

``` python
>>> class Complex:
...     def __init__(self, realpart, imagpart):
...         self.r = realpart
...         self.i = imagpart
...
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)
```
> Code: [init_2.py](init_2.py)

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 9.3.2: Sınıftan başlangıç durumu olan nesne üret**

**Odak:** Sınıf nitelikleri, `__doc__`, sınıf çağrısı ve `__init__` argümanları.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:9.3.1](../9.3.1-class-definition-syntax/README.md).

##### Tek görev

1. Bir Point sınıfına kısa docstring, category = "point" sınıf niteliği ve `__init__`(self, x, y) ekle; self.x/self.y atamalarını yap.

2. Point(2, 5) oluşturup koordinatları, Point.category ve `Point.__doc__` değerlerini göster.

3. İkinci bir nesneyi farklı koordinatlarla oluştur; `__init__` ne zaman ve hangi nesne için çalışıyor açıkla.

##### Geçiş ölçütleri

- [ ] İki nesnenin başlangıç koordinatları kendilerine verilen değerler.
- [ ] Sınıfa çağrı yeni örnek oluşturuyor; örnek `__init__` içine ilk argüman olarak geliyor.
- [ ] Sınıf niteliği ve docstring sınıftan erişiliyor.
- [ ] `__init__` çağrının dönüş nesnesi yerine yalnız başlatıcı olarak açıklanmış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../9.3.3-instance-objects/README.md)
<!-- learning-task:end -->
