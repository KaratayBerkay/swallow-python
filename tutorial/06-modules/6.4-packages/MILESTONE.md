# Milestone: Paketin dışarı açtığı adları tasarla

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Paket ağacı, mutlak/göreli import ve `__all__` sözleşmesi.

## Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

## Tek görev

1. studytools paketinde core/counts.py ve reports/summary.py oluştur; ara paketlerin `__init__`.py dosyaları olsun. counts bir liste uzunluğu işlevi versin; summary bu işlevi göreli importla kullanıp metin değil sayısal özet döndürsün. reports/`__init__`.py için `__all__` ile yalnız summary modülünü dışarı aç.

2. Üç import biçimiyle kullanıcıya hangi adın bağlandığını ayrı oturumlarda göster.

## Geçiş ölçütleri

- [ ] Göreli import ..core üzerinden doğru hedefe gidiyor.
- [ ] Kullanıcı paketinden çağrı gerçek sayısal sonuç veriyor.
- [ ] `__all__` yalnız belirlenen modülü dışarı açıyor; disk otomatik tarama varsayımı yok.
- [ ] Paket bağlamıyla doğrudan dosya çalıştırması karıştırılmamış; kaynak örneklerdeki boş stub çıktısı gerçek işlev diye sunulmamış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
