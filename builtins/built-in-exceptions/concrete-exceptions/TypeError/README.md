## `TypeError`

```
TypeError
```

Raised when an operation or function is applied to an object of inappropriate
type.  The associated value is a string giving details about the type mismatch.

This exception may be raised by user code to indicate that an attempted
operation on an object is not supported, and is not meant to be. If an object
is meant to support a given operation but has not yet provided an
implementation, [NotImplementedError](../NotImplementedError/README.md) is the proper exception to raise.

Passing arguments of the wrong type (e.g. passing a [list](../../../built-in-functions/list/README.md) when an
[int](../../../built-in-functions/int/README.md) is expected) should result in a TypeError, but passing
arguments with the wrong value (e.g. a number outside expected boundaries)
should result in a [ValueError](../ValueError/README.md).

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.4.28: TypeError teşhisini gerekçelendir**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Verilen olay: int bekleyen işleme liste verilmesi; doğru türde ama geçersiz değerin verilmesi. Beklenen hata türünü veya normal sonucu çıkar. Sistem olayıysa yalnız yazılı teşhis yap; gerçek arıza üretme. Basit veri işlemi ise küçük yerel örnekle doğrula. Bu türün neden uygun olduğunu, yakın ama farklı bir durumdan nasıl ayrıldığını açıkla.

#### Geçiş ölçütleri

- [ ] İlk durum TypeError; ikinci durum için ValueError veya daha özel değer hatası seçilir.
- [ ] Sadece hata adı değil, tetikleyici koşul ve ilgili yakalama sınırı gerekçelendirilmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../UnboundLocalError/README.md)
<!-- learning-task:end -->
