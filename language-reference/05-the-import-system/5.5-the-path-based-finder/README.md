## 5.5. The Path Based Finder

As mentioned previously, Python comes with several default meta path finders. One of these, called the path based finder (`PathFinder`), searches an import path, which contains a list of path entries. Each path entry names a location to search for modules.

The path based finder itself doesn't know how to import anything. Instead, it traverses the individual path entries, associating each of them with a path entry finder that knows how to handle that particular kind of path.

The default set of path entry finders implement all the semantics for finding modules on the file system, handling special file types such as Python source code (`.py` files), Python byte code (`.pyc` files) and shared libraries (e.g. `.so` files). When supported by the `zipimport` module in the standard library, the default path entry finders also handle loading all of these file types (other than shared libraries) from zipfiles.

Path entries need not be limited to file system locations. They can refer to URLs, database queries, or any other location that can be specified as a string.

The path based finder provides additional hooks and protocols so that you can extend and customize the types of searchable path entries. For example, if you wanted to support path entries as network URLs, you could write a hook that implements HTTP semantics to find modules on the web. This hook (a callable) would return a path entry finder supporting the protocol described below, which was then used to get a loader for the module from the web.

A word of warning: this section and the previous both use the term *finder*, distinguishing between them by using the terms meta path finder and path entry finder. These two types of finders are very similar, support similar protocols, and function in similar ways during the import process, but it's important to keep in mind that they are subtly different. In particular, meta path finders operate at the beginning of the import process, as keyed off the `sys.meta_path` traversal.

By contrast, path entry finders are in a sense an implementation detail of the path based finder, and in fact, if the path based finder were to be removed from `sys.meta_path`, none of the path entry finder semantics would be invoked.


<!-- learning-task:start -->
### Bölüm görevi

**Görev 5.5: İki finder türünü farklı katmanlara yerleştir**

**Odak:** PathFinder meta path içinde; path entry finder tek bir yol türünü işler.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.4.6](../5.4-loading/5.4.6-cached-bytecode-invalidation/README.md).

#### Tek görev

1. Bir import akışını iki katmanlı çiz: sys.meta_path içindeki PathFinder, altındaki dizin/zip girdileri ve her girdiyi bilen path entry finder.

2. PathFinder listeden kaldırılmış olsaydı path entry hooklarının neden bu yoldan çalışmayacağını açıkla.

3. URL veya veritabanı yolunun kavramsal yerini göster; bu kaynaklar için bağlantı kodu yazman gerekmiyor.

#### Geçiş ölçütleri

- [ ] PathFinder bütün yol girdilerini doğrudan yükleyen loader olarak çizilmemiş.
- [ ] Meta path finder ile path entry finder farklı katmanlarda.
- [ ] PathFinder devreden çıkınca onun alt protokolü de bu arama yolu üzerinden çağrılmıyor.
- [ ] Dizin/zip ve özel konumlar metin girdisi olabiliyor; paylaşımlı kütüphanelerin zip sınırı kaynak notuyla ayrılmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](5.5.1-path-entry-finders/README.md)
<!-- learning-task:end -->
### Sections

- [5.5.1. Path entry finders](5.5.1-path-entry-finders/README.md)
- [5.5.2. Path entry finder protocol](5.5.2-path-entry-finder-protocol/README.md)

<!-- learning-milestone:start -->
### Klasör milestone görevi

**Milestone: Bir yol girdisini seçme izini tamamla**

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** PathFinder, path hook, importer cache ve namespace portion teslimini birleştirme.

#### Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

#### Tek görev

1. Bir paket alt modülü için `__path__` iki metin girdisi içeriyor.

2. İlk girdinin cache değeri None; ikincisi cachete yok, ilk hook reddediyor, ikinci hook namespace portion bilgisi veren finder döndürüyor.

3. Çalıştırmadan tam arama izini ve iki cachein anahtar/değerlerini çiz.

4. İkinci aynı aramada hangi seçme işinin tekrar edilmediğini göster.

#### Geçiş ölçütleri

- [ ] PathFinder meta path aşamasından path girişlerine iniyor.
- [ ] İlk girdinin None kaydı modül için zorunlu ModuleNotFoundError sanılmamış.
- [ ] İkinci girdide hook ImportError reddiyle devam, finder cache kaydı ve find_spec teslimi ayrı.
- [ ] Namespace portion submodule_search_locations ile belirtilmiş.
- [ ] Sonraki aramada hookla finder seçimi cacheten; module cache ile karıştırılmamış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../5.6-replacing-the-standard-import-system/README.md)
<!-- learning-milestone:end -->
