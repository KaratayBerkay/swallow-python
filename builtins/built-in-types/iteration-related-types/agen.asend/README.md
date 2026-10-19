## `agen.asend`

```
agen.asend(value)
```

Returns an awaitable which, when run, "sends" a value into the underlying
asynchronous generator function: the *value* argument becomes
the result of the current yield expression.

Otherwise, this method behaves like [__anext__()](../agen.__anext__/README.md): when the
returned awaitable runs, it resumes the underlying function and either
returns the next yielded value as the value of the raised
[StopIteration](https://docs.python.org/3.15/builtins/exceptions.html#StopIteration), or raises [StopAsyncIteration](https://docs.python.org/3.15/builtins/exceptions.html#StopAsyncIteration).

When `asend()` is called to start the asynchronous
generator, it must be called with [None](https://docs.python.org/3.15/builtins/constants.html#None) as the argument,
because there is no yield expression that could receive the value.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.6.9: agen.asend durum geçişini kanıtla**

#### Önce

[b:2.6](../README.md) ve bu sayfanın açıklama/örnekleri.

Bu görevde verilen durumların yazılı çözümü geçerlidir; ek çalışma ortamı veya harici araç kurulumu gerekmez.

#### Tek görev

Async generator `x = yield 4` satırında duruyor; sonraki ifade `yield x+1`. asend(7) awaitableı beklendiğinde ne olur? Başlatılmamış örnekte asend(7) ile karşılaştır. Sonuçları çağrı -> durulan nokta -> sonraki durum tablosuyla göster.

#### Geçiş ölçütleri

- [ ] Durmuş örnek x=7 ile 8 üretir; yeni generator non-None ile başlatılamaz.
- [ ] Çağrı ve tüketim/ilerleme anı birbirinden ayrılmıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../agen.athrow/README.md)
<!-- learning-task:end -->
