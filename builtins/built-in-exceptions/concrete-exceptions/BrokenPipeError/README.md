## `BrokenPipeError`

```
BrokenPipeError
```

A subclass of [ConnectionError](../ConnectionError/README.md), raised when trying to write on a
pipe while the other end has been closed, or trying to write on a socket
which has been shutdown for writing.
Corresponds to `errno` [EPIPE](https://docs.python.org/3.15/library/errno.html#errno.EPIPE) and [ESHUTDOWN](https://docs.python.org/3.15/library/errno.html#errno.ESHUTDOWN).

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.4.42: BrokenPipeError teşhisini gerekçelendir**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Verilen olay: Diğer ucu kapatılmış pipea yazma. Beklenen hata türünü veya normal sonucu çıkar. Sistem olayıysa yalnız yazılı teşhis yap; gerçek arıza üretme. Basit veri işlemi ise küçük yerel örnekle doğrula. Bu türün neden uygun olduğunu, yakın ama farklı bir durumdan nasıl ayrıldığını açıkla.

#### Geçiş ölçütleri

- [ ] BrokenPipeError; ConnectionError ve OSError ile de yakalanabilir.
- [ ] Sadece hata adı değil, tetikleyici koşul ve ilgili yakalama sınırı gerekçelendirilmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../ConnectionAbortedError/README.md)
<!-- learning-task:end -->
