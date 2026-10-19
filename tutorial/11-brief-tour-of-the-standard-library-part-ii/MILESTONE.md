# Milestone: Öncelikli yerel işlerin raporunu üret

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Veri yapısı, Decimal, sunum şablonu ve logging seçimlerini birlikte gerekçelendirme.

## Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

## Tek görev

1. İşler için (öncelik, ad, ondalık ücret metni) kayıtları tut. heap ile en küçük öncelikli iki işi al, Decimal ile ücretleri topla, Template ile rapor mesajını kur; pprint veya textwrap ile sun. logging ile normal bilgi ve uyarı satırlarının varsayılan görünüm farkını göster.

2. Aynı tasarımda zayıf cache neyi yaşatmamalı ve arka plan thread kullanılsaydı join nereye konmalı sorularını küçük sahiplik/akış çiziminde yanıtla.

3. Thread veya weak cache uygulamasını tekrar yazmak gerekmiyor.

## Geçiş ölçütleri

- [ ] Heap seçimi doğru iki işi veriyor; iç listenin tümden sıralı olduğu varsayılmamış.
- [ ] Decimal metinden oluşuyor, toplam ve gösterim ayrı.
- [ ] Şablon alanları veriden geliyor, eksik alan davranışı belirtilmiş.
- [ ] Logging görünürlüğüyle yürütme ayrılmış.
- [ ] Zayıf referans son güçlü sahibi yaşatmaz; son rapor thread tamamlanmasına bağlıysa join önce gelir.
- [ ] Binary struct bölümündeki alan sırasının rapor verisine doğrudan uygulanamayacağı ve ayrıca bir kayıt sözleşmesi gerektireceği açıklanmış.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md) · [Sıra](../../TASKS.md)
