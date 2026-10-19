## `iterator.__next__`

```
iterator.__next__()
```

Return the next item from the [iterator](https://docs.python.org/3.15/glossary.html#term-iterator).  If there are no further
items, raise the [StopIteration](https://docs.python.org/3.15/builtins/exceptions.html#StopIteration) exception.  This method corresponds to
the [tp_iternext](https://docs.python.org/3.15/c-api/typeobj.html#c.PyTypeObject.tp_iternext) slot of the type structure for
Python objects in the Python/C API.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.6.3: iterator.__next__ durum geçişini kanıtla**

#### Önce

[b:2.6](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

4 ve 6 veren iterator için dört ardışık __next__ çağrısını izle. Sonuçları çağrı -> durulan nokta -> sonraki durum tablosuyla göster.

#### Geçiş ölçütleri

- [ ] 4, 6, StopIteration, StopIteration; tükenme kalıcıdır.
- [ ] Çağrı ve tüketim/ilerleme anı birbirinden ayrılmıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../generator.__next__/README.md)
<!-- learning-task:end -->
