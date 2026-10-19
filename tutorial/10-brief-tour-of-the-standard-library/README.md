# 10. Brief tour of the standard library

## Sections

- [10.1. Operating system interface](10.1-operating-system-interface/README.md)
- [10.2. File wildcards](10.2-file-wildcards/README.md)
- [10.3. Command-line arguments](10.3-command-line-arguments/README.md)
- [10.4. Error output redirection and program termination](10.4-error-output-redirection-and-program-termination/README.md)
- [10.5. String pattern matching](10.5-string-pattern-matching/README.md)
- [10.6. Mathematics](10.6-mathematics/README.md)
- [10.7. Internet access](10.7-internet-access/README.md)
- [10.8. Dates and times](10.8-dates-and-times/README.md)
- [10.9. Data compression](10.9-data-compression/README.md)
- [10.10. Performance measurement](10.10-performance-measurement/README.md)
- [10.11. Quality control](10.11-quality-control/README.md)
- [10.12. Batteries included](10.12-batteries-included/README.md)

<!-- learning-milestone:start -->
## Klasör milestone görevi

**Milestone: Küçük bir yerel rapor aracını sınır durumlarıyla doğrula**

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Standart modül seçimi, argüman doğrulama, dosya seçimi, tarih/istatistik ve test.

### Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

### Tek görev

1. argparse ile bir veya daha çok dosya adı alan küçük araç kur.

2. Çalışma klasöründe glob ile .txt dosyalarını listele; açıkça verilen dosyaları with ile oku ve her dosyanın karakter sayısını çıkar.

3. Tarih etiketi, mean karakter sayısı ve zlib ile geri açılabilir bir rapor üret.

4. En az bir saf hesap işlevini doctest veya unittest ile normal/boş veri durumlarında kontrol et.

5. Ağ/email bölümü için hangi adımın dış yan etki olacağını yalnız tasarım notunda belirt.

### Geçiş ölçütleri

- [ ] Dosya adları ve .txt keşfi ayrı sorumluluklar; kaynak dosyalar korunmuş.
- [ ] Boş koleksiyon davranışı bilinçli; ilgisiz hatalar sessizce yutulmuyor.
- [ ] Tarih etiketiyle hesap verisi ayrılmış, sıkıştırma geri dönüş eşitliğiyle doğrulanmış.
- [ ] Rastgelelik veya makineye bağlı zaman sabit sonuç ölçütü yapılmamış.
- [ ] Bir test bozulduğunda başarısız olduğu gösterilmiş; gerçek ağ/gönderim yok.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md) · [Sıra](../../TASKS.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../11-brief-tour-of-the-standard-library-part-ii/11.1-output-formatting/README.md)
<!-- learning-milestone:end -->
