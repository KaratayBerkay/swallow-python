## `RecursionError`

```
RecursionError
```

This exception is derived from [RuntimeError](../RuntimeError/README.md).  It is raised when the
interpreter detects that the maximum recursion depth (see
[sys.getrecursionlimit()](https://docs.python.org/3.15/library/sys.html#sys.getrecursionlimit)) is exceeded.

> *Added in version 3.5:* Previously, a plain [RuntimeError](../RuntimeError/README.md) was raised.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.4.18: RecursionError teşhisini gerekçelendir**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Verilen olay: Interpreterın izin verilen recursion derinliğinin aşıldığını saptaması. Beklenen hata türünü veya normal sonucu çıkar. Sistem olayıysa yalnız yazılı teşhis yap; gerçek arıza üretme. Basit veri işlemi ise küçük yerel örnekle doğrula. Bu türün neden uygun olduğunu, yakın ama farklı bir durumdan nasıl ayrıldığını açıkla.

#### Geçiş ölçütleri

- [ ] RecursionError, RuntimeError alt türüdür; limiti değiştirme veya gerçek taşma üretme gerekmez.
- [ ] Sadece hata adı değil, tetikleyici koşul ve ilgili yakalama sınırı gerekçelendirilmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../ReferenceError/README.md)
<!-- learning-task:end -->
