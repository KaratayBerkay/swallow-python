## 5.8. Special considerations for \_\_main\_\_

The `__main__` module is a special case relative to Python's import system. As noted elsewhere, the `__main__` module is directly initialized at interpreter startup, much like `sys` and `builtins`. However, unlike those two, it doesn't strictly qualify as a built-in module. This is because the manner in which `__main__` is initialized depends on the flags and other options with which the interpreter is invoked.


<!-- learning-task:start -->
### Bölüm görevi

**Görev 5.8: Ana modülü built-in modülle karıştırma**

**Odak:** `__main__` başlangıçta oluşur; başlatma biçimiyle kimliği ilişkilidir.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.7](../5.7-package-relative-imports/README.md).
- Ön bilgi: [t:6.1.1](../../../tutorial/06-modules/6.1-more-on-modules/6.1.1-executing-modules-as-scripts/README.md).

#### Tek görev

1. Normal import edilen helper modülü ile python helper.py olarak başlatılan dosya için ad çizimi yap.

2. Her durumda `__main__` hangisi, helper hangi adla bağlanıyor ve `__name__` kontrolü hangi blokları yürütür? sys ile aynı biçimde başlangıçta hazır olmasının `__main__` modülünü neden built-in sınıfına sokmadığını açıkla.

#### Geçiş ölçütleri

- [ ] Doğrudan dosya girişinde `__name__` `__main__`; normal importta helper.
- [ ] Ana modülün başlatma seçenekleriyle değişmesi belirtilmiş.
- [ ] Başlangıçta hazırlanma ile built-in modül olma ayrı tutulmuş.
- [ ] Henüz alt bölümdeki `__spec__` varyantlarını ezberden üretmek gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](5.8.1-main-spec/README.md)
<!-- learning-task:end -->
### Sections

- [5.8.1. \_\_main\_\_.\_\_spec\_\_](5.8.1-main-spec/README.md)

<!-- learning-milestone:start -->
### Klasör milestone görevi

**Milestone: Ana modül geçişi**

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Başlatma biçimi ve ana spec.

#### Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

#### Tek kontrol

Bu klasörün kapsamı altındaki tek kontrolle aynıdır. [Mevcut görevin](5.8.1-main-spec/TASK.md) geçiş ölçütleri bu milestone için de geçerlidir. Aynı işi ikinci kez yapman gerekmez.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-milestone:end -->
