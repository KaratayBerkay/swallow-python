## `iterator.__iter__`

```
iterator.__iter__()
```

Return the [iterator](https://docs.python.org/3.15/glossary.html#term-iterator) object itself.  This is required to allow both
containers and iterators to be used with the `for` and
`in` statements.  This method corresponds to the
[tp_iter](https://docs.python.org/3.15/c-api/typeobj.html#c.PyTypeObject.tp_iter) slot of the type structure for Python
objects in the Python/C API.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.6.2: iterator.__iter__ durum geçişini kanıtla**

#### Önce

[b:2.6](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Üç öğeli iteratorın ilk öğesini tükettin. iter(it) ile alınan nesne hangi nesnedir ve sıradaki öğesi hangisidir? Sonuçları çağrı -> durulan nokta -> sonraki durum tablosuyla göster.

#### Geçiş ölçütleri

- [ ] Iterator __iter__ kendisini döndürür; yeniden başlatmaz, ikinci öğeden devam eder.
- [ ] Çağrı ve tüketim/ilerleme anı birbirinden ayrılmıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../iterator.__next__/README.md)
<!-- learning-task:end -->
