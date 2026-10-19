# Milestone: Python ile yerel ve sınanabilir bir veri akışı kur

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Tutorial boyunca öğrenilenleri yeni ama küçük bir programda birleştirme.

## Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

## Tek görev

1. Bir yerel reading_log paketi oluştur.

2. JSON dosyasında ad, okunan sayfa ve ücret metni kayıtları olsun. argparse ile dosya ve yalnız anahtarlı bir rapor seçeneği al; kayıtları bir sınıfla yönet, generator ile dolaş, ad başına sayfaları sözlükte biriktir ve Decimal ücretleri topla.

3. Geçersiz kayıtları satır/kayıt notlarıyla toplayıp ExceptionGroup ile raporla; bütün dosyaları with ile yönet.

4. Çıktıyı hizalı yerel metin dosyası yap.

5. Normal, boş, yinelenen ad, geçersiz sayı ve eksik dosya senaryolarını göster; en az iki anlamlı test yaz.

6. Önce davranış sözleşmesini kendin yaz, sonra uygulamayı ona göre doğrula.

## Geçiş ölçütleri

- [ ] Girdi -> nesne -> dönüşüm -> rapor akışı gerçek yerel dosyalarla tamamlanmış.
- [ ] Kayıt sahipliği, modül/örnek kapsamı, generator tüketimi ve dict/set seçimi gerekçeli.
- [ ] Geçersiz kayıt bütün geçerli veriyi sessizce kaybettirmiyor; hata ve kaynak temizliği ayrı.
- [ ] Hesap ile Decimal/float/metin gösterimi ayrılmış.
- [ ] Testler normal sonuç kadar hata/veri sınırı da kontrol ediyor; bilerek bozulan bir davranışı yakalıyor.
- [ ] Yeni veri ve küçük gereksinim değişikliğinde sonucu önce türetip sonra programla doğrulayabiliyor.
- [ ] Ağ, framework, üçüncü taraf paket, veritabanı, decorator yazımı veya işlenmemiş dil özelliği gerekmiyor.

[Değerlendirme yöntemi](../DEGERLENDIRME.md) · [Sıra](../TASKS.md)
