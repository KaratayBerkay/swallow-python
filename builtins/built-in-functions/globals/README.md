## `globals()`

```
globals()
```

Return the dictionary implementing the current module namespace. For code within
functions, this is set when the function is defined and remains the same
regardless of where the function is called.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.30: globals sözleşmesini uygula**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Modül düzeyinde `puan=3` tanımla. `def oku(): return globals()["puan"]` yaz. Globals sözlüğündeki puan değerini 8 yapıp fonksiyonu yeniden çağır; sözlüğün bir kopya mı canlı namespace mi olduğunu kanıtla.

#### Geçiş ölçütleri

- [ ] Sonuç önce 3 sonra 8 olur; globals modülün canlı sözlüğüdür.
- [ ] Fonksiyonun tanımlandığı modülün global alanı kullanılır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../hasattr/README.md)
<!-- learning-task:end -->
