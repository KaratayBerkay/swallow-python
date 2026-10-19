# Milestone: Katılımcı kayıtlarını veri yapılarına dönüştür

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Liste/tuple/set/dict, dolaşma, koşul ve sıralama seçimini gerçek veriyle kullanma.

## Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

## Tek görev

1. records = [("Ada", 8), ("Ece", 5), ("Ada", 9), ("Can", 5)] verisinden son görülen puanı tutan bir sözlük, tekrarsız ad kümesi ve puanı en az 8 olan kayıtların yeni listesini üret.

2. Sözlükte eksik "Deniz" için get kullan; Ece kaydını del ile kaldır.

3. Son raporu ad sırasıyla, sıra numarasıyla yazdır.

4. Kaynak kayıtlardaki Ada tekrarının neden listede kalıp sözlükte tek değer olduğunu açıkla.

## Geçiş ölçütleri

- [ ] Sözlük başlangıçta Ada:9, Ece:5, Can:5; set üç ad içeriyor.
- [ ] Başarılı kayıt listesi Ada-8 ve Ada-9 içeriyor; kaynak korunmuş.
- [ ] Eksik anahtar davranışı kontrol edilmiş, Ece silinmiş.
- [ ] Rapor sorted ve enumerate mantığıyla deterministik; set sırası dayatılmamış.
- [ ] Tuple/anahtar/kimlik/eşitlik ayrımları somut veri üzerinden gerekçeli; tek bir veri yapısı her şeye zorlanmamış.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md) · [Sıra](../../TASKS.md)
