# Built-in Constants

A small number of constants live in the built-in namespace.  They are:

> **Note**
>
> The names [None](None/README.md), [False](False/README.md), [True](True/README.md) and [__debug__](__debug__/README.md)
> cannot be reassigned (assignments to them, even as an attribute name, raise
> [SyntaxError](https://docs.python.org/3.15/builtins/exceptions.html#SyntaxError)), so they can be considered "true" constants.


<!-- learning-task:start -->
## Bölüm görevi

**Görev b:1: Yeniden atanamayan adları ayır**

### Önce

[t:4.8](../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

### Tek görev

None, False, True, __debug__ adlarına atama içeren dört ayrı kısa kaynak parçasını incele. Her birinin neden çalışma zamanına ulaşmadığını açıkla; `durum=False` ile farkını belirt.

### Geçiş ölçütleri

- [ ] Dört özel ada atama SyntaxError verir; değişken adına atama geçerlidir.
- [ ] Sözdizimi hatasıyla normal bir bool değeri saklama ayrılmıştır.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](False/README.md)
<!-- learning-task:end -->
## Contents

- [`False`](False/README.md) — The false value of the bool type.
- [`True`](True/README.md) — The true value of the bool type.
- [`None`](None/README.md) — An object frequently used to represent the absence of a value, as when default arguments are not passed to a function.
- [`NotImplemented`](NotImplemented/README.md) — A special value which should be returned by the binary special methods (e.g. __eq__(), __lt__(), __add__(), __rsub__(), etc.) to indicate that the…
- [`Ellipsis`](Ellipsis/README.md) — The same as the ellipsis literal "...", an object frequently used to indicate that something is omitted.
- [`__debug__`](__debug__/README.md) — This constant is true if Python was not started with an -O option.

## Constants added by the `site` module

The [site](https://docs.python.org/3.15/library/site.html#module-site) module (which is imported automatically during startup, except
if the [-S](https://docs.python.org/3.15/using/cmdline.html#cmdoption-S) command-line option is given) adds several constants to the
built-in namespace.  They are useful for the interactive interpreter shell and
should not be used in programs.

- [`quit()`](constants-added-by-the-site-module/quit/README.md) — Objects that when printed, print a message like "Use quit() or Ctrl-D (i.e. EOF) to exit", and when accessed directly in the interactive…
- [`help`](constants-added-by-the-site-module/help/README.md) — Object that when printed, prints the message "Type help() for interactive help, or help(object) for help about object.", and when accessed…
- [`copyright`](constants-added-by-the-site-module/copyright/README.md) — Objects that when printed or called, print the text of copyright or credits, respectively.
- [`license`](constants-added-by-the-site-module/license/README.md) — Object that when printed, prints the message "Type license() to see the full license text", and when called, displays the full license text in a…
- [`exit()`](constants-added-by-the-site-module/exit/README.md) — Documented together with quit().
- [`credits`](constants-added-by-the-site-module/credits/README.md) — Documented together with copyright.

<!-- learning-milestone:start -->
## Klasör milestone görevi

**Milestone: Varsayılan ile açık değeri ayır**

### Önce

Bu klasördeki bütün bölüm görevleri ve alt klasör milestone kontrolleri tamamlanmış olmalı. Sırayı [görev dizininden](../../TASKS.md) kontrol et.

### Tek görev

Bir fonksiyonun verilmemiş argümanı için kendi tekil object nesneni kullan; açık None, False ve 0 girdilerini ayrı sonuçlara yönlendir. None/False/True adlarını değiştirmeden durum sakla. NotImplemented ve Ellipsisin bu uygulamada neden rastgele varsayılan yerine konmaması gerektiğini açıkla.

### Geçiş ölçütleri

- [ ] Verilmemiş ve açık değerler kimlik karşılaştırmasıyla ayrılır.
- [ ] NotImplemented operatör protokolüne, Ellipsis kendi anlamına göre değerlendirilir; özel sabit adları yeniden atanmamıştır.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../built-in-types/README.md)
<!-- learning-milestone:end -->
