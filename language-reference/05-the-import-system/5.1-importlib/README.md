## 5.1. `importlib`

The `importlib` module provides a rich API for interacting with the import system. For example `importlib.import_module()` provides a recommended, simpler API than built-in `__import__()` for invoking the import machinery. Refer to the `importlib` library documentation for additional detail.

<!-- learning-task:start -->
### Bölüm görevi

**Görev 5.1: Dinamik adla basit modül al**

**Odak:** importlib.import_module ile adı metinden gelen modüle erişim.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5](../README.md).

#### Tek görev

1. module_name = "math" için importlib.import_module(module_name) sonucunu m adına bağla, m.cos(0) çağır.

2. Aynı işlemin import math biçiminde modül adını kaynak kodda sabitlemesiyle farkını açıkla.

3. Bu kısa bölümde anlatılmayan özel loader tasarlaman gerekmiyor.

#### Geçiş ölçütleri

- [ ] Sonuç 1.0; m modül nesnesi olarak kullanılmış.
- [ ] Metin içindeki modül adı ile yerel değişken adı ayrılmış.
- [ ] Dinamik import için bölümün önerdiği basit API seçilmiş; exec ile kod metni üretilmemiş.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../5.2-packages/README.md)
<!-- learning-task:end -->
