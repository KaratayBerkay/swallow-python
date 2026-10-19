## `__debug__`

```
__debug__
```

This constant is true if Python was not started with an [-O](https://docs.python.org/3.15/using/cmdline.html#cmdoption-O) option.
See also the `assert` statement.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:1.6: Başlatma kipini sonuca bağla**

#### Önce

[b:1](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Normal Python ve -O ile başlatılan Python için __debug__ değerini, `assert False` satırının etkisini yazılı olarak karşılaştır. __debug__ değerini programın içinde atamayla değiştirmenin neden çözüm olmadığını açıkla.

#### Geçiş ölçütleri

- [ ] Normalde True ve AssertionError, -O ile False ve assert kontrolünün kaldırılması.
- [ ] __debug__ özel adına atama SyntaxError verir; başlatma kipiyle ilişki kurulmuştur.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../constants-added-by-the-site-module/README.md)
<!-- learning-task:end -->
