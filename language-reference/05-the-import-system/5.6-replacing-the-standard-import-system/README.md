## 5.6. Replacing the standard import system

The most reliable mechanism for replacing the entire import system is to delete the default contents of `sys.meta_path`, replacing them entirely with a custom meta path hook.

If it is acceptable to only alter the behaviour of import statements without affecting other APIs that access the import system, then replacing the builtin `__import__()` function may be sufficient.

To selectively prevent the import of some modules from a hook early on the meta path (rather than disabling the standard import system entirely), it is sufficient to raise `ModuleNotFoundError` directly from `find_spec()` instead of returning `None`. The latter indicates that the meta path search should continue, while raising an exception terminates it immediately.

<!-- learning-task:start -->
### Bölüm görevi

**Görev 5.6: Aramayı sürdürmekle reddetmeyi ayır**

**Odak:** Meta path değişimi, `__import__` değiştirme sınırı ve None/hata ayrımı.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.5.2](../5.5-the-path-based-finder/5.5.2-path-entry-finder-protocol/README.md).

#### Tek görev

1. Gerçek import sistemini değiştirmeden üç gereksinim için tasarım seç: bütün standart arama düzenini değiştirmek; yalnız import ifadesinin davranışını değiştirmek; belirli bir modülü erken hookta engellemek.

2. Son gereksinimde find_spec None döndürürse sonraki finderın ne yapacağını, ModuleNotFoundError yükselirse ne olacağını adım adım yaz.

#### Geçiş ölçütleri

- [ ] Bütün sistem için sys.meta_path, yalnız ifade için built-in `__import__` sınırı belirtilmiş.
- [ ] None aramaya devam ettirir; engelleme garantisi değildir.
- [ ] ModuleNotFoundError zinciri durdurur.
- [ ] importlib gibi diğer giriş yollarının `__import__` değişiminden etkilenmeyebileceği açıklanmış; canlı sistem değiştirilmemiş.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../5.7-package-relative-imports/README.md)
<!-- learning-task:end -->
