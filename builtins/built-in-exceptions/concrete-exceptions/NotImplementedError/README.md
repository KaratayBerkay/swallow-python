## `NotImplementedError`

```
NotImplementedError
```

This exception is derived from [RuntimeError](../RuntimeError/README.md).  In user defined base
classes, abstract methods should raise this exception when they require
derived classes to override the method, or while the class is being
developed to indicate that the real implementation still needs to be added.

> **Note**
>
> It should not be used to indicate that an operator or method is not
> meant to be supported at all -- in that case either leave the operator /
> method undefined or, if a subclass, set it to [None](https://docs.python.org/3.15/builtins/constants.html#None).

> **Caution**
>
> NotImplementedError and [NotImplemented](https://docs.python.org/3.15/builtins/constants.html#NotImplemented) are not
> interchangeable. This exception should only be used as described
> above; see [NotImplemented](https://docs.python.org/3.15/builtins/constants.html#NotImplemented) for details on correct usage of
> the built-in constant.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.4.14: NotImplementedError teşhisini gerekçelendir**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Verilen olay: Alt sınıfın gerçekleştirmesi gereken gövdesiz yöntem sözleşmesi. Beklenen hata türünü veya normal sonucu çıkar. Sistem olayıysa yalnız yazılı teşhis yap; gerçek arıza üretme. Basit veri işlemi ise küçük yerel örnekle doğrula. Bu türün neden uygun olduğunu, yakın ama farklı bir durumdan nasıl ayrıldığını açıkla.

#### Geçiş ölçütleri

- [ ] NotImplementedError yükseltilebilir; operatör desteği için döndürülen NotImplemented sabitiyle değiştirilemez.
- [ ] Sadece hata adı değil, tetikleyici koşul ve ilgili yakalama sınırı gerekçelendirilmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../OSError/README.md)
<!-- learning-task:end -->
