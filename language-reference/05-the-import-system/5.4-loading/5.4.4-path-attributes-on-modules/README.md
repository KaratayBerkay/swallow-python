### 5.4.4. \_\_path\_\_ attributes on modules

The `__path__` attribute should be a (possibly empty) sequence of strings enumerating the locations where the package's submodules will be found. By definition, if a module has a `__path__` attribute, it is a package.

A package's `__path__` attribute is used during imports of its subpackages. Within the import machinery, it functions much the same as `sys.path`, i.e. providing a list of locations to search for modules during import. However, `__path__` is typically much more constrained than `sys.path`.

The same rules used for `sys.path` also apply to a package's `__path__`. `sys.path_hooks` (described below) are consulted when traversing a package's `__path__`.

A package's `__init__.py` file may set or alter the package's `__path__` attribute, and this was typically the way namespace packages were implemented prior to [**PEP 420**](https://peps.python.org/pep-0420/). With the adoption of [**PEP 420**](https://peps.python.org/pep-0420/), namespace packages no longer need to supply `__init__.py` files containing only `__path__` manipulation code; the import machinery automatically sets `__path__` correctly for the namespace package.

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 5.4.4: Paket aramasının kapsamını daralt**

**Odak:** `__path__` ile alt modül arama, sys.path farkı ve namespace yolu.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.4.3](../5.4.3-module-specs/README.md).

##### Tek görev

1. Üst düzey sys.path = ["/global", "/plugins"], `lessonpack.__path__` = ["/plugins/lessonpack"] varsay. lessonpack.tools importunda hangi yolun tarandığını ve neden bütün sys.path girdilerinin doğrudan tools aramasına çevrilmediğini çiz. `__path__` boşken paket sayılma ile alt modül bulunabilirliğini ayrı değerlendir; regular/namespace paketlerde yolun nasıl hazırlanabildiğini açıkla.

##### Geçiş ölçütleri

- [ ] Alt arama ebeveyn `lessonpack.__path__` üzerinden.
- [ ] `__path__` varlığı paket ölçütü; boş olma tek başına normal modüle dönüştürmüyor.
- [ ] sys.path_hooks paket yollarında da kullanılabiliyor.
- [ ] Regular paket başlangıç dosyası yolu değiştirebilir; namespace yolu machinery tarafından hazırlanır; gerçek sistem yolu değiştirilmemiş.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../5.4.5-module-reprs/README.md)
<!-- learning-task:end -->
