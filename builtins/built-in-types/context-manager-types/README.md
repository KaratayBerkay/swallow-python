Python's `with` statement supports the concept of a runtime context
defined by a context manager.  This is implemented using a pair of methods
that allow user-defined classes to define a runtime context that is entered
before the statement body is executed and exited when the statement ends:

- [`contextmanager.__enter__`](contextmanager.__enter__/README.md) — Enter the runtime context and return either this object or another object related to the runtime context.
- [`contextmanager.__exit__`](contextmanager.__exit__/README.md) — Exit the runtime context and return a Boolean flag indicating if any exception that occurred should be suppressed.

Python defines several context managers to support easy thread synchronisation,
prompt closure of files or other objects, and simpler manipulation of the active
decimal arithmetic context. The specific types are not treated specially beyond
their implementation of the context management protocol. See the
[contextlib](https://docs.python.org/3.15/library/contextlib.html#module-contextlib) module for some examples.

Python's [generator](https://docs.python.org/3.15/glossary.html#term-generator)s and the `contextlib.contextmanager` decorator
provide a convenient way to implement these protocols.  If a generator function is
decorated with the `contextlib.contextmanager` decorator, it will return a
context manager implementing the necessary [__enter__()](contextmanager.__enter__/README.md) and
[__exit__()](contextmanager.__exit__/README.md) methods, rather than the iterator produced by an
undecorated generator function.

Note that there is no specific slot for any of these methods in the type
structure for Python objects in the Python/C API. Extension types wanting to
define these methods must provide them as a normal Python accessible method.
Compared to the overhead of setting up the runtime context, the overhead of a
single class dictionary lookup is negligible.

<!-- learning-task:start -->
## Bölüm görevi

**Görev b:2.13: With giriş ve çıkışını izle**

### Önce

[b:2](../README.md) ve bu sayfanın açıklama/örnekleri.

### Tek görev

Bir with akışında yöneticinin giriş metodu "hazir" döndürüyor, gövde normal bitiyor, çıkış metodu çağrılıyor. Yönetici nesne -> giriş dönüşü -> as değişkeni -> gövde -> çıkış sırasını yazılı çiz. Dosya yöneticisi gibi farklı bir türün de aynı protokolle çalışabilmesini açıkla.

### Geçiş ölçütleri

- [ ] Giriş, gövde, çıkış sırası ve as değişkeninin giriş dönüşünü alması doğru gösterilmiştir.
- [ ] With belirli bir sınıf adına değil protokol metotlarına dayanır; hata argümanlarının ayrıntısı sonraki yaprak görevde incelenir.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](contextmanager.__enter__/README.md)
<!-- learning-task:end -->

<!-- learning-milestone:start -->
## Klasör milestone görevi

**Milestone: Kaynak yaşam döngüsünü yönet**

### Önce

Bu klasördeki bütün bölüm görevleri ve alt klasör milestone kontrolleri tamamlanmış olmalı. Sırayı [görev dizininden](../../../TASKS.md) kontrol et.

### Tek görev

Kaynak açıldı/kullanıldı/kapandı olaylarını kaydeden context manager yaz. Normal gövde, bastırılan ValueError ve bastırılmayan TypeError yollarını göster; as değişkeni selften farklı olsun.

### Geçiş ölçütleri

- [ ] Exit bütün başarılı girişlerden sonra çalışır; giriş hatasında çalışmaz.
- [ ] Exit yalnız seçilen ValueErrorı bastırır; temizleme hatanın yanlışlıkla yutulmasına yol açmaz.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../type-annotation-types-generic-alias-union/README.md)
<!-- learning-milestone:end -->
