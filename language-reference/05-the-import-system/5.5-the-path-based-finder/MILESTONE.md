# Milestone: Bir yol girdisini seçme izini tamamla

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** PathFinder, path hook, importer cache ve namespace portion teslimini birleştirme.

## Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

## Tek görev

1. Bir paket alt modülü için `__path__` iki metin girdisi içeriyor.

2. İlk girdinin cache değeri None; ikincisi cachete yok, ilk hook reddediyor, ikinci hook namespace portion bilgisi veren finder döndürüyor.

3. Çalıştırmadan tam arama izini ve iki cachein anahtar/değerlerini çiz.

4. İkinci aynı aramada hangi seçme işinin tekrar edilmediğini göster.

## Geçiş ölçütleri

- [ ] PathFinder meta path aşamasından path girişlerine iniyor.
- [ ] İlk girdinin None kaydı modül için zorunlu ModuleNotFoundError sanılmamış.
- [ ] İkinci girdide hook ImportError reddiyle devam, finder cache kaydı ve find_spec teslimi ayrı.
- [ ] Namespace portion submodule_search_locations ile belirtilmiş.
- [ ] Sonraki aramada hookla finder seçimi cacheten; module cache ile karıştırılmamış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
