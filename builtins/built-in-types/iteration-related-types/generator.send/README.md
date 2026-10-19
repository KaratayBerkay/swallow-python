## `generator.send`

```
generator.send(value)
```

"Sends" a value into the generator function: the *value* argument becomes
the result of the current yield expression.

Otherwise, this method behaves like [__next__()](../generator.__next__/README.md): it resumes
the underlying function and either returns the next yielded value or raises
[StopIteration](https://docs.python.org/3.15/builtins/exceptions.html#StopIteration).

When `send()` is called to start the generator, it must be called
with [None](https://docs.python.org/3.15/builtins/constants.html#None) as the argument, because there is no current yield
expression that could receive the value.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.6.5: generator.send durum geçişini kanıtla**

#### Önce

[b:2.6](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

aşağıdaki generatorı generatorını kur. Başlatılmamış örneğe send(7) dene; yeni örnekte next ardından send(7) uygula. Sonuçları çağrı -> durulan nokta -> sonraki durum tablosuyla göster.

```python
def g():
    x = yield 4
    yield x + 1
```

#### Geçiş ölçütleri

- [ ] Başlatılmamış örnekte non-None send TypeError; next 4, send(7) 8 verir; x=7 olur.
- [ ] Çağrı ve tüketim/ilerleme anı birbirinden ayrılmıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../generator.throw/README.md)
<!-- learning-task:end -->
