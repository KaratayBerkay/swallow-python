# Milestone: Bir veri dosyasından okunabilir rapor çıkar

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Dosyaya yapılandırılmış kayıt, geri yükleme ve kontrollü metin sunumu.

## Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

## Tek görev

1. İki kişinin adı ve puan listesini içeren veriyi yerel JSON dosyasına kaydet, yeni açılışta yükle.

2. Her kişi için toplamı hesaplayıp ad alanı 10, toplam alanı 4 karakterlik rapor metnini ayrı UTF-8 dosyasına yaz.

3. Dosyayı geri okuyup beklenen iki satırla karşılaştır.

4. Test verisinde boş puan listesi de kullan.

## Geçiş ölçütleri

- [ ] JSON turunda yapı korunuyor; rapor dosyası gerçek hesaplanan veriden oluşuyor.
- [ ] Boş puan listesinin toplamı 0; iki satırın alanları doğru.
- [ ] Kaynak dosya rapor yazımıyla yanlışlıkla ezilmiyor; kaynaklar kapanmış.
- [ ] repr ile boşluk ve satır sonu kanıtı var; daha önce işlenmeyen hata yakalama altyapısı eklenmemiş.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md) · [Sıra](../../TASKS.md)
