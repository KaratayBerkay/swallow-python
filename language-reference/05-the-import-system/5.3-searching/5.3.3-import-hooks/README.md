### 5.3.3. Import hooks

The import machinery is designed to be extensible; the primary mechanism for this are the *import hooks*. There are two types of import hooks: *meta hooks* and *import path hooks*.

Meta hooks are called at the start of import processing, before any other import processing has occurred, other than `sys.modules` cache look up. This allows meta hooks to override `sys.path` processing, frozen modules, or even built-in modules. Meta hooks are registered by adding new finder objects to `sys.meta_path`, as described below.

Import path hooks are called as part of `sys.path` (or `package.__path__`) processing, at the point where their associated path item is encountered. Import path hooks are registered by adding new callables to `sys.path_hooks` as described below.

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 5.3.3: Hookun hangi aşamaya girdiğini seç**

**Odak:** Meta hook ile path hook giriş noktalarının farkı.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.3.2](../5.3.2-finders-and-loaders/README.md).

##### Tek görev

1. İki gereksinimi kağıt üzerinde doğru hook listesine yerleştir: cache başarısız olduktan sonra built-in araması dahil normal arama akışının önüne geçmek; yalnız özel bir arama yolu girdisiyle karşılaşınca o girdiyi ele almak.

2. Her biri için sys.modules, sys.meta_path ve sys.path_hooks sırasındaki yerini göster.

##### Geçiş ölçütleri

- [ ] İlk gereksinim meta hook/sys.meta_path, ikinci path hook/sys.path_hooks.
- [ ] Cache kontrolü meta hooktan önce.
- [ ] Path hook bütün importların ilk aşaması sayılmamış; sys.path veya paket `__path__` işlenirken devreye giriyor.
- [ ] Bu bölümde protokol uygulaması gösterilmediği için yeni hook sınıfı yazılmamış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../5.3.4-the-meta-path/README.md)
<!-- learning-task:end -->
