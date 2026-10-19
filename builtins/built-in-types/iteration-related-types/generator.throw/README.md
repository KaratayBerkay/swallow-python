## `generator.throw`

```
generator.throw(value)
generator.throw(type[, value[, traceback]])
```

Raises an exception at the point where the generator is currently suspended.

Otherwise, this method behaves like [__next__()](../generator.__next__/README.md): it resumes
the underlying function and either returns the next yielded value or raises
[StopIteration](https://docs.python.org/3.15/builtins/exceptions.html#StopIteration).
If the generator function does not catch the passed-in exception, or
raises a different exception, then that exception propagates to the caller.

When `throw()` is called to start the generator, the generator
immediately exits (that is, subsequent calls to [__next__()](../generator.__next__/README.md)
will raise [StopIteration](https://docs.python.org/3.15/builtins/exceptions.html#StopIteration)) and the thrown exception is propagated to
`throw()`'s caller.

In typical use, this is called with a single argument, an exception instance,
similar to the way the `raise` keyword is used.

For backwards compatibility, however, the second signature is
supported, following a convention from older versions of Python.
The *type* argument should be an exception class, and *value*
should be an exception instance. If the *value* is not provided, the
*type* constructor is called to get an instance. If *traceback*
is provided, it is set on the exception, otherwise any existing
[__traceback__](https://docs.python.org/3.15/builtins/exceptions.html#BaseException.__traceback__) attribute stored in *value* may
be cleared.

> *Changed in version 3.12:* The second signature (type[, value[, traceback]]) is deprecated and
> may be removed in a future version of Python.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.6.6: generator.throw durum geçişini kanıtla**

#### Önce

[b:2.6](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Hazır bir generatorın yield noktasında durduğu biliniyor. Gövdedeki try/except ValueError bu hatayı yakalayıp 8 yield ediyor. throw(ValueError("x")) sonucunu, yakalanmayan TypeError ile karşılaştır. Sonuçları çağrı -> durulan nokta -> sonraki durum tablosuyla göster.

#### Geçiş ölçütleri

- [ ] Yakalanan hata generator içinde işlenir, 8 döner; yakalanmayan TypeError dışarı yayılır ve generator kapanır.
- [ ] Çağrı ve tüketim/ilerleme anı birbirinden ayrılmıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../generator.close/README.md)
<!-- learning-task:end -->
