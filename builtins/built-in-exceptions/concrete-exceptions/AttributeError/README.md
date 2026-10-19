## `AttributeError`

```
AttributeError
```

Raised when an attribute reference (see [Attribute references](https://docs.python.org/3.15/reference/expressions.html#attribute-references)) or
assignment fails.  (When an object does not support attribute references or
attribute assignments at all, [TypeError](../TypeError/README.md) is raised.)

The optional *name* and *obj* keyword-only arguments
set the corresponding attributes:

### name

The name of the attribute that was attempted to be accessed.

### obj

The object that was accessed for the named attribute.

> *Changed in version 3.10:* Added the `name` and `obj` attributes.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.4.2: AttributeError teşhisini gerekçelendir**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Verilen olay: Bir nesnede bulunmayan .puan niteliğini okuma. Beklenen hata türünü veya normal sonucu çıkar. Sistem olayıysa yalnız yazılı teşhis yap; gerçek arıza üretme. Basit veri işlemi ise küçük yerel örnekle doğrula. Bu türün neden uygun olduğunu, yakın ama farklı bir durumdan nasıl ayrıldığını açıkla.

#### Geçiş ölçütleri

- [ ] AttributeError; isim ve nesne nitelikleri verilmişse teşhiste kullanılabilir.
- [ ] Sadece hata adı değil, tetikleyici koşul ve ilgili yakalama sınırı gerekçelendirilmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../EOFError/README.md)
<!-- learning-task:end -->
