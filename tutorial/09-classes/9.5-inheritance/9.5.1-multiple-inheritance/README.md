### 9.5.1. Multiple Inheritance

Python supports a form of multiple inheritance as well. A class definition with multiple base classes looks like this:

``` python
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```
> Code: [derived_class_name.py](derived_class_name.py)

For most purposes, in the simplest cases, you can think of the search for attributes inherited from a parent class as depth-first, left-to-right, not searching twice in the same class where there is an overlap in the hierarchy. Thus, if an attribute is not found in `DerivedClassName`, it is searched for in `Base1`, then (recursively) in the base classes of `Base1`, and if it was not found there, it was searched for in `Base2`, and so on.

In fact, it is slightly more complex than that; the method resolution order changes dynamically to support cooperative calls to `super()`. This approach is known in some other multiple-inheritance languages as call-next-method and is more powerful than the super call found in single-inheritance languages.

Dynamic ordering is necessary because all cases of multiple inheritance exhibit one or more diamond relationships (where at least one of the parent classes can be accessed through multiple paths from the bottommost class). For example, all classes inherit from `object`, so any case of multiple inheritance provides more than one path to reach `object`. To keep the base classes from being accessed more than once, the dynamic algorithm linearizes the search order in a way that preserves the left-to-right ordering specified in each class, that calls each parent only once, and that is monotonic (meaning that a class can be subclassed without affecting the precedence order of its parents). Taken together, these properties make it possible to design reliable and extensible classes with multiple inheritance. For more detail, see The Python 2.3 Method Resolution Order.

In some cases multiple inheritance is not allowed; see Multiple inheritance for details.

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 9.5.1: Elmas hiyerarşide arama sırasını çıkar**

**Odak:** Çoklu kalıtım, soldan sağa öncelik, ortak atanın tek kez sıralanması ve monotonic düzen.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:9.5](../README.md).

##### Tek görev

1. A sınıfında label = "A"; B(A) içinde yeni nitelik yok; C(A) içinde label = "C"; D(B, C) olsun.

2. D().label değerinin B üzerinden doğrudan A seçilerek bulunup bulunamayacağını bölümdeki ortak atanın tek kez ve alt sınıflardan sonra sıralanması kuralıyla açıkla, sonra dene.

3. B içine label = "B" eklenince sonucu yeniden çıkar.

4. Bu adımda cooperative super zinciri yazman gerekmiyor.

##### Geçiş ölçütleri

- [ ] İlk sonuç C; B üzerinde değer yokken ortak A, C önüne yanlışlıkla alınmamış.
- [ ] İkinci sonuç B; D taban sırası B sonra C olarak etkili.
- [ ] Ortak A iki kez aranacak biçimde sıralanmamış; B/C öncelikleri korunmuş.
- [ ] Basit depth-first sezgisinin elmas durumda yeterli olmadığı somut örnekle açıklanmış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
