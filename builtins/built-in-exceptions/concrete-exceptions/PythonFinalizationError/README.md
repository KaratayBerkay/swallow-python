## `PythonFinalizationError`

```
PythonFinalizationError
```

This exception is derived from [RuntimeError](../RuntimeError/README.md).  It is raised when
an operation is blocked during interpreter shutdown also known as
[Python finalization](https://docs.python.org/3.15/glossary.html#term-interpreter-shutdown).

Examples of operations which can be blocked with a
PythonFinalizationError during the Python finalization:

- Creating a new Python thread.

- [Joining](https://docs.python.org/3.15/library/threading.html#threading.Thread.join) a running daemon thread.

- [os.fork()](https://docs.python.org/3.15/library/os.html#os.fork),

- acquiring a lock such as [threading.Lock](https://docs.python.org/3.15/library/threading.html#threading.Lock), when it is known that
  the operation would otherwise deadlock.

See also the [sys.is_finalizing()](https://docs.python.org/3.15/library/sys.html#sys.is_finalizing) function.

> *Added in version 3.13:* Previously, a plain [RuntimeError](../RuntimeError/README.md) was raised.

> *Changed in version 3.14:* [threading.Thread.join()](https://docs.python.org/3.15/library/threading.html#threading.Thread.join) can now raise this exception.

> *Changed in version 3.15:* This exception may be raised when acquiring `threading.Lock()`
> or `threading.RLock()`.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.4.17: PythonFinalizationError teşhisini gerekçelendir**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

Sürüm: Python 3.13 veya üzeri. Daha eski yorumlayıcıda yalnız bu sürüme bağlı kısmı gerekçeli yazılı iz ile çözebilirsin; çalıştırma kanıtını bekleyen olarak kaydet.

#### Tek görev

Verilen olay: Interpreter kapanışı sırasında yasaklanan yeni thread oluşturma girişimi. Beklenen hata türünü veya normal sonucu çıkar. Sistem olayıysa yalnız yazılı teşhis yap; gerçek arıza üretme. Basit veri işlemi ise küçük yerel örnekle doğrula. Bu türün neden uygun olduğunu, yakın ama farklı bir durumdan nasıl ayrıldığını açıkla.

#### Geçiş ölçütleri

- [ ] Python 3.13+ PythonFinalizationError; RuntimeError alt türüdür, sıradan uygulama akışındaki her thread hatası değildir.
- [ ] Sadece hata adı değil, tetikleyici koşul ve ilgili yakalama sınırı gerekçelendirilmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../RecursionError/README.md)
<!-- learning-task:end -->
