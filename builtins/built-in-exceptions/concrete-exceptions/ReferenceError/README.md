## `ReferenceError`

```
ReferenceError
```

This exception is raised when a weak reference proxy, created by the
[weakref.proxy()](https://docs.python.org/3.15/library/weakref.html#weakref.proxy) function, is used to access an attribute of the referent
after it has been garbage collected. For more information on weak references,
see the [weakref](https://docs.python.org/3.15/library/weakref.html#module-weakref) module.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.4.19: ReferenceError teşhisini gerekçelendir**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Verilen olay: Referenti toplanmış weak-reference proxy üzerinden nitelik okuma. Beklenen hata türünü veya normal sonucu çıkar. Sistem olayıysa yalnız yazılı teşhis yap; gerçek arıza üretme. Basit veri işlemi ise küçük yerel örnekle doğrula. Bu türün neden uygun olduğunu, yakın ama farklı bir durumdan nasıl ayrıldığını açıkla.

#### Geçiş ölçütleri

- [ ] ReferenceError; sıradan bir değişkenin tanımsız olmasıyla karıştırılmaz.
- [ ] Sadece hata adı değil, tetikleyici koşul ve ilgili yakalama sınırı gerekçelendirilmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../RuntimeError/README.md)
<!-- learning-task:end -->
