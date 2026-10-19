# Python Tutorial

Her numaralı klasörde anlatım ve örnekler bulunur. Bazı .py dosyaları tek başına çalışan program değil, REPL parçası, kasıtlı hata veya örnek iskeletidir.

[Sayısal öğrenme ve görev sırası](../TASKS.md) · [Değerlendirme yöntemi](../DEGERLENDIRME.md)

## Bölümler

- [2. Using the Python Interpreter](02-using-the-python-interpreter/README.md)
- [3. An Informal Introduction to Python](03-an-informal-introduction-to-python/README.md)
- [4. More Control Flow Tools](04-more-control-flow-tools/README.md)
- [5. Data Structures](05-data-structures/README.md)
- [6. Modules](06-modules/README.md)
- [7. Input and output](07-input-and-output/README.md)
- [8. Errors and Exceptions](08-errors-and-exceptions/README.md)
- [9. Classes](09-classes/README.md)
- [10. Brief tour of the standard library](10-brief-tour-of-the-standard-library/README.md)
- [11. Brief tour of the standard library --- part II](11-brief-tour-of-the-standard-library-part-ii/README.md)
- [12. Virtual Environments and Packages](12-virtual-environments-and-packages/README.md)
- [13. What Now?](13-what-now/README.md)
- [14. Interactive Input Editing and History Substitution](14-interactive-input-editing-and-history-substitution/README.md)
- [15. Floating-Point Arithmetic: Issues and Limitations](15-floating-point-arithmetic-issues-and-limitations/README.md)
- [16. Appendix](16-appendix/README.md)

Bölüm görevinin metni aynı README sayfasında, anlatım ve örneklerden hemen sonra görünür. Milestone bütün alt bölümlerden sonra yapılır. Kontrolün sonundaki **Sonraki adım** bağlantısı okuma sırasını korur.

<!-- learning-milestone:start -->
## Klasör milestone görevi

**Milestone: Python ile yerel ve sınanabilir bir veri akışı kur**

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Tutorial boyunca öğrenilenleri yeni ama küçük bir programda birleştirme.

### Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

### Tek görev

1. Bir yerel reading_log paketi oluştur.

2. JSON dosyasında ad, okunan sayfa ve ücret metni kayıtları olsun. argparse ile dosya ve yalnız anahtarlı bir rapor seçeneği al; kayıtları bir sınıfla yönet, generator ile dolaş, ad başına sayfaları sözlükte biriktir ve Decimal ücretleri topla.

3. Geçersiz kayıtları satır/kayıt notlarıyla toplayıp ExceptionGroup ile raporla; bütün dosyaları with ile yönet.

4. Çıktıyı hizalı yerel metin dosyası yap.

5. Normal, boş, yinelenen ad, geçersiz sayı ve eksik dosya senaryolarını göster; en az iki anlamlı test yaz.

6. Önce davranış sözleşmesini kendin yaz, sonra uygulamayı ona göre doğrula.

### Geçiş ölçütleri

- [ ] Girdi -> nesne -> dönüşüm -> rapor akışı gerçek yerel dosyalarla tamamlanmış.
- [ ] Kayıt sahipliği, modül/örnek kapsamı, generator tüketimi ve dict/set seçimi gerekçeli.
- [ ] Geçersiz kayıt bütün geçerli veriyi sessizce kaybettirmiyor; hata ve kaynak temizliği ayrı.
- [ ] Hesap ile Decimal/float/metin gösterimi ayrılmış.
- [ ] Testler normal sonuç kadar hata/veri sınırı da kontrol ediyor; bilerek bozulan bir davranışı yakalıyor.
- [ ] Yeni veri ve küçük gereksinim değişikliğinde sonucu önce türetip sonra programla doğrulayabiliyor.
- [ ] Ağ, framework, üçüncü taraf paket, veritabanı, decorator yazımı veya işlenmemiş dil özelliği gerekmiyor.

[Değerlendirme yöntemi](../DEGERLENDIRME.md) · [Sıra](../TASKS.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../language-reference/05-the-import-system/README.md)
<!-- learning-milestone:end -->
