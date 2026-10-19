## 9.5. Inheritance

Of course, a language feature would not be worthy of the name "class" without supporting inheritance. The syntax for a derived class definition looks like this:

``` python
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```
> Code: [derived_class_name.py](derived_class_name.py)

The name `BaseClassName` must be defined in a namespace accessible from the scope containing the derived class definition. In place of a base class name, other arbitrary expressions are also allowed. This can be useful, for example, when the base class is defined in another module:

``` python
class DerivedClassName(modname.BaseClassName):
```
> Code: [derived_class_name_2.py](derived_class_name_2.py)

Execution of a derived class definition proceeds the same as for a base class. When the class object is constructed, the base class is remembered. This is used for resolving attribute references: if a requested attribute is not found in the class, the search proceeds to look in the base class. This rule is applied recursively if the base class itself is derived from some other class.

There's nothing special about instantiation of derived classes: `DerivedClassName()` creates a new instance of the class. Method references are resolved as follows: the corresponding class attribute is searched, descending down the chain of base classes if necessary, and the method reference is valid if this yields a function object.

Derived classes may override methods of their base classes. Because methods have no special privileges when calling other methods of the same object, a method of a base class that calls another method defined in the same base class may end up calling a method of a derived class that overrides it. (For C++ programmers: all methods in Python are effectively `virtual`.)

An overriding method in a derived class may in fact want to extend rather than simply replace the base class method of the same name. There is a simple way to call the base class method directly: just call `BaseClassName.methodname(self, arguments)`. This is occasionally useful to clients as well. (Note that this only works if the base class is accessible as `BaseClassName` in the global scope.)

Python has two built-in functions that work with inheritance:

- Use `isinstance()` to check an instance's type: `isinstance(obj, int)` will be `True` only if `obj.__class__` is `int` or some class derived from `int`.

- Use `issubclass()` to check class inheritance: `issubclass(bool, int)` is `True` since `bool` is a subclass of `int`. However, `issubclass(float, int)` is `False` since `float` is not a subclass of `int`.


<!-- learning-task:start -->
### Bölüm görevi

**Görev 9.5: Üst metodun çağırdığı alt davranışı izle**

**Odak:** Kalıtım, nitelik arama, override, taban metodu açık çağırma, isinstance/issubclass.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:9.4](../9.4-random-remarks/README.md).

#### Tek görev

1. BaseCounter içinde kind niteliği, describe(self) içinde self.label() çağrısı, label(self) içinde "base" dönüşü olsun.

2. NamedCounter(BaseCounter) yalnız label metodunu "named" döndürecek biçimde değiştirsin.

3. Alt örnekte describe, kind, isinstance ve issubclass sonuçlarını göster.

4. Sonra alt label içinde BaseCounter.label(self) sonucuna ek metin ekleyerek genişlet.

#### Geçiş ölçütleri

- [ ] Alt örnekte describe named döndürüyor; üst gövdedeki self.label alt override buluyor.
- [ ] kind üst sınıftan bulunuyor.
- [ ] Örnek/taban isinstance ve sınıf/taban issubclass doğru; ilgisiz tür karşılaştırması yanlış.
- [ ] Üst metodun açık çağrısında self verilmiş; henüz yalnız adı geçmiş super altyapısı gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](9.5.1-multiple-inheritance/README.md)
<!-- learning-task:end -->
### Sections

- [9.5.1. Multiple Inheritance](9.5.1-multiple-inheritance/README.md)

<!-- learning-milestone:start -->
### Klasör milestone görevi

**Milestone: Kalıtım aramasını durumdan ayrı izle**

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Tek/çoklu kalıtım, override ve örnek türü ilişkilerini birleştirme.

#### Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

#### Tek görev

1. Base içinde run(self) yalnız self.label() döndürsün.

2. Left(Base) boş, Right(Base) label ile "right" döndürsün; Combined(Left, Right) boş olsun.

3. Combined örneğinde run sonucunu önce türet, sonra kontrol et.

4. Left içine label ekleyip değişimi göster; isinstance/issubclass ilişkilerini belirt.

5. Aynı örnekte üst metodun doğrudan çağrısıyla alt override çağrısını karşılaştır.

#### Geçiş ölçütleri

- [ ] İlk sonuç right, Left override sonrası left.
- [ ] Ortak Base erken seçilerek Right atlanmamış.
- [ ] Tür/aile ilişkileri nesne ile sınıf düzeyinde doğru.
- [ ] Üst run içindeki self çağrısının dinamik olarak alt label bulması açıklanmış; MRO listesini ezberden saymak tek kanıt değil.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../9.6-private-variables/README.md)
<!-- learning-milestone:end -->
