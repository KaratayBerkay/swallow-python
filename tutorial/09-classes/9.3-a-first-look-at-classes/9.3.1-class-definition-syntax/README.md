### 9.3.1. Class Definition Syntax

The simplest form of class definition looks like this:

``` python
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```
> Code: [class_name.py](class_name.py)

Class definitions, like function definitions (`def` statements) must be executed before they have any effect. (You could conceivably place a class definition in a branch of an `if` statement, or inside a function.)

In practice, the statements inside a class definition will usually be function definitions, but other statements are allowed, and sometimes useful --- we'll come back to this later. The function definitions inside a class normally have a peculiar form of argument list, dictated by the calling conventions for methods --- again, this is explained later.

When a class definition is entered, a new namespace is created, and used as the local scope --- thus, all assignments to local variables go into this new namespace. In particular, function definitions bind the name of the new function here.

When a class definition is left normally (via the end), a *class object* is created. This is basically a wrapper around the contents of the namespace created by the class definition; we'll learn more about class objects in the next section. The original local scope (the one in effect just before the class definition was entered) is reinstated, and the class object is bound here to the class name given in the class definition header (`ClassName` in the example).

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 9.3.1: Sınıf gövdesinin ne zaman yürüdüğünü göster**

**Odak:** class bildiriminin yürütülmesi, yeni namespace ve sınıf adının dış kapsamda bağlanması.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:9.2.1](../../9.2-python-scopes-and-namespaces/9.2.1-scopes-and-namespaces-example/README.md).

##### Tek görev

1. label = "outside" ile başla.

2. Bir class Lesson gövdesinde label = "inside" ve print(label) kullan; gövde bittikten sonra print(label) ile dış değeri göster.

3. Aynı sınıf bildirimini if False içine koyan ayrı bir taslakta sınıfın oluşup oluşmayacağını açıklayıp dene.

4. Bu adımda örnek oluşturma gerekmiyor.

##### Geçiş ölçütleri

- [ ] İlk çıktı inside, sonraki outside.
- [ ] Sınıf gövdesinin atamaları kendi namespace alanında; dış label korunmuş.
- [ ] Sınıf bildirimi yürütülünce dış kapsamda Lesson adı bağlanıyor.
- [ ] False dalındaki tanım yürütülmediği için yeni sınıf bağlanmıyor; class yalnız metin şablonu sayılmamış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../9.3.2-class-objects/README.md)
<!-- learning-task:end -->
