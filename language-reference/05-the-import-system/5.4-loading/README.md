## 5.4. Loading

If and when a module spec is found, the import machinery will use it (and the loader it contains) when loading the module. Here is an approximation of what happens during the loading portion of import:

``` python
module = None
if spec.loader is not None and hasattr(spec.loader, 'create_module'):
    # It is assumed 'exec_module' will also be defined on the loader.
    module = spec.loader.create_module(spec)
if module is None:
    module = ModuleType(spec.name)
# The import-related module attributes get set here:
_init_module_attrs(spec, module)

if spec.loader is None:
    # unsupported
    raise ImportError

sys.modules[spec.name] = module
try:
    spec.loader.exec_module(module)
except BaseException:
    try:
        del sys.modules[spec.name]
    except KeyError:
        pass
    raise
return sys.modules[spec.name]
```
> Code: [module.py](module.py)

Note the following details:

- If there is an existing module object with the given name in `sys.modules`, import will have already returned it.

- The module will exist in `sys.modules` before the loader executes the module code. This is crucial because the module code may (directly or indirectly) import itself; adding it to `sys.modules` beforehand prevents unbounded recursion in the worst case and multiple loading in the best.

- If loading fails, the failing module -- and only the failing module -- gets removed from `sys.modules`. Any module already in the `sys.modules` cache, and any module that was successfully loaded as a side-effect, must remain in the cache. This contrasts with reloading where even the failing module is left in `sys.modules`.

- After the module is created but before execution, the import machinery sets the import-related module attributes ("\_init_module_attrs" in the pseudo-code example above), as summarized in a later section.

- Module execution is the key moment of loading in which the module's namespace gets populated. Execution is entirely delegated to the loader, which gets to decide what gets populated and how.

- The module created during loading and passed to exec_module() may not be the one returned at the end of import (The importlib implementation avoids using the return value directly. Instead, it gets the module object by looking the module name up in `sys.modules`. The indirect effect of this is that an imported module may replace itself in `sys.modules`. This is implementation-specific behavior that is not guaranteed to work in other Python implementations.) .

Changed in version 3.4: The import system has taken over the boilerplate responsibilities of loaders. These were previously performed by the `importlib.abc.Loader.load_module` method.

Changed in version 3.15: The `load_module` method is no longer used.


<!-- learning-task:start -->
### Bölüm görevi

**Görev 5.4: Yükleme hatasında yalnız başarısız modülü çıkar**

**Odak:** Modül yaratma, metadata, yürütmeden önce cache, hata temizliği ve dönüş nesnesi.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.3.4](../5.3-searching/5.3.4-the-meta-path/README.md).

**Kaynak/ortam notu:** Bu README kodu yaklaşık bir akıştır ve loader=None durumunu unsupported diye kısaltıyor. Namespace paketler için 5.2.2 anlatımını koru; sözde kodu doğrudan çalışan tam importlib uygulaması sayma. load_module için 3.15 kaldırılma notu geçerlidir.

#### Tek görev

1. README içindeki yükleme sözde kodunu çalıştırmadan bir olay izi çıkar.

2. A modülü yaratılıp cache içine konuyor; A yürürken B başarıyla yükleniyor; sonra A hata veriyor.

3. Cache içinde önceden C de var.

4. Hata sonrasında A/B/C durumunu yaz.

5. İkinci izde A yürütülürken yeniden A istenmesini, üçüncüde loaderın cache içindeki A nesnesini değiştirmesini ele al.

6. Reload hatasını ilk import hatasından ayır.

#### Geçiş ölçütleri

- [ ] Sıra yaratma, metadata hazırlığı, cache kaydı, exec_module; kendini import cache üzerinden çözülüyor.
- [ ] A ilk yükleme hatasında çıkar, B ve önceden C kalır.
- [ ] Dönen nesne sys.modules üzerinden alındığından yürütmeye verilen nesneden farklı olabilir; bu ayrıntı CPython sınırıyla belirtilmiş.
- [ ] Reload hatasında kayıt aynı biçimde silinmiş varsayılmamış.
- [ ] Sözde koddaki loader=None/ImportError satırı bütün namespace paketlerine genellenmemiş.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](5.4.1-loaders/README.md)
<!-- learning-task:end -->
### Sections

- [5.4.1. Loaders](5.4.1-loaders/README.md)
- [5.4.2. Submodules](5.4.2-submodules/README.md)
- [5.4.3. Module specs](5.4.3-module-specs/README.md)
- [5.4.4. \_\_path\_\_ attributes on modules](5.4.4-path-attributes-on-modules/README.md)
- [5.4.5. Module reprs](5.4.5-module-reprs/README.md)
- [5.4.6. Cached bytecode invalidation](5.4.6-cached-bytecode-invalidation/README.md)

<!-- learning-milestone:start -->
### Klasör milestone görevi

**Milestone: Başarısız importun geride bıraktığı durumu değerlendir**

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Yaratma, spec, loader, parent bağı, cache ve bytecode politikasını birleştirme.

#### Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

#### Tek görev

1. Bir package.child ilk kez yükleniyor: parent zaten var; child metadata/cache kaydı hazırlanıyor; child başka modülü başarıyla yüklüyor ve sonra hata veriyor.

2. Son durumu namespace/cache haritasında göster.

3. Aynı akışın başarılı, cache içindeki nesneyi değiştiren ve reload sırasında hata veren varyantlarını karşılaştır.

4. Ayrı bir kod seçimi kararı olarak, diskteki checked hash cache geçersizse eski bytecode'un kullanılmasını mı, kaynaktan yeniden derlemeyi mi beklediğini açıkla. Bytecode geçerliliği ile modül gövdesinin çalışırken hata vermesini ayır.

#### Geçiş ölçütleri

- [ ] İlk hatada child çıkar; parent ve başarıyla yüklenen diğer modül kalır.
- [ ] Başarı durumunda parent.child ile sys.modules kaydı tutarlı.
- [ ] exec_module dönüşü kullanılmıyor; nihai cache nesnesi önem taşıyor.
- [ ] Reload hata temizliği ilk yüklemeyle karıştırılmamış.
- [ ] Spec metadata taşıyor, `__path__` alt aramayı sınırlandırıyor; geçersiz checked hash için kaynak yeniden derleniyor. Bu karar gövdenin hatasız çalışacağı garantisi sayılmamış.
- [ ] Namespace paket durumu kısaltılmış sözde kod yüzünden imkansız sayılmamış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../5.5-the-path-based-finder/README.md)
<!-- learning-milestone:end -->
