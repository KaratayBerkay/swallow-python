## `generator.close`

```
generator.close()
```

Raises a [GeneratorExit](https://docs.python.org/3.15/builtins/exceptions.html#GeneratorExit) exception at the point where the generator
function is currently suspended (equivalent to calling `throw(GeneratorExit)`).

If the generator function has already exited (due to an exception or
normal return), or raises [GeneratorExit](https://docs.python.org/3.15/builtins/exceptions.html#GeneratorExit) (by not catching the
exception), `close()` returns [None](https://docs.python.org/3.15/builtins/constants.html#None).
If the generator yields a value, a [RuntimeError](https://docs.python.org/3.15/builtins/exceptions.html#RuntimeError) is raised.
If the generator raises any other exception, it is propagated to the caller.
If a generator returns a value upon being closed, that value is returned
by `close()`.

When a generator iterator is garbage collected before it has exited,
close() is called automatically.

> *Changed in version 3.13:* If a generator returns a value upon being closed, the value is returned
> by `close()`.
> Previously, it returned `None`.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.6.7: generator.close durum geçişini kanıtla**

#### Önce

[b:2.6](../README.md) ve bu sayfanın açıklama/örnekleri.

Sürüm: Python 3.13 veya üzeri. Daha eski yorumlayıcıda yalnız bu sürüme bağlı kısmı gerekçeli yazılı iz ile çözebilirsin; çalıştırma kanıtını bekleyen olarak kaydet.

#### Tek görev

Yield noktasında durdurulmuş üç generator düşün: A GeneratorExit ile normal sonlanıyor; B GeneratorExit yakalayıp yeni bir değer yield ediyor; C yakalayıp return 7 yapıyor. Close sonuçlarını ve tekrar close çağrısını izle. Sonuçları çağrı -> durulan nokta -> sonraki durum tablosuyla göster.

#### Geçiş ölçütleri

- [ ] A None, B RuntimeError; C Python 3.13+ için 7 döndürür; kapalı generator close None olur.
- [ ] Çağrı ve tüketim/ilerleme anı birbirinden ayrılmıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../agen.__anext__/README.md)
<!-- learning-task:end -->
