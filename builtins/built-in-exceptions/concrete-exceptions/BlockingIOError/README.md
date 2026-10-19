## `BlockingIOError`

```
BlockingIOError
```

Raised when an operation would block on an object (e.g. socket) set
for non-blocking operation.
Corresponds to `errno` [EAGAIN](https://docs.python.org/3.15/library/errno.html#errno.EAGAIN), [EALREADY](https://docs.python.org/3.15/library/errno.html#errno.EALREADY),
[EWOULDBLOCK](https://docs.python.org/3.15/library/errno.html#errno.EWOULDBLOCK) and [EINPROGRESS](https://docs.python.org/3.15/library/errno.html#errno.EINPROGRESS).

In addition to those of [OSError](../OSError/README.md), BlockingIOError can have
one more attribute:

### characters_written

An integer containing the number of **bytes** written to the stream
before it blocked. This attribute is available when using the
buffered I/O classes from the [io](https://docs.python.org/3.15/library/io.html#module-io) module.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.4.39: BlockingIOError teşhisini gerekçelendir**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Verilen olay: Non-blocking akışın şu an ilerleyemediği, daha önce 3 bayt yazdığı bildirilmiş durum. Beklenen hata türünü veya normal sonucu çıkar. Sistem olayıysa yalnız yazılı teşhis yap; gerçek arıza üretme. Basit veri işlemi ise küçük yerel örnekle doğrula. Bu türün neden uygun olduğunu, yakın ama farklı bir durumdan nasıl ayrıldığını açıkla.

#### Geçiş ölçütleri

- [ ] BlockingIOError; buffered I/O tarafından verilen characters_written değeri 3 bayttır, karakter sayısı değildir.
- [ ] Sadece hata adı değil, tetikleyici koşul ve ilgili yakalama sınırı gerekçelendirilmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../ChildProcessError/README.md)
<!-- learning-task:end -->
