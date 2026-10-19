# Milestone: Küçük bir yerel rapor aracını sınır durumlarıyla doğrula

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Standart modül seçimi, argüman doğrulama, dosya seçimi, tarih/istatistik ve test.

## Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

## Tek görev

1. argparse ile bir veya daha çok dosya adı alan küçük araç kur.

2. Çalışma klasöründe glob ile .txt dosyalarını listele; açıkça verilen dosyaları with ile oku ve her dosyanın karakter sayısını çıkar.

3. Tarih etiketi, mean karakter sayısı ve zlib ile geri açılabilir bir rapor üret.

4. En az bir saf hesap işlevini doctest veya unittest ile normal/boş veri durumlarında kontrol et.

5. Ağ/email bölümü için hangi adımın dış yan etki olacağını yalnız tasarım notunda belirt.

## Geçiş ölçütleri

- [ ] Dosya adları ve .txt keşfi ayrı sorumluluklar; kaynak dosyalar korunmuş.
- [ ] Boş koleksiyon davranışı bilinçli; ilgisiz hatalar sessizce yutulmuyor.
- [ ] Tarih etiketiyle hesap verisi ayrılmış, sıkıştırma geri dönüş eşitliğiyle doğrulanmış.
- [ ] Rastgelelik veya makineye bağlı zaman sabit sonuç ölçütü yapılmamış.
- [ ] Bir test bozulduğunda başarısız olduğu gösterilmiş; gerçek ağ/gönderim yok.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md) · [Sıra](../../TASKS.md)
