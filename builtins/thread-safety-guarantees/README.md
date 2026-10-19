# Thread Safety Guarantees

This page documents thread-safety guarantees for built-in types in Python's
free-threaded build. The guarantees described here apply when using Python with
the [GIL](https://docs.python.org/3.15/glossary.html#term-GIL) disabled (free-threaded mode). When the GIL is enabled, most
operations are implicitly serialized.

For general guidance on writing thread-safe code in free-threaded Python, see
[Python support for free threading](https://docs.python.org/3.15/howto/free-threading-python.html#freethreading-python-howto).


<!-- learning-task:start -->
## Bölüm görevi

**Görev b:5: Garanti kapsamını sınırla**

### Önce

[t:11.4](../../tutorial/11-brief-tour-of-the-standard-library-part-ii/11.4-multi-threading/README.md) ve bu sayfanın açıklama/örnekleri.

Bu görevde verilen durumların yazılı çözümü geçerlidir; ek çalışma ortamı veya harici araç kurulumu gerekmez.

### Tek görev

GIL açık Python, GIL kapalı free-threaded Python ve farklı Python implementasyonu için bu sayfadaki garantilerin kapsamını yaz. "Her built-in kullanımı artık tek adımda güvenlidir" iddiasının neden sayfadan çıkmadığını açıkla.

### Geçiş ölçütleri

- [ ] Garantiler free-threaded/GIL kapalı bağlamda okunur; başka çalışma koşullarına koşulsuz taşınmaz.
- [ ] Tek işlem garantisi bütün kullanıcı algoritmasının atomik olduğu anlamına gelmez.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](thread-safety-levels/README.md)
<!-- learning-task:end -->
## Contents

- [Thread safety levels](thread-safety-levels/README.md) — The C API documentation uses the following levels to describe the thread safety guarantees of each function.
- [Thread safety for list objects](thread-safety-for-list-objects/README.md) — Reading a single element from a list is atomic:
- [Thread safety for dict objects](thread-safety-for-dict-objects/README.md) — Creating a dictionary with the dict constructor is atomic when the argument to it is a dict or a tuple.
- [Thread safety for set objects](thread-safety-for-set-objects/README.md) — The len() function is lock-free and atomic.
- [Thread safety for bytearray objects](thread-safety-for-bytearray-objects/README.md) — The len() function is lock-free and atomic.
- [Thread safety for memoryview objects](thread-safety-for-memoryview-objects/README.md) — memoryview objects provide access to the internal data of an underlying object without copying.

<!-- learning-milestone:start -->
## Klasör milestone görevi

**Milestone: Paylaşılan veriye yönelik iddiayı denetle**

### Önce

Bu klasördeki bütün bölüm görevleri ve alt klasör milestone kontrolleri tamamlanmış olmalı. Sırayı [görev dizininden](../../TASKS.md) kontrol et.

### Tek görev

Bir list, dict ve bytearray görünümü paylaşan iki iş parçacığı için tasarım incelemesi yaz. Her biri için bir güvenli tek işlem, iki adımdan oluşan bir yarış ve varsayımı bozan argüman türünü göster. Memoryview readonly seçeneğiyle veri yarışının çözülmediğini kanıtla; gerekli dış eşgüdümün kapsamını akış üzerinde işaretle.

### Geçiş ölçütleri

- [ ] Atomik işlem ile algoritma garantisi ayrıdır; deterministik olay sırası karşı örnek üretir.
- [ ] Aynı tamponu paylaşma, özel iterable ve kullanıcı karşılaştırma kodu sınırları gözden kaçmaz; olasılıksal thread testi geçiş koşulu değildir.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../time-complexity-of-operations-on-built-in-types/README.md)
<!-- learning-milestone:end -->
