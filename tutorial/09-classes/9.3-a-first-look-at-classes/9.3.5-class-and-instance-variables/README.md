### 9.3.5. Class and Instance Variables

Generally speaking, instance variables are for data unique to each instance and class variables are for attributes and methods shared by all instances of the class:

``` python
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind                  # shared by all dogs
'canine'
>>> e.kind                  # shared by all dogs
'canine'
>>> d.name                  # unique to d
'Fido'
>>> e.name                  # unique to e
'Buddy'
```
> Code: [init.py](init.py)

As discussed in A Word About Names and Objects, shared data can have possibly surprising effects involving mutable objects such as lists and dictionaries. For example, the *tricks* list in the following code should not be used as a class variable because just a single list would be shared by all *Dog* instances:

``` python
class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks                # unexpectedly shared by all dogs
['roll over', 'play dead']
```
> Code: [init_2.py](init_2.py)

Correct design of the class should use an instance variable instead:

``` python
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']
```
> Code: [init_3.py](init_3.py)

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 9.3.5: Örneklere ait listeyi paylaşmaktan kurtar**

**Odak:** Ortak sınıf değişkeni, ayrı örnek değişkeni ve değiştirilebilir sınıf verisi.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:9.3.4](../9.3.4-method-objects/README.md).
- Ön bilgi: [t:4.9.1](../../../04-more-control-flow-tools/4.9-more-on-defining-functions/4.9.1-default-argument-values/README.md).

##### Tek görev

1. Bir Notebook sınıfında category = "study", notes = [] ve add_note metodu olsun.

2. İki nesne üzerinden farklı notlar ekleyip paylaşım hatasını göster.

3. Sonra notes listesini her örneğe ayrı oluşturacak biçimde düzelt; category sınıfta kalsın.

4. Aynı çağrıları yeni nesnelerle tekrar yap.

##### Geçiş ölçütleri

- [ ] İlk sürümde iki örnek aynı iki notu görüyor.
- [ ] Düzeltilmiş sürümde her örnek yalnız kendi notunu görüyor.
- [ ] category ortak sınıf verisi olarak korunmuş.
- [ ] Sorun append işlemiyle ortak nesnenin değişmesi üzerinden açıklanmış; yalnız sonuç listesi elle değiştirilmemiş.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
