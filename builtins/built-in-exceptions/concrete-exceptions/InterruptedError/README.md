## `InterruptedError`

```
InterruptedError
```

Raised when a system call is interrupted by an incoming signal.
Corresponds to `errno` [EINTR](https://docs.python.org/3.15/library/errno.html#errno.EINTR).

> *Changed in version 3.5:* Python now retries system calls when a syscall is interrupted by a
> signal, except if the signal handler raises an exception (see [PEP 475](https://peps.python.org/pep-475/)
> for the rationale), instead of raising InterruptedError.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.4.48: InterruptedError teşhisini gerekçelendir**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Verilen olay: Sistem çağrısının sinyalle kesilmesi; handlerın hata yükseltmediği modern Python. Beklenen hata türünü veya normal sonucu çıkar. Sistem olayıysa yalnız yazılı teşhis yap; gerçek arıza üretme. Basit veri işlemi ise küçük yerel örnekle doğrula. Bu türün neden uygun olduğunu, yakın ama farklı bir durumdan nasıl ayrıldığını açıkla.

#### Geçiş ölçütleri

- [ ] Genellikle sistem çağrısı yeniden denenir; her kesinti mutlaka InterruptedError olarak dışarı çıkmaz.
- [ ] Sadece hata adı değil, tetikleyici koşul ve ilgili yakalama sınırı gerekçelendirilmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../IsADirectoryError/README.md)
<!-- learning-task:end -->
