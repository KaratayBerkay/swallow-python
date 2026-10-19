## `ModuleNotFoundError`

```
ModuleNotFoundError
```

A subclass of [ImportError](../ImportError/README.md) which is raised by `import`
when a module could not be located.  It is also raised when `None`
is found in [sys.modules](https://docs.python.org/3.15/library/sys.html#sys.modules).

> *Added in version 3.6.*

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.4.7: ModuleNotFoundError teşhisini gerekçelendir**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Verilen olay: Import sisteminin modülü hiç bulamaması. Beklenen hata türünü veya normal sonucu çıkar. Sistem olayıysa yalnız yazılı teşhis yap; gerçek arıza üretme. Basit veri işlemi ise küçük yerel örnekle doğrula. Bu türün neden uygun olduğunu, yakın ama farklı bir durumdan nasıl ayrıldığını açıkla.

#### Geçiş ölçütleri

- [ ] ModuleNotFoundError, ImportError alt türüdür; modül içindeki her hata modül yokluğu demek değildir.
- [ ] Sadece hata adı değil, tetikleyici koşul ve ilgili yakalama sınırı gerekçelendirilmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../ImportCycleError/README.md)
<!-- learning-task:end -->
