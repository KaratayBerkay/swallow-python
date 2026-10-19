## `FileNotFoundError`

```
FileNotFoundError
```

Raised when a file or directory is requested but doesn't exist.
Corresponds to `errno` [ENOENT](https://docs.python.org/3.15/library/errno.html#errno.ENOENT).

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.4.47: FileNotFoundError teşhisini gerekçelendir**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Verilen olay: İstenen dosya veya yol bileşeninin bulunmaması. Beklenen hata türünü veya normal sonucu çıkar. Sistem olayıysa yalnız yazılı teşhis yap; gerçek arıza üretme. Basit veri işlemi ise küçük yerel örnekle doğrula. Bu türün neden uygun olduğunu, yakın ama farklı bir durumdan nasıl ayrıldığını açıkla.

#### Geçiş ölçütleri

- [ ] FileNotFoundError; izin reddinden ayrı sebeptir.
- [ ] Sadece hata adı değil, tetikleyici koşul ve ilgili yakalama sınırı gerekçelendirilmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../InterruptedError/README.md)
<!-- learning-task:end -->
