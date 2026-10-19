### 5.3.2. Finders and loaders

If the named module is not found in `sys.modules`, then Python's import protocol is invoked to find and load the module. This protocol consists of two conceptual objects, finders and loaders. A finder's job is to determine whether it can find the named module using whatever strategy it knows about. Objects that implement both of these interfaces are referred to as importers - they return themselves when they find that they can load the requested module.

Python includes a number of default finders and importers. The first one knows how to locate built-in modules, and the second knows how to locate frozen modules. A third default finder searches an import path for modules. The import path is a list of locations that may name file system paths or zip files. It can also be extended to search for any locatable resource, such as those identified by URLs.

The import machinery is extensible, so new finders can be added to extend the range and scope of module searching.

Finders do not actually load modules. If they can find the named module, they return a *module spec*, an encapsulation of the module's import-related information, which the import machinery then uses when loading the module.

The following sections describe the protocol for finders and loaders in more detail, including how you can create and register new ones to extend the import machinery.

Changed in version 3.4: In previous versions of Python, finders returned loaders directly, whereas now they return module specs which *contain* loaders. Loaders are still used during import but have fewer responsibilities.

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 5.3.2: Bulucuyla yükleyicinin teslim sınırını çiz**

**Odak:** Finder modül bilgisini/spec bulur, loader yürütür; importer iki rolü birleştirebilir.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.3.1](../5.3.1-the-module-cache/README.md).

##### Tek görev

1. Bir modülün cache içinde olmadığı durumu çiz: arama isteği, finder, module spec, loader ve modül yürütmesi.

2. Disk, frozen ve built-in kaynaklarını bu çizimdeki arama stratejilerine yerleştir.

3. Finder spec döndüğünde modül gövdesinin yürümüş sayılıp sayılamayacağını açıkla.

##### Geçiş ölçütleri

- [ ] Finder keşif, loader yürütme; spec aradaki bilgi aktarımı.
- [ ] Spec loader bilgisini içeriyor; finder doğrudan modül kodunu yürütmek zorunda değil.
- [ ] Aynı nesnenin iki rolü gerçekleştirebileceği importer kavramıyla açıklanmış.
- [ ] Eski finderın doğrudan loader döndürmesi tarihsel bilgi olarak ayrılmış; güncel iş akışına taşınmamış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../5.3.3-import-hooks/README.md)
<!-- learning-task:end -->
