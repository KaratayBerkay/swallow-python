## 9.4. Random Remarks

If the same attribute name occurs in both an instance and in a class, then attribute lookup prioritizes the instance:

``` python
>>> class Warehouse:
...    purpose = 'storage'
...    region = 'west'
...
>>> w1 = Warehouse()
>>> print(w1.purpose, w1.region)
storage west
>>> w2 = Warehouse()
>>> w2.region = 'east'
>>> print(w2.purpose, w2.region)
storage east
```
> Code: [warehouse.py](warehouse.py)

Data attributes may be referenced by methods as well as by ordinary users ("clients") of an object. In other words, classes are not usable to implement pure abstract data types. In fact, nothing in Python makes it possible to enforce data hiding --- it is all based upon convention. (On the other hand, the Python implementation, written in C, can completely hide implementation details and control access to an object if necessary; this can be used by extensions to Python written in C.)

Clients should use data attributes with care --- clients may mess up invariants maintained by the methods by stamping on their data attributes. Note that clients may add data attributes of their own to an instance object without affecting the validity of the methods, as long as name conflicts are avoided --- again, a naming convention can save a lot of headaches here.

There is no shorthand for referencing data attributes (or other methods!) from within methods. I find that this actually increases the readability of methods: there is no chance of confusing local variables and instance variables when glancing through a method.

Often, the first argument of a method is called `self`. This is nothing more than a convention: the name `self` has absolutely no special meaning to Python. Note, however, that by not following the convention your code may be less readable to other Python programmers, and it is also conceivable that a *class browser* program might be written that relies upon such a convention.

Any function object that is a class attribute defines a method for instances of that class. It is not necessary that the function definition is textually enclosed in the class definition: assigning a function object to a local variable in the class is also ok. For example:

``` python
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g
```
> Code: [f1.py](f1.py)

Now `f`, `g` and `h` are all attributes of class `C` that refer to function objects, and consequently they are all methods of instances of `C` --- `h` being exactly equivalent to `g`. Note that this practice usually only serves to confuse the reader of a program.

Methods may call other methods by using method attributes of the `self` argument:

``` python
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
```
> Code: [init.py](init.py)

Methods may reference global names in the same way as ordinary functions. The global scope associated with a method is the module containing its definition. (A class is never used as a global scope.) While one rarely encounters a good reason for using global data in a method, there are many legitimate uses of the global scope: for one thing, functions and modules imported into the global scope can be used by methods, as well as functions and classes defined in it. Usually, the class containing the method is itself defined in this global scope, and in the next section we'll find some good reasons why a method would want to reference its own class.

Each value is an object, and therefore has a *class* (also called its *type*). It is stored as `object.__class__`.

<!-- learning-task:start -->
### Bölüm görevi

**Görev 9.4: Nitelik aramasının önceliğini izle**

**Odak:** Örnek niteliğinin sınıfı gölgelemesi, self üzerinden metot çağrısı ve sınıf dışındaki fonksiyon.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:9.3.5](../9.3-a-first-look-at-classes/9.3.5-class-and-instance-variables/README.md).
- Ön bilgi: [t:6](../../06-modules/README.md).

#### Tek görev

1. Notebook sınıfının kopyasında bir örneğin category değerini "personal" yap; diğer örnek ve sınıf değerini kontrol et, sonra örnekteki niteliği sil. add_twice metodunun self.add_note çağrısını iki kez kullanmasını sağla.

2. Bölümdeki f1/g/h örneğini hazır iskelet olarak okuyup h ile g ilişkisinin ve metot içinden global ad aramasının nerede gerçekleştiğini açıkla.

#### Geçiş ölçütleri

- [ ] Örnek ataması yalnız bir örneğin sınıf değerini gölgeliyor; del sonrası sınıf değeri tekrar görünüyor.
- [ ] add_twice tek örneğin listesine iki not ekliyor.
- [ ] self sözcüğünün özel anahtar değil anlaşılır adlandırma geleneği olduğu açıklanmış.
- [ ] Sınıfa bağlanan dış fonksiyonun metot olabilmesi ve h/g ortak fonksiyon referansı açıklanmış.
- [ ] Metotların global kapsamı sınıf sözlüğü değil tanımlandıkları modül; `__class__` nesnenin türüyle ilişkilendirilmiş.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../9.5-inheritance/README.md)
<!-- learning-task:end -->
