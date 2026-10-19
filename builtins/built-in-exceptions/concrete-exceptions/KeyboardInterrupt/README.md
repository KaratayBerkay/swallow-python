## `KeyboardInterrupt`

```
KeyboardInterrupt
```

Raised when the user hits the interrupt key (normally `Control-C` or
`Delete`).  During execution, a check for interrupts is made
regularly. The exception inherits from [BaseException](../../base-classes/BaseException/README.md) so as to not be
accidentally caught by code that catches [Exception](../../base-classes/Exception/README.md) and thus prevent
the interpreter from exiting.

> **Note**
>
> Catching a KeyboardInterrupt requires special consideration.
> Because it can be raised at unpredictable points, it may, in some
> circumstances, leave the running program in an inconsistent state. It is
> generally best to allow KeyboardInterrupt to end the program as
> quickly as possible or avoid raising it entirely. (See
> [Note on Signal Handlers and Exceptions](https://docs.python.org/3.15/library/signal.html#handlers-and-exceptions).)

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.4.11: KeyboardInterrupt teşhisini gerekçelendir**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Verilen olay: Kullanıcı kesme tuşuna basıyor; kod yalnız except Exception kullanıyor. Beklenen hata türünü veya normal sonucu çıkar. Sistem olayıysa yalnız yazılı teşhis yap; gerçek arıza üretme. Basit veri işlemi ise küçük yerel örnekle doğrula. Bu türün neden uygun olduğunu, yakın ama farklı bir durumdan nasıl ayrıldığını açıkla.

#### Geçiş ölçütleri

- [ ] KeyboardInterrupt bu handlerı aşar; BaseException kolundadır; keyfi kesintiler tutarsız durum bırakabilir.
- [ ] Sadece hata adı değil, tetikleyici koşul ve ilgili yakalama sınırı gerekçelendirilmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../MemoryError/README.md)
<!-- learning-task:end -->
