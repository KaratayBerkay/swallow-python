## `ImportError`

```
ImportError
```

Raised when the `import` statement has troubles trying to
load a module.  Also raised when the "from list" in `from ... import`
has a name that cannot be found.

The optional *name* and *path* keyword-only arguments
set the corresponding attributes:

### name

The name of the module that was attempted to be imported.

### path

The path to any file which triggered the exception.

> *Changed in version 3.3:* Added the `name` and `path` attributes.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.4.6: ImportError teşhisini gerekçelendir**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Verilen olay: Modül bulunuyor ama from import ile istenen ad bulunamıyor. Beklenen hata türünü veya normal sonucu çıkar. Sistem olayıysa yalnız yazılı teşhis yap; gerçek arıza üretme. Basit veri işlemi ise küçük yerel örnekle doğrula. Bu türün neden uygun olduğunu, yakın ama farklı bir durumdan nasıl ayrıldığını açıkla.

#### Geçiş ölçütleri

- [ ] ImportError; name ve path ek bilgileri koşula göre tanımlanabilir.
- [ ] Sadece hata adı değil, tetikleyici koşul ve ilgili yakalama sınırı gerekçelendirilmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../ModuleNotFoundError/README.md)
<!-- learning-task:end -->
