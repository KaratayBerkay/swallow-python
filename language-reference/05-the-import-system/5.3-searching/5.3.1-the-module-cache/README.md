### 5.3.1. The module cache

The first place checked during import search is `sys.modules`. This mapping serves as a cache of all modules that have been previously imported, including the intermediate paths. So if `foo.bar.baz` was previously imported, `sys.modules` will contain entries for `foo`, `foo.bar`, and `foo.bar.baz`. Each key will have as its value the corresponding module object.

During import, the module name is looked up in `sys.modules` and if present, the associated value is the module satisfying the import, and the process completes. However, if the value is `None`, then a `ModuleNotFoundError` is raised. If the module name is missing, Python will continue searching for the module.

`sys.modules` is writable. Deleting a key may not destroy the associated module (as other modules may hold references to it), but it will invalidate the cache entry for the named module, causing Python to search anew for the named module upon its next import. The key can also be assigned to `None`, forcing the next import of the module to result in a `ModuleNotFoundError`.

Beware though, as if you keep a reference to the module object, invalidate its cache entry in `sys.modules`, and then re-import the named module, the two module objects will *not* be the same. By contrast, `importlib.reload()` will reuse the *same* module object, and simply reinitialise the module contents by rerunning the module's code.

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 5.3.1: Eksik cache kaydıyla None kaydını ayır**

**Odak:** sys.modules başarı/None/eksik durumları, silme ile nesne ömrü ve reload kimliği.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.3](../README.md).
- Ön bilgi: [t:9.1](../../../../tutorial/09-classes/9.1-a-word-about-names-and-objects/README.md).

##### Tek görev

1. Gerçek sys.modules üzerinde değişiklik yapmadan bir durum tablosu hazırla: x anahtarı modül nesnesi gösteriyor; x değeri None; x anahtarı yok.

2. Her birinin sonraki import sonucunu yaz.

3. Sonra eski modül nesnesine old referansı tutulurken cache anahtarı silinip yeniden import ve importlib.reload senaryolarının kimlik ilişkisini çiz.

##### Geçiş ölçütleri

- [ ] Modül nesnesi varsa arama erken döner; None doğrudan ModuleNotFoundError; eksik kayıt aramaya devam.
- [ ] Cache silme eski nesneyi eldeki başka bağlardan yok etmiyor.
- [ ] Silip yeniden import yeni nesne; reload aynı modül nesnesini yeniden başlatır.
- [ ] Cache anahtarı ile yerel değişken adının yaşamı ayrılmış; canlı modül cache değiştirme gerekmiyor.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../5.3.2-finders-and-loaders/README.md)
<!-- learning-task:end -->
