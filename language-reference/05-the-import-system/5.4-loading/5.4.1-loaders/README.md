### 5.4.1. Loaders

Module loaders provide the critical function of loading: module execution. The import machinery calls the `importlib.abc.Loader.exec_module()` method with a single argument, the module object to execute. Any value returned from `exec_module()` is ignored.

Loaders must satisfy the following requirements:

- If the module is a Python module (as opposed to a built-in module or a dynamically loaded extension), the loader should execute the module's code in the module's global name space (`module.__dict__`).

- If the loader cannot execute the module, it should raise an `ImportError`, although any other exception raised during `exec_module()` will be propagated.

In many cases, the finder and loader can be the same object; in such cases the `find_spec()` method would just return a spec with the loader set to `self`.

Module loaders may opt in to creating the module object during loading by implementing a `create_module()` method. It takes one argument, the module spec, and returns the new module object to use during loading. `create_module()` does not need to set any attributes on the module object. If the method returns `None`, the import machinery will create the new module itself.

Added in version 3.4: The `create_module()` method of loaders.

Changed in version 3.4: The `importlib.abc.Loader.load_module` method was replaced by `exec_module()` and the import machinery assumed all the boilerplate responsibilities of loading.

For compatibility with existing loaders, the import machinery will use the `load_module()` method of loaders if it exists and the loader does not also implement `exec_module()`. However, `load_module()` has been deprecated and loaders should implement `exec_module()` instead.

The `load_module()` method must implement all the boilerplate loading functionality described above in addition to executing the module. All the same constraints apply, with some additional clarification:

- If there is an existing module object with the given name in `sys.modules`, the loader must use that existing module. (Otherwise, `importlib.reload()` will not work correctly.) If the named module does not exist in `sys.modules`, the loader must create a new module object and add it to `sys.modules`.

- The module *must* exist in `sys.modules` before the loader executes the module code, to prevent unbounded recursion or multiple loading.

- If loading fails, the loader must remove any modules it has inserted into `sys.modules`, but it must remove **only** the failing module(s), and only if the loader itself has loaded the module(s) explicitly.

Changed in version 3.5: A `DeprecationWarning` is raised when `exec_module()` is defined but `create_module()` is not.

Changed in version 3.6: An `ImportError` is raised when `exec_module()` is defined but `create_module()` is not.

Changed in version 3.10: Use of `load_module()` will raise `ImportWarning`.

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 5.4.1: Loaderın sorumluluğunu makineninkinden ayır**

**Odak:** create_module/exec_module, dönüş değeri, modül namespace ve tarihsel load_module.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.4](../README.md).

**Kaynak/ortam notu:** Bu sayfada eski load_module uyumluluk paragrafları duruyor; üst 5.4 bölümündeki 3.15 kaldırılma notuyla birlikte oku. Görev modern create_module/exec_module sözleşmesini esas alır.

##### Tek görev

1. Kod yazmadan loader sözleşme tablosu hazırla: create_module yeni nesne döndürüyor; create_module None döndürüyor; exec_module başarılı ama 123 döndürüyor; exec_module hata yükseltiyor.

2. Her satırda yaratmayı kim tamamlar, modülün verisi nerede oluşur ve sonuç/hata nasıl ele alınır yaz.

3. Metindeki load_module gerekliliklerini tarihsel API sütununda tut.

##### Geçiş ölçütleri

- [ ] create_module None ise import machinery nesneyi oluşturuyor.
- [ ] exec_module kendisine verilen modülün namespace alanını dolduruyor, dönüşte 123 kullanılması gerekmiyor.
- [ ] Yükleyememe ImportError olabilir; diğer hatalar da yayılır.
- [ ] Eski load_module boilerplate sorumlulukları modern exec_module sorumluluğuyla karıştırılmamış.
- [ ] 3.15 hedefinde eski fallback güncel sözleşme sayılmamış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../5.4.2-submodules/README.md)
<!-- learning-task:end -->
