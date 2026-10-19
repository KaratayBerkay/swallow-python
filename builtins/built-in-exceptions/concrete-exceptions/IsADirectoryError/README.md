## `IsADirectoryError`

```
IsADirectoryError
```

Raised when a file operation (such as [os.remove()](https://docs.python.org/3.15/library/os.html#os.remove)) is requested
on a directory.
Corresponds to `errno` [EISDIR](https://docs.python.org/3.15/library/errno.html#errno.EISDIR).

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.4.49: IsADirectoryError teşhisini gerekçelendir**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Verilen olay: Normal dosya bekleyen bir işleme dizin verilmesi. Beklenen hata türünü veya normal sonucu çıkar. Sistem olayıysa yalnız yazılı teşhis yap; gerçek arıza üretme. Basit veri işlemi ise küçük yerel örnekle doğrula. Bu türün neden uygun olduğunu, yakın ama farklı bir durumdan nasıl ayrıldığını açıkla.

#### Geçiş ölçütleri

- [ ] IsADirectoryError; NotADirectoryError ters yöndeki uyuşmazlıktır.
- [ ] Sadece hata adı değil, tetikleyici koşul ve ilgili yakalama sınırı gerekçelendirilmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../NotADirectoryError/README.md)
<!-- learning-task:end -->
