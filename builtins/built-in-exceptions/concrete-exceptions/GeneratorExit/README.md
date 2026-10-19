## `GeneratorExit`

```
GeneratorExit
```

Raised when a [generator](https://docs.python.org/3.15/glossary.html#term-generator) or [coroutine](https://docs.python.org/3.15/glossary.html#term-coroutine) is closed;
see [generator.close()](https://docs.python.org/3.15/builtins/stdtypes.html#generator.close) and [coroutine.close()](https://docs.python.org/3.15/reference/datamodel.html#coroutine.close).  It
directly inherits from [BaseException](../../base-classes/BaseException/README.md) instead of [Exception](../../base-classes/Exception/README.md) since
it is technically not an error.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.4.5: GeneratorExit teşhisini gerekçelendir**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Verilen olay: Yield noktasındaki generatorın close ile kapatılması. Beklenen hata türünü veya normal sonucu çıkar. Sistem olayıysa yalnız yazılı teşhis yap; gerçek arıza üretme. Basit veri işlemi ise küçük yerel örnekle doğrula. Bu türün neden uygun olduğunu, yakın ama farklı bir durumdan nasıl ayrıldığını açıkla.

#### Geçiş ölçütleri

- [ ] GeneratorExit doğrudan BaseException kolundadır; sıradan Exception yakalayıcısı bunu yakalamaz.
- [ ] Sadece hata adı değil, tetikleyici koşul ve ilgili yakalama sınırı gerekçelendirilmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../ImportError/README.md)
<!-- learning-task:end -->
