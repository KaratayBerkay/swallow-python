## `NameError`

```
NameError
```

Raised when a local or global name is not found.  This applies only to
unqualified names.  The associated value is an error message that includes the
name that could not be found.

The optional *name* keyword-only argument sets the attribute:

### name

The name of the variable that was attempted to be accessed.

> *Changed in version 3.10:* Added the `name` attribute.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.4.13: NameError teşhisini gerekçelendir**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Verilen olay: Tanımlanmamış yalın puan adını okuma. Beklenen hata türünü veya normal sonucu çıkar. Sistem olayıysa yalnız yazılı teşhis yap; gerçek arıza üretme. Basit veri işlemi ise küçük yerel örnekle doğrula. Bu türün neden uygun olduğunu, yakın ama farklı bir durumdan nasıl ayrıldığını açıkla.

#### Geçiş ölçütleri

- [ ] NameError; o.puan nitelik erişimiyle aynı hata kategorisi değildir.
- [ ] Sadece hata adı değil, tetikleyici koşul ve ilgili yakalama sınırı gerekçelendirilmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../NotImplementedError/README.md)
<!-- learning-task:end -->
