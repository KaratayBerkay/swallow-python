## `SystemExit`

```
SystemExit
```

This exception is raised by the [sys.exit()](https://docs.python.org/3.15/library/sys.html#sys.exit) function.  It inherits from
[BaseException](../../base-classes/BaseException/README.md) instead of [Exception](../../base-classes/Exception/README.md) so that it is not accidentally
caught by code that catches [Exception](../../base-classes/Exception/README.md).  This allows the exception to
properly propagate up and cause the interpreter to exit.  When it is not
handled, the Python interpreter exits; no stack traceback is printed.  The
constructor accepts the same optional argument passed to [sys.exit()](https://docs.python.org/3.15/library/sys.html#sys.exit).
If the value is an integer, it specifies the system exit status (passed to
C's `exit` function); if it is `None`, the exit status is zero; if
it has another type (such as a string), the object's value is printed and
the exit status is one.

A call to [sys.exit()](https://docs.python.org/3.15/library/sys.html#sys.exit) is translated into an exception so that clean-up
handlers (`finally` clauses of `try` statements) can be
executed, and so that a debugger can execute a script without running the risk
of losing control.  The [os._exit()](https://docs.python.org/3.15/library/os.html#os._exit) function can be used if it is
absolutely positively necessary to exit immediately (for example, in the child
process after a call to [os.fork()](https://docs.python.org/3.15/library/os.html#os.fork)).

### code

The exit status or error message that is passed to the constructor.
(Defaults to `None`.)

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.4.27: SystemExit teşhisini gerekçelendir**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Verilen olay: SystemExit(3), SystemExit(None) ve SystemExit("hata") nesneleri. Beklenen hata türünü veya normal sonucu çıkar. Sistem olayıysa yalnız yazılı teşhis yap; gerçek arıza üretme. Basit veri işlemi ise küçük yerel örnekle doğrula. Bu türün neden uygun olduğunu, yakın ama farklı bir durumdan nasıl ayrıldığını açıkla.

#### Geçiş ölçütleri

- [ ] Code alanları sırasıyla 3, None, "hata"; yakalanmazsa çıkış durumları 3, 0, 1; Exception handlerı yakalamaz.
- [ ] Sadece hata adı değil, tetikleyici koşul ve ilgili yakalama sınırı gerekçelendirilmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../TypeError/README.md)
<!-- learning-task:end -->
