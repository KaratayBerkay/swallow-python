## `PermissionError`

```
PermissionError
```

Raised when trying to run an operation without the adequate access
rights - for example filesystem permissions.
Corresponds to `errno` [EACCES](https://docs.python.org/3.15/library/errno.html#errno.EACCES),
[EPERM](https://docs.python.org/3.15/library/errno.html#errno.EPERM), and [ENOTCAPABLE](https://docs.python.org/3.15/library/errno.html#errno.ENOTCAPABLE).

> *Changed in version 3.11.1:* WASI's [ENOTCAPABLE](https://docs.python.org/3.15/library/errno.html#errno.ENOTCAPABLE) is now mapped to
> PermissionError.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.4.51: PermissionError teşhisini gerekçelendir**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Verilen olay: Var olan dosyaya gereken erişim hakkı olmadan işlem yapma. Beklenen hata türünü veya normal sonucu çıkar. Sistem olayıysa yalnız yazılı teşhis yap; gerçek arıza üretme. Basit veri işlemi ise küçük yerel örnekle doğrula. Bu türün neden uygun olduğunu, yakın ama farklı bir durumdan nasıl ayrıldığını açıkla.

#### Geçiş ölçütleri

- [ ] PermissionError; bulunmayan dosyayla aynı gerekçe değildir.
- [ ] Sadece hata adı değil, tetikleyici koşul ve ilgili yakalama sınırı gerekçelendirilmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../ProcessLookupError/README.md)
<!-- learning-task:end -->
