# 9. Classes

Classes provide a means of bundling data and functionality together. Creating a new class creates a new *type* of object, allowing new *instances* of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state.

Compared with other programming languages, Python's class mechanism adds classes with a minimum of new syntax and semantics. It is a mixture of the class mechanisms found in C++ and Modula-3. Python classes provide all the standard features of Object Oriented Programming: the class inheritance mechanism allows multiple base classes, a derived class can override any methods of its base class or classes, and a method can call the method of a base class with the same name. Objects can contain arbitrary amounts and kinds of data. As is true for modules, classes partake of the dynamic nature of Python: they are created at runtime, and can be modified further after creation.

In C++ terminology, normally class members (including the data members) are *public* (except see below Private Variables), and all member functions are *virtual*. As in Modula-3, there are no shorthands for referencing the object's members from its methods: the method function is declared with an explicit first argument representing the object, which is provided implicitly by the call. As in Smalltalk, classes themselves are objects. This provides semantics for importing and renaming. Unlike C++ and Modula-3, built-in types can be used as base classes for extension by the user. Also, like in C++, most built-in operators with special syntax (arithmetic operators, subscripting etc.) can be redefined for class instances.

(Lacking universally accepted terminology to talk about classes, I will make occasional use of Smalltalk and C++ terms. I would use Modula-3 terms, since its object-oriented semantics are closer to those of Python than C++, but I expect that few readers have heard of it.)


<!-- learning-task:start -->
## Bölüm görevi

**Görev 9: Nesnenin veriyle davranışı nasıl birleştirdiğini çiz**

**Odak:** Sınıf, örnek, nitelik ve metot arasındaki temel ilişki.

### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:4.8](../04-more-control-flow-tools/4.8-defining-functions/README.md).
- Ön bilgi: [t:8.6](../08-errors-and-exceptions/8.6-user-defined-exceptions/README.md).

### Tek görev

1. Kod yazmadan iki ayrı sayaç nesnesi tasarla.

2. Bir çizim veya kısa tabloda ortak türü, her nesnenin ayrı sayı değerini ve değeri artıracak davranışı göster.

3. Bölümdeki class/instance/attribute/method terimlerini çizimdeki parçalara eşleştir.

4. Aynı sınıftan iki örneğin neden aynı nesne olmak zorunda olmadığını açıkla.

### Geçiş ölçütleri

- [ ] Sınıf türü tanımlıyor, iki örnek bu türün ayrı nesneleri.
- [ ] Sayı durum, artırma davranış/metot olarak ayrılmış.
- [ ] Veri ile davranış birlikte modellenmiş; sınıf ile tek bir örneğin kimliği karıştırılmamış.
- [ ] İleri bölümdeki sınıf sözdizimini üretmek gerekmiyor.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md) · [Sıra](../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](9.1-a-word-about-names-and-objects/README.md)
<!-- learning-task:end -->
## Sections

- [9.1. A Word About Names and Objects](9.1-a-word-about-names-and-objects/README.md)
- [9.2. Python Scopes and Namespaces](9.2-python-scopes-and-namespaces/README.md)
- [9.3. A First Look at Classes](9.3-a-first-look-at-classes/README.md)
- [9.4. Random Remarks](9.4-random-remarks/README.md)
- [9.5. Inheritance](9.5-inheritance/README.md)
- [9.6. Private Variables](9.6-private-variables/README.md)
- [9.7. Odds and Ends](9.7-odds-and-ends/README.md)
- [9.8. Iterators](9.8-iterators/README.md)
- [9.9. Generators](9.9-generators/README.md)
- [9.10. Generator Expressions](9.10-generator-expressions/README.md)

<!-- learning-milestone:start -->
## Klasör milestone görevi

**Milestone: Durumu olan, dolaşılabilen küçük bir koleksiyon yap**

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Nesne sahipliği, metot, iterator/generator ve kalıtımı birlikte kullanma.

### Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

### Tek görev

1. ReadingList sınıfında owner ve entries listesi örnek üzerinde tutulsun. add(title) ve `__iter__` içinde yield ile öğe dolaşımı olsun.

2. İki nesnenin bağımsızlığını göster.

3. TaggedReadingList alt sınıfı add davranışını önce etiketi ekleyip sonra üst add metodunu açık çağırarak genişletsin.

4. Generator expressionla başlık uzunluklarının toplamını al.

5. Son bir izde tükenen generator, yeni iter çağrısı ve kaydedilmiş bound method davranışını kendi nesnelerin üzerinden açıkla.

### Geçiş ölçütleri

- [ ] İki liste veri paylaşmıyor; alt sınıf eklemesi yalnız hedef örneğe gidiyor.
- [ ] for ile ekleme sırası korunuyor; tükenmiş generator yeniden değer üretmiyor.
- [ ] Yeni iter yeni generator üretebiliyor; bunun kendini döndüren tüketilmiş iterator örneğinden farkı açıklanmış.
- [ ] Toplam gerçek başlıklardan hesaplanıyor.
- [ ] Nitelik, metot ve modül kapsamı ayrılmış; private isimlerin erişim güvenliği sağlamadığı kaynak sınırıyla belirtilmiş.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md) · [Sıra](../../TASKS.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../10-brief-tour-of-the-standard-library/10.1-operating-system-interface/README.md)
<!-- learning-milestone:end -->
