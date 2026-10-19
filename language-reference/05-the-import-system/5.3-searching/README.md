## 5.3. Searching

To begin the search, Python needs the fully qualified name of the module (or package, but for the purposes of this discussion, the difference is immaterial) being imported. This name may come from various arguments to the `import` statement, or from the parameters to the `importlib.import_module()` or `__import__()` functions.

This name will be used in various phases of the import search, and it may be the dotted path to a submodule, e.g. `foo.bar.baz`. In this case, Python first tries to import `foo`, then `foo.bar`, and finally `foo.bar.baz`. If any of the intermediate imports fail, a `ModuleNotFoundError` is raised.


<!-- learning-task:start -->
### Bölüm görevi

**Görev 5.3: Noktalı importu sırayla çöz**

**Odak:** Tam nitelikli ad, ebeveynleri sırayla içe aktarma ve ara düzeyde hata.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.2.2](../5.2-packages/5.2.2-namespace-packages/README.md).

#### Tek görev

1. foo.bar.baz için üç arama aşaması yaz.

2. Ayrı senaryolarda foo yok, foo var ama bar yok, bütün ebeveynler var ama baz yok kabul et.

3. Her durumda hangi aşamaya kadar gelindiğini ve hangi hata ile durulduğunu göster.

4. Ebeveynler bulunmadan doğrudan son dosyaya gitmenin neden doğru model olmadığını açıkla.

#### Geçiş ölçütleri

- [ ] Sıra foo, foo.bar, foo.bar.baz.
- [ ] Hata ilgili ilk başarısız düzeyde ModuleNotFoundError; sonrası yürütülmüyor.
- [ ] Tam adın disk yolu değil import adı olduğu ayrılmış.
- [ ] Henüz alt bölümdeki cache/finder ayrıntılarıyla yeni mekanizma tasarlamak gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](5.3.1-the-module-cache/README.md)
<!-- learning-task:end -->
### Sections

- [5.3.1. The module cache](5.3.1-the-module-cache/README.md)
- [5.3.2. Finders and loaders](5.3.2-finders-and-loaders/README.md)
- [5.3.3. Import hooks](5.3.3-import-hooks/README.md)
- [5.3.4. The meta path](5.3.4-the-meta-path/README.md)

<!-- learning-milestone:start -->
### Klasör milestone görevi

**Milestone: Arama kararını cacheten spec teslimine kadar izle**

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Cache, noktalı ad, finder sırası ve hook katmanlarının birlikte kullanımı.

#### Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

#### Tek görev

1. foo.bar importunda foo cachete modül nesnesi, foo.bar cachete yok olsun.

2. İki meta finder sırasıyla None ve spec döndürsün.

3. Tam ad, path ve target argümanlarıyla olay izini yaz.

4. Sonra yalnız foo.bar cache değerini None kabul edip izi yeniden çıkar; son olarak ilk finderın hata yükseltmesi durumunu karşılaştır.

#### Geçiş ölçütleri

- [ ] Cacheteki ebeveyn yeniden yürütülmüyor; alt ad için arama var.
- [ ] Alt adın pathi `foo.__path__`, normal target None.
- [ ] None cache kaydı arama başlatmadan hata; finder None sonucu sonraki findera geçiş.
- [ ] Finder hatası zinciri durduruyor; spec bulunması yürütme ile aynı aşama sayılmamış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../5.4-loading/README.md)
<!-- learning-milestone:end -->
