## `next()`

```
next(iterator, /)
next(iterator, default, /)
```

Retrieve the next item from the [iterator](https://docs.python.org/3.15/glossary.html#term-iterator) by calling its
[__next__()](https://docs.python.org/3.15/builtins/stdtypes.html#iterator.__next__) method.  If *default* is given, it is returned
if the iterator is [exhausted](https://docs.python.org/3.15/glossary.html#term-exhausted), otherwise [StopIteration](https://docs.python.org/3.15/builtins/exceptions.html#StopIteration) is raised.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.48: next sözleşmesini uygula**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

`it=iter([4])` için önce `next(it)`, sonra `next(it,"SON")`, sonra defaultsuz `next(it)` çağır. Her çağrıyı ayrı incele; aynı iteratorın tüketim durumunu takip et.

#### Geçiş ölçütleri

- [ ] Sonuçlar 4, "SON", StopIteration olur.
- [ ] Default tüketimi geri sarmaz; tükenmiş iterator yeniden başlamaz.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../object/README.md)
<!-- learning-task:end -->
