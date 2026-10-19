### 9.3.3. Instance Objects

Now what can we do with instance objects? The only operations understood by instance objects are attribute references. There are two kinds of valid attribute names: data attributes and methods.

*Data attributes* correspond to "instance variables" in Smalltalk, and to "data members" in C++. Data attributes need not be declared; like local variables, they spring into existence when they are first assigned to. For example, if `x` is the instance of `MyClass` created above, the following piece of code will print the value `16`, without leaving a trace:

``` python
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
```
> Code: [example_01.py](example_01.py)

The other kind of instance attribute reference is a *method*. A method is a function that "belongs to" an object.

Valid method names of an instance object depend on its class. By definition, all attributes of a class that are function objects define corresponding methods of its instances. So in our example, `x.f` is a valid method reference, since `MyClass.f` is a function, but `x.i` is not, since `MyClass.i` is not. But `x.f` is not the same thing as `MyClass.f` --- it is a *method object*, not a function object.

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 9.3.3: Örnek niteliğinin oluşmasını ve silinmesini izle**

**Odak:** Veri niteliği, metot niteliği ve sonradan atama/silme.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:9.3.2](../9.3.2-class-objects/README.md).

##### Tek görev

1. README içindeki MyClass tanımını REPL oturumuna al; iki örnek oluştur.

2. Birinciye counter = 1 ekleyip 8 olana kadar ikiyle çarp; ikinciye bu niteliği ekleme.

3. İlk counter değerini göster, del ile kaldır ve iki nesnenin counter erişimlerini ayrı girişlerde dene. x.f, MyClass.f ve x.i nesnelerinin rolünü karşılaştır.

##### Geçiş ölçütleri

- [ ] counter 8 oluyor; ikinci örnekte ve silindikten sonra ilk örnekte erişim başarısız.
- [ ] Niteliğin önceden bildirilmesine gerek olmadığı gösterilmiş.
- [ ] x.i veri niteliği; x.f bağlı metot, MyClass.f fonksiyon olarak ayrılmış.
- [ ] Bir örneğe eklenen veri diğerine kendiliğinden eklenmiyor.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../9.3.4-method-objects/README.md)
<!-- learning-task:end -->
