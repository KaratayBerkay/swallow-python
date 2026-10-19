# Milestone: Arama kararını cacheten spec teslimine kadar izle

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Cache, noktalı ad, finder sırası ve hook katmanlarının birlikte kullanımı.

## Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

## Tek görev

1. foo.bar importunda foo cachete modül nesnesi, foo.bar cachete yok olsun.

2. İki meta finder sırasıyla None ve spec döndürsün.

3. Tam ad, path ve target argümanlarıyla olay izini yaz.

4. Sonra yalnız foo.bar cache değerini None kabul edip izi yeniden çıkar; son olarak ilk finderın hata yükseltmesi durumunu karşılaştır.

## Geçiş ölçütleri

- [ ] Cacheteki ebeveyn yeniden yürütülmüyor; alt ad için arama var.
- [ ] Alt adın pathi `foo.__path__`, normal target None.
- [ ] None cache kaydı arama başlatmadan hata; finder None sonucu sonraki findera geçiş.
- [ ] Finder hatası zinciri durduruyor; spec bulunması yürütme ile aynı aşama sayılmamış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
