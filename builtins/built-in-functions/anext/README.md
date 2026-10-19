## `anext()`

```
anext(async_iterator, /)
anext(async_iterator, default, /)
```

When awaited, return the next item from the given `asynchronous
iterator`, or *default* if given and the iterator is [exhausted](https://docs.python.org/3.15/glossary.html#term-exhausted).

This is the async variant of the [next()](../next/README.md) builtin, and behaves
similarly.

This calls the [__anext__()](https://docs.python.org/3.15/reference/datamodel.html#object.__anext__) method of *async_iterator*,
returning an [awaitable](https://docs.python.org/3.15/glossary.html#term-awaitable). Awaiting this returns the next value of the
iterator. If *default* is given, it is returned if the iterator is exhausted,
otherwise [StopAsyncIteration](https://docs.python.org/3.15/builtins/exceptions.html#StopAsyncIteration) is raised.

> *Added in version 3.10.*

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.4: anext sözleşmesini uygula**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

Bu görevde verilen durumların yazılı çözümü geçerlidir; ek çalışma ortamı veya harici araç kurulumu gerekmez.

#### Tek görev

Bir async iterator ilk beklemede 7, ikincide 9 veriyor, sonra StopAsyncIteration bildiriyor. Üç `await anext(it)` çağrısını izle. Yeni bir iterator için üçüncü çağrıyı `await anext(it, "SON")` yap ve sonucu karşılaştır.

#### Geçiş ölçütleri

- [ ] Sıra 7, 9, StopAsyncIteration; default verilirse son sonuç "SON".
- [ ] Çağrı awaitable üretir; öğe veya tükenme, bu awaitable beklendiğinde ortaya çıkar.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../any/README.md)
<!-- learning-task:end -->
