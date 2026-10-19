## `MemoryError`

```
MemoryError
```

Raised when an operation runs out of memory but the situation may still be
rescued (by deleting some objects).  The associated value is a string indicating
what kind of (internal) operation ran out of memory. Note that because of the
underlying memory management architecture (C's `malloc` function), the
interpreter may not always be able to completely recover from this situation; it
nevertheless raises an exception so that a stack traceback can be printed, in
case a run-away program was the cause.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.4.12: MemoryError teşhisini gerekçelendir**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Verilen olay: Bellek ayırma işleminin başarısız olduğu bildirilmiş bir olay. Beklenen hata türünü veya normal sonucu çıkar. Sistem olayıysa yalnız yazılı teşhis yap; gerçek arıza üretme. Basit veri işlemi ise küçük yerel örnekle doğrula. Bu türün neden uygun olduğunu, yakın ama farklı bir durumdan nasıl ayrıldığını açıkla.

#### Geçiş ölçütleri

- [ ] MemoryError; her durumda tam kurtarma garantisi yoktur; gerçek bellek tüketme deneyi gerekmez.
- [ ] Sadece hata adı değil, tetikleyici koşul ve ilgili yakalama sınırı gerekçelendirilmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../NameError/README.md)
<!-- learning-task:end -->
