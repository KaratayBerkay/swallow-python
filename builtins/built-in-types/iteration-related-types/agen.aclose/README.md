## `agen.aclose`

```
agen.aclose()
```

Returns an awaitable that when run will throw a [GeneratorExit](https://docs.python.org/3.15/builtins/exceptions.html#GeneratorExit) into
the underlying asynchronous generator function at the point where it is
currently suspended (equivalent to calling `athrow(GeneratorExit)`).

If the asynchronous generator function then exits gracefully, is already
closed, or raises [GeneratorExit](https://docs.python.org/3.15/builtins/exceptions.html#GeneratorExit) (by not catching the exception),
then the returned awaitable will raise a [StopIteration](https://docs.python.org/3.15/builtins/exceptions.html#StopIteration) exception.
Any further awaitables returned by subsequent calls to the asynchronous
generator will raise a [StopAsyncIteration](https://docs.python.org/3.15/builtins/exceptions.html#StopAsyncIteration) exception.

If the asynchronous generator yields a value, a [RuntimeError](https://docs.python.org/3.15/builtins/exceptions.html#RuntimeError) is
raised by the awaitable.
If the asynchronous generator raises any other exception, that exception
is propagated to the caller of the awaitable.

If the asynchronous generator has already exited due to an exception or
normal exit, then further calls to `aclose()` will return an awaitable
that does nothing.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.6.11: agen.aclose durum geçişini kanıtla**

#### Önce

[b:2.6](../README.md) ve bu sayfanın açıklama/örnekleri.

Bu görevde verilen durumların yazılı çözümü geçerlidir; ek çalışma ortamı veya harici araç kurulumu gerekmez.

#### Tek görev

Yield noktasındaki async generatora aclose uygulanıp bekleniyor. Normal kapanış, kapanış sırasında yield, farklı hata yayılması ve tekrar kapanışı ayrı durumlar olarak çöz. Sonuçları çağrı -> durulan nokta -> sonraki durum tablosuyla göster.

#### Geçiş ölçütleri

- [ ] GeneratorExit aktarılır; normal kapanış None, yield RuntimeError, farklı hata dışarı yayılır; sonraki anext StopAsyncIteration verir.
- [ ] Çağrı ve tüketim/ilerleme anı birbirinden ayrılmıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
