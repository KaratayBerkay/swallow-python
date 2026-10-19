### 5.4.3. Module specs

The import machinery uses a variety of information about each module during import, especially before loading. Most of the information is common to all modules. The purpose of a module's spec is to encapsulate this import-related information on a per-module basis.

Using a spec during import allows state to be transferred between import system components, e.g. between the finder that creates the module spec and the loader that executes it. Most importantly, it allows the import machinery to perform the boilerplate operations of loading, whereas without a module spec the loader had that responsibility.

The module's spec is exposed as `module.__spec__`. Setting `__spec__` appropriately applies equally to modules initialized during interpreter startup. The one exception is `__main__`, where `__spec__` is set to None in some cases.

See `ModuleSpec` for details on the contents of the module spec.

Added in version 3.4.

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 5.4.3: Specin hangi sınırdan bilgi taşıdığını açıkla**

**Odak:** Per-module import metadata, finder/loader arası taşıma ve `__spec__`.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.4.2](../5.4.2-submodules/README.md).

##### Tek görev

1. math ve kendi küçük modülünü import edip `__spec__` değerlerini yalnız gözlemle.

2. Bir çizimde specin finder tarafından üretildiği yeri, import machinery ve loader tarafından kullanılma amacını göster.

3. Aynı isimli modülün verisini taşıyan `__dict__` ile import bilgisini taşıyan `__spec__` rollerini ayır; `__main__` için her zaman dolu olduğunu varsayma.

##### Geçiş ölçütleri

- [ ] Spec modülün import bilgisi; kullanıcı iş verisi yerine konmamış.
- [ ] Finder -> spec -> machinery/loader ilişkisi doğru.
- [ ] `__spec__` modülden gözlemlenmiş; gösterimdeki adres veya her alanın aynı olması beklenmemiş.
- [ ] `__main__` istisnası belirtilmiş; ileride açıklanacak bütün başlatma türleri ezberden istenmemiş.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../5.4.4-path-attributes-on-modules/README.md)
<!-- learning-task:end -->
