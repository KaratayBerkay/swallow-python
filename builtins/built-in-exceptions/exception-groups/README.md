The following are used when it is necessary to raise multiple unrelated
exceptions. They are part of the exception hierarchy so they can be
handled with `except` like all other exceptions. In addition,
they are recognised by `except*`, which matches
their subgroups based on the types of the contained exceptions.

- [`ExceptionGroup`](ExceptionGroup/README.md) — Both of these exception types wrap the exceptions in the sequence excs.
- [`BaseExceptionGroup`](BaseExceptionGroup/README.md) — Documented together with ExceptionGroup.

<!-- learning-milestone:start -->
## Klasör milestone görevi

**Milestone: Hata grubu kanıtını devral**

### Önce

Bu klasördeki bütün bölüm görevleri ve alt klasör milestone kontrolleri tamamlanmış olmalı. Sırayı [görev dizininden](../../../TASKS.md) kontrol et.

### Tek görev

[b:4.6.1 görevindeki](ExceptionGroup/README.md) mevcut çözümünü kullan. Aynı ağaç bölme ve metadata kanıtını ikinci kez yazma.

### Geçiş ölçütleri

- [ ] İç içe yapı, seçim, kalan grup ve korunan metadata mevcut kanıtta doğrulanmıştır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../exception-hierarchy/README.md)
<!-- learning-milestone:end -->
