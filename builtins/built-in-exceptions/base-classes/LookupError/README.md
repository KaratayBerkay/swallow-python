## `LookupError`

```
LookupError
```

The base class for the exceptions that are raised when a key or index used on
a mapping or sequence is invalid: [IndexError](../../concrete-exceptions/IndexError/README.md), [KeyError](../../concrete-exceptions/KeyError/README.md).  This
can be raised directly by [codecs.lookup()](https://docs.python.org/3.15/library/codecs.html#codecs.lookup).

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.3.5: LookupError teşhisini gerekçelendir**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Verilen olay: KeyError, IndexError ve ValueError örnekleri. Beklenen hata türünü veya normal sonucu çıkar. Sistem olayıysa yalnız yazılı teşhis yap; gerçek arıza üretme. Basit veri işlemi ise küçük yerel örnekle doğrula. Bu türün neden uygun olduğunu, yakın ama farklı bir durumdan nasıl ayrıldığını açıkla.

#### Geçiş ölçütleri

- [ ] İlk ikisi LookupError kolundadır; üçüncüsü değildir.
- [ ] Sadece hata adı değil, tetikleyici koşul ve ilgili yakalama sınırı gerekçelendirilmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
