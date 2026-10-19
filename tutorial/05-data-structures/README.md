# 5. Data Structures

This chapter describes some things you've learned about already in more detail, and adds some new things as well.

## Sections

- [5.1. More on Lists](5.1-more-on-lists/README.md)
- [5.2. The `del` statement](5.2-the-del-statement/README.md)
- [5.3. Tuples and Sequences](5.3-tuples-and-sequences/README.md)
- [5.4. Sets](5.4-sets/README.md)
- [5.5. Dictionaries](5.5-dictionaries/README.md)
- [5.6. Looping Techniques](5.6-looping-techniques/README.md)
- [5.7. More on Conditions](5.7-more-on-conditions/README.md)
- [5.8. Comparing Sequences and Other Types](5.8-comparing-sequences-and-other-types/README.md)

<!-- learning-milestone:start -->
## Klasör milestone görevi

**Milestone: Katılımcı kayıtlarını veri yapılarına dönüştür**

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Liste/tuple/set/dict, dolaşma, koşul ve sıralama seçimini gerçek veriyle kullanma.

### Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

### Tek görev

1. records = [("Ada", 8), ("Ece", 5), ("Ada", 9), ("Can", 5)] verisinden son görülen puanı tutan bir sözlük, tekrarsız ad kümesi ve puanı en az 8 olan kayıtların yeni listesini üret.

2. Sözlükte eksik "Deniz" için get kullan; Ece kaydını del ile kaldır.

3. Son raporu ad sırasıyla, sıra numarasıyla yazdır.

4. Kaynak kayıtlardaki Ada tekrarının neden listede kalıp sözlükte tek değer olduğunu açıkla.

### Geçiş ölçütleri

- [ ] Sözlük başlangıçta Ada:9, Ece:5, Can:5; set üç ad içeriyor.
- [ ] Başarılı kayıt listesi Ada-8 ve Ada-9 içeriyor; kaynak korunmuş.
- [ ] Eksik anahtar davranışı kontrol edilmiş, Ece silinmiş.
- [ ] Rapor sorted ve enumerate mantığıyla deterministik; set sırası dayatılmamış.
- [ ] Tuple/anahtar/kimlik/eşitlik ayrımları somut veri üzerinden gerekçeli; tek bir veri yapısı her şeye zorlanmamış.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md) · [Sıra](../../TASKS.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../06-modules/README.md)
<!-- learning-milestone:end -->
