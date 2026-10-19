## `NotADirectoryError`

```
NotADirectoryError
```

Raised when a directory operation (such as [os.listdir()](https://docs.python.org/3.15/library/os.html#os.listdir)) is requested on
something which is not a directory.  On most POSIX platforms, it may also be
raised if an operation attempts to open or traverse a non-directory file as if
it were a directory.
Corresponds to `errno` [ENOTDIR](https://docs.python.org/3.15/library/errno.html#errno.ENOTDIR).

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.4.50: NotADirectoryError teşhisini gerekçelendir**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Verilen olay: Dizin olarak geçilmek istenen yol bileşeninin normal dosya olması. Beklenen hata türünü veya normal sonucu çıkar. Sistem olayıysa yalnız yazılı teşhis yap; gerçek arıza üretme. Basit veri işlemi ise küçük yerel örnekle doğrula. Bu türün neden uygun olduğunu, yakın ama farklı bir durumdan nasıl ayrıldığını açıkla.

#### Geçiş ölçütleri

- [ ] NotADirectoryError; mevcut olmayan dosya veya izinsiz erişim ayrı teşhislerdir.
- [ ] Sadece hata adı değil, tetikleyici koşul ve ilgili yakalama sınırı gerekçelendirilmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../PermissionError/README.md)
<!-- learning-task:end -->
