## `container.__iter__`

```
container.__iter__()
```

Return an [iterator](https://docs.python.org/3.15/glossary.html#term-iterator) object.  The object is required to support the
iterator protocol described below.  If a container supports different types
of iteration, additional methods can be provided to specifically request
iterators for those iteration types.  (An example of an object supporting
multiple forms of iteration would be a tree structure which supports both
breadth-first and depth-first traversal.)  This method corresponds to the
[tp_iter](https://docs.python.org/3.15/c-api/typeobj.html#c.PyTypeObject.tp_iter) slot of the type structure for Python
objects in the Python/C API.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.6.1: container.__iter__ durum geçişini kanıtla**

#### Önce

[b:2.6](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Bir container iki bağımsız iterator veriyor. Birinciden iki öğe al; ikinci ilk hangi öğeyi verir? Sonuçları çağrı -> durulan nokta -> sonraki durum tablosuyla göster.

#### Geçiş ölçütleri

- [ ] Container __iter__ yeni iterator sağlayabilir; ikinci ilk öğeden başlar.
- [ ] Çağrı ve tüketim/ilerleme anı birbirinden ayrılmıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../iterator.__iter__/README.md)
<!-- learning-task:end -->
