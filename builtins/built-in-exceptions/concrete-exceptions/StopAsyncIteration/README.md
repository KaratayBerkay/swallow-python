## `StopAsyncIteration`

```
StopAsyncIteration
```

Must be raised by [__anext__()](https://docs.python.org/3.15/reference/datamodel.html#object.__anext__) method of an
[asynchronous iterator](https://docs.python.org/3.15/glossary.html#term-asynchronous-iterator) object to stop the iteration.

> *Added in version 3.5.*

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.4.22: StopAsyncIteration teşhisini gerekçelendir**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Verilen olay: Async iteratorın __anext__ sözleşmesinde öğelerin bitmesi. Beklenen hata türünü veya normal sonucu çıkar. Sistem olayıysa yalnız yazılı teşhis yap; gerçek arıza üretme. Basit veri işlemi ise küçük yerel örnekle doğrula. Bu türün neden uygun olduğunu, yakın ama farklı bir durumdan nasıl ayrıldığını açıkla.

#### Geçiş ölçütleri

- [ ] StopAsyncIteration; normal iteratorın StopIteration türüyle değiştirilmez.
- [ ] Sadece hata adı değil, tetikleyici koşul ve ilgili yakalama sınırı gerekçelendirilmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../SyntaxError/README.md)
<!-- learning-task:end -->
