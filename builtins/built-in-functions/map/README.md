## `map()`

```
map(function, iterable, /, *iterables, strict=False)
```

Return an iterator that applies *function* to every item of *iterable*,
yielding the results.  If additional *iterables* arguments are passed,
*function* must take that many arguments and is applied to the items from all
iterables in parallel.  With multiple iterables, the iterator stops when the
shortest iterable is [exhausted](https://docs.python.org/3.15/glossary.html#term-exhausted).  If *strict* is `True` and one of the
iterables is exhausted before the others, a [ValueError](https://docs.python.org/3.15/builtins/exceptions.html#ValueError) is raised. For
cases where the function inputs are already arranged into argument tuples,
see [itertools.starmap()](https://docs.python.org/3.15/library/itertools.html#itertools.starmap).

> *Changed in version 3.14:* Added the *strict* parameter.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.44: map sözleşmesini uygula**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

Sürüm: Python 3.14 veya üzeri. Daha eski yorumlayıcıda yalnız bu sürüme bağlı kısmı gerekçeli yazılı iz ile çözebilirsin; çalıştırma kanıtını bekleyen olarak kaydet.

#### Tek görev

Bir çağrı listesi tutan `iki(x)` fonksiyonu yaz. `m=map(iki,[2,3])` oluşturulurken ve next çağrılarında kayıtları karşılaştır. İki iterable alan map için kısa girdide durmayı göster. Python 3.14+ strict=True kullanıldığında uzunluk farkının hangi anda hata verdiğini ekle.

#### Geçiş ölçütleri

- [ ] Map oluşturulurken iki çağrılmaz; tüketimde sırasıyla çalışır.
- [ ] Normal biçim kısa girdide durur; strict=True tüketim sırasında ValueError verir.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../max/README.md)
<!-- learning-task:end -->
