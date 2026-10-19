## `FileExistsError`

```
FileExistsError
```

Raised when trying to create a file or directory which already exists.
Corresponds to `errno` [EEXIST](https://docs.python.org/3.15/library/errno.html#errno.EEXIST).

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.4.46: FileExistsError teşhisini gerekçelendir**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Verilen olay: Yalnız yeni dosya oluşturma isteğinin mevcut bir ada uygulanması. Beklenen hata türünü veya normal sonucu çıkar. Sistem olayıysa yalnız yazılı teşhis yap; gerçek arıza üretme. Basit veri işlemi ise küçük yerel örnekle doğrula. Bu türün neden uygun olduğunu, yakın ama farklı bir durumdan nasıl ayrıldığını açıkla.

#### Geçiş ölçütleri

- [ ] FileExistsError; dosya yokluğu değildir.
- [ ] Sadece hata adı değil, tetikleyici koşul ve ilgili yakalama sınırı gerekçelendirilmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../FileNotFoundError/README.md)
<!-- learning-task:end -->
