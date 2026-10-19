## 9.1. A Word About Names and Objects

Objects have individuality, and multiple names (in multiple scopes) can be bound to the same object. This is known as aliasing in other languages. This is usually not appreciated on a first glance at Python, and can be safely ignored when dealing with immutable basic types (numbers, strings, tuples). However, aliasing has a possibly surprising effect on the semantics of Python code involving mutable objects such as lists, dictionaries, and most other types. This is usually used to the benefit of the program, since aliases behave like pointers in some respects. For example, passing an object is cheap since only a pointer is passed by the implementation; and if a function modifies an object passed as an argument, the caller will see the change --- this eliminates the need for two different argument passing mechanisms as in Pascal.

<!-- learning-task:start -->
### Bölüm görevi

**Görev 9.1: İki adın ortak nesneye etkisini izle**

**Odak:** Ad bağlama, alias ve değiştirilebilir nesnenin paylaşılması.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:3.1.3](../../03-an-informal-introduction-to-python/3.1-using-python-as-a-calculator/3.1.3-lists/README.md).
- Ön bilgi: [t:4.8](../../04-more-control-flow-tools/4.8-defining-functions/README.md).

#### Tek görev

1. original = [1], alias = original kur.

2. Listeyi parametre alıp append ile değiştiren bir fonksiyon çağır; ardından alias adını [9] listesine yeniden bağla.

3. Her olaydan sonra iki adın hangi nesneyi gösterdiğini çiz.

4. Aynı akışta sayı parametresine yeni değer atamanın çağıranın sayısını neden değiştirmediğini göster.

#### Geçiş ölçütleri

- [ ] Fonksiyon içindeki append her iki ad üzerinden görülüyor.
- [ ] alias yeniden bağlanınca original eski listeyi koruyor.
- [ ] Atama yeni nesne kopyalama olarak yorumlanmamış.
- [ ] Fonksiyon parametresinin de bir ad olduğu ve mutation/rebinding farkı açıklanmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../9.2-python-scopes-and-namespaces/README.md)
<!-- learning-task:end -->
