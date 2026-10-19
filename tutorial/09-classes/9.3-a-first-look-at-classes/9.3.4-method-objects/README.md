### 9.3.4. Method Objects

Usually, a method is called right after it is bound:

``` python
x.f()
```
> Code: [example_01.py](example_01.py)

If `x = MyClass()`, as above, this will return the string `'hello world'`. However, it is not necessary to call a method right away: `x.f` is a method object, and can be stored away and called at a later time. For example:

``` python
xf = x.f
while True:
    print(xf())
```
> Code: [xf.py](xf.py)

will continue to print `hello world` until the end of time.

What exactly happens when a method is called? You may have noticed that `x.f()` was called without an argument above, even though the function definition for `f()` specified an argument. What happened to the argument? Surely Python raises an exception when a function that requires an argument is called without any --- even if the argument isn't actually used...

Actually, you may have guessed the answer: the special thing about methods is that the instance object is passed as the first argument of the function. In our example, the call `x.f()` is exactly equivalent to `MyClass.f(x)`. In general, calling a method with a list of *n* arguments is equivalent to calling the corresponding function with an argument list that is created by inserting the method's instance object before the first argument.

In general, methods work as follows. When a non-data attribute of an instance is referenced, the instance's class is searched. If the name denotes a valid class attribute that is a function object, references to both the instance object and the function object are packed into a method object. When the method object is called with an argument list, a new argument list is constructed from the instance object and the argument list, and the function object is called with this new argument list.

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 9.3.4: Kaydedilen metodun hangi nesneye bağlı kaldığını göster**

**Odak:** Bağlı metot, self argümanının eklenmesi ve sonradan çağırma.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:9.3.3](../9.3.3-instance-objects/README.md).

##### Tek görev

1. name alanını tutan ve read(self) ile döndüren küçük sınıf yaz. a ve b örneklerini oluştur; saved = a.read kaydet, a adını b nesnesine yeniden bağla. saved(), a.read() ve ClassName.read(b) sonuçlarını karşılaştır. saved oluşturulması sırasında read gövdesinin çalışıp çalışmadığını açıkla.

##### Geçiş ölçütleri

- [ ] saved ilk nesnenin adını, a.read() ikinci nesnenin adını döndürüyor.
- [ ] ClassName.read(b), b.read() ile eşdeğer.
- [ ] Metot kaydında çağrı parantezi yok ve gövde henüz yürümüyor.
- [ ] Nesnenin ilk argüman olarak otomatik eklenmesi ve metot nesnesinin nesne/fonksiyon bağını saklaması açıklanmış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../9.3.5-class-and-instance-variables/README.md)
<!-- learning-task:end -->
