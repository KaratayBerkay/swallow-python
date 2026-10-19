### 5.5.2. Path entry finder protocol

In order to support imports of modules and initialized packages and also to contribute portions to namespace packages, path entry finders must implement the `find_spec()` method.

`find_spec()` takes two arguments: the fully qualified name of the module being imported, and the (optional) target module. `find_spec()` returns a fully populated spec for the module. This spec will always have "loader" set (with one exception).

To indicate to the import machinery that the spec represents a namespace portion, the path entry finder sets `submodule_search_locations` to a list containing the portion.

Changed in version 3.4: `find_spec()` replaced `find_loader()` and `find_module()`, both of which are now deprecated, but will be used if `find_spec()` is not defined.

Older path entry finders may implement one of these two deprecated methods instead of `find_spec()`. The methods are still respected for the sake of backward compatibility. However, if `find_spec()` is implemented on the path entry finder, the legacy methods are ignored.

`find_loader()` takes one argument, the fully qualified name of the module being imported. `find_loader()` returns a 2-tuple where the first item is the loader and the second item is a namespace portion.

For backwards compatibility with other implementations of the import protocol, many path entry finders also support the same, traditional `find_module()` method that meta path finders support. However path entry finder `find_module()` methods are never called with a `path` argument (they are expected to record the appropriate path information from the initial call to the path hook).

The `find_module()` method on path entry finders is deprecated, as it does not allow the path entry finder to contribute portions to namespace packages. If both `find_loader()` and `find_module()` exist on a path entry finder, the import system will always call `find_loader()` in preference to `find_module()`.

Changed in version 3.10: Calls to `find_module()` and `find_loader()` by the import system will raise `ImportWarning`.

Changed in version 3.12: `find_module()` and `find_loader()` have been removed.

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 5.5.2: Path finder protokolünü doğru imzayla oku**

**Odak:** Path entry find_spec imzası, loader/spec ve namespace portion bilgisi.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.5.1](../5.5.1-path-entry-finders/README.md).

##### Tek görev

1. Meta path finder ile path entry finder için find_spec çağrılarının parametrelerini yan yana yaz.

2. Normal modül speci ile namespace portion bildiren specin hangi bilgiyi farklı taşıdığını göster.

3. Kaynaktaki find_loader/find_module yöntemlerini tarihsel olarak etiketle; bunlarla yeni bir finder yazma.

##### Geçiş ölçütleri

- [ ] Meta path fullname/path/target; path entry fullname/target olarak ayrılmış.
- [ ] Normal spec loader bilgisi taşır; namespace portion submodule_search_locations ile bildirilir.
- [ ] Path entry finder yolu başlangıçtaki hook seçiminden zaten biliyor.
- [ ] 3.12 ile kaldırılan eski protokoller güncel zorunluluk sanılmamış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
