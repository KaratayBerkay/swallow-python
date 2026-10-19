## `aiter()`

```
aiter(async_iterable, /)
```

Return an [asynchronous iterator](https://docs.python.org/3.15/glossary.html#term-asynchronous-iterator) for an [asynchronous iterable](https://docs.python.org/3.15/glossary.html#term-asynchronous-iterable).
Equivalent to calling `x.__aiter__()`.

Note: Unlike [iter()](../iter/README.md), aiter() has no 2-argument variant.

> *Added in version 3.10.*

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.2: aiter sözleşmesini uygula**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

Bu görevde verilen durumların yazılı çözümü geçerlidir; ek çalışma ortamı veya harici araç kurulumu gerekmez.

#### Tek görev

Verilen async iterable için `__aiter__()` çağrısının `it` nesnesini döndürdüğü biliniyor. `aiter(kaynak)` çağrısını ve `aiter(kaynak, "SON")` denemesini yazılı olarak izle. Sonucu, çağrılan metodu ve normal `iter` ile imza farkını göster.

#### Geçiş ölçütleri

- [ ] İlk çağrı async iterator `it` nesnesini döndürür; öğe tüketmez.
- [ ] İkinci çağrı TypeError olur; iki argümanlı sentinel biçimi yoktur.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../all/README.md)
<!-- learning-task:end -->
