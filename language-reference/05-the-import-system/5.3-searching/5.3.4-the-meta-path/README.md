### 5.3.4. The meta path

When the named module is not found in `sys.modules`, Python next searches `sys.meta_path`, which contains a list of meta path finder objects. These finders are queried in order to see if they know how to handle the named module. Meta path finders must implement a method called `find_spec()` which takes three arguments: a name, an import path, and (optionally) a target module. The meta path finder can use any strategy it wants to determine whether it can handle the named module or not.

If the meta path finder knows how to handle the named module, it returns a spec object. If it cannot handle the named module, it returns `None`. If `sys.meta_path` processing reaches the end of its list without returning a spec, then a `ModuleNotFoundError` is raised. Any other exceptions raised are simply propagated up, aborting the import process.

The `find_spec()` method of meta path finders is called with two or three arguments. The first is the fully qualified name of the module being imported, for example `foo.bar.baz`. The second argument is the path entries to use for the module search. For top-level modules, the second argument is `None`, but for submodules or subpackages, the second argument is the value of the parent package's `__path__` attribute. If the appropriate `__path__` attribute cannot be accessed, a `ModuleNotFoundError` is raised. The third argument is an existing module object that will be the target of loading later. The import system passes in a target module only during reload.

The meta path may be traversed multiple times for a single import request. For example, assuming none of the modules involved has already been cached, importing `foo.bar.baz` will first perform a top level import, calling `mpf.find_spec("foo", None, None)` on each meta path finder (`mpf`). After `foo` has been imported, `foo.bar` will be imported by traversing the meta path a second time, calling `mpf.find_spec("foo.bar", foo.__path__, None)`. Once `foo.bar` has been imported, the final traversal will call `mpf.find_spec("foo.bar.baz", foo.bar.__path__, None)`.

Some meta path finders only support top level imports. These importers will always return `None` when anything other than `None` is passed as the second argument.

Python's default `sys.meta_path` has three meta path finders, one that knows how to import built-in modules, one that knows how to import frozen modules, and one that knows how to import modules from an import path (i.e. the path based finder).

Changed in version 3.4: The `find_spec()` method of meta path finders replaced `find_module()`, which is now deprecated. While it will continue to work without change, the import machinery will try it only if the finder does not implement `find_spec()`.

Changed in version 3.10: Use of `find_module()` by the import system now raises `ImportWarning`.

Changed in version 3.12: `find_module()` has been removed. Use `find_spec()` instead.

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 5.3.4: Meta path taramasının devam ve durma koşullarını izle**

**Odak:** find_spec argümanları, None/spec/hata sonuçları, cache sonrası sıra ve reload target.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.3.3](../5.3.3-import-hooks/README.md).

##### Tek görev

1. Cache boş ve meta path sırası F1, F2, F3 olsun.

2. F1 None, F2 spec, F3 hata verecek şekilde tanımlandığında hangi çağrılar gerçekleşir?

3. Sonra F1 hata versin; sonra hepsi None versin. foo.bar.baz için tam ad/path/target argümanlarını her ebeveyn düzeyinde tabloya yaz; foo.bar reload olduğunda target farkını belirt.

##### Geçiş ölçütleri

- [ ] İlk senaryoda F3 çağrılmaz; ikinci hata hemen yayılır; hepsi None ise ModuleNotFoundError.
- [ ] Üst düzey path None, alt düzeylerde ebeveyn `__path__`.
- [ ] Normal import target None; reload mevcut modül hedefi kullanıyor.
- [ ] Noktalı import için meta path birden fazla kez dolaşılabiliyor.
- [ ] Built-in/frozen/path finder rolleri ve kaldırılmış find_module yerine find_spec kullanımı ayrılmış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
