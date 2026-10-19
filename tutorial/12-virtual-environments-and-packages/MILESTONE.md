# Milestone: İki uygulamanın bağımlılık planını yeniden üretilebilir yap

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Ortam seçimi, yorumlayıcı sürümü, pip sürüm sabitleme ve freeze aktarımı.

## Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

## Tek görev

1. [12.2 görevinin](12.2-creating-virtual-environments/TASK.md) gerçek oluşturma/etkinleştirme/deactivate kanıtını kullan; aynı ortamı yeniden kurma. Bu yerel deneyden hareketle A için lib 1.0, B için lib 2.0 gereksinimini iki ayrı ortam planına çevir.

2. Her ortamın hangi yorumlayıcıyla oluşturulacağını, aktif python/pip eşleşmesini nasıl koruyacağını ve gereksinim dosyasının nasıl üretileceğini yaz.

3. B yükseltildikten sonra A tarafında değişmemesi gereken durumu göster; ikinci bir temiz B ortamını requirements üzerinden kurma komutunu taslak olarak ekle.

4. Paket kurma/yükseltme komutları taslak kalır; ağ veya ek paket kurulumu gerekmez. Gerçek ortam deneyiyle yalnız planlanan paket işlemlerini kayıtta ayrı göster.

## Geçiş ölçütleri

- [ ] A/B ortamları ve paket sürümleri açıkça ayrı.
- [ ] python -m pip seçilen yorumlayıcıyla ilişkili.
- [ ] requirements dosyası tam sürüm verilerini taşıyor; list çıktısı yerine freeze biçimi kullanılmış.
- [ ] Etkinleştirme ile bağımlılık yükleme aynı işlem sanılmamış; PYTHONPATH sınırı not edilmiş.
- [ ] 12.2 uygulama kanıtı mevcut; yalnız planla bütün klasörün uygulama becerisi doğrulanmış sayılmamış.
- [ ] Taslak kurulum gerçekten yapılmış gibi raporlanmamış.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md) · [Sıra](../../TASKS.md)
