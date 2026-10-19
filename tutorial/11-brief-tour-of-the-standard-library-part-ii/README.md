# 11. Brief tour of the standard library --- part II

This second tour covers more advanced modules that support professional programming needs. These modules rarely occur in small scripts.

## Sections

- [11.1. Output formatting](11.1-output-formatting/README.md)
- [11.2. Templating](11.2-templating/README.md)
- [11.3. Working with binary data record layouts](11.3-working-with-binary-data-record-layouts/README.md)
- [11.4. Multi-threading](11.4-multi-threading/README.md)
- [11.5. Logging](11.5-logging/README.md)
- [11.6. Weak references](11.6-weak-references/README.md)
- [11.7. Tools for working with lists](11.7-tools-for-working-with-lists/README.md)
- [11.8. Decimal floating-point arithmetic](11.8-decimal-floating-point-arithmetic/README.md)

<!-- learning-milestone:start -->
## Klasör milestone görevi

**Milestone: Öncelikli yerel işlerin raporunu üret**

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Veri yapısı, Decimal, sunum şablonu ve logging seçimlerini birlikte gerekçelendirme.

### Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

### Tek görev

1. İşler için (öncelik, ad, ondalık ücret metni) kayıtları tut. heap ile en küçük öncelikli iki işi al, Decimal ile ücretleri topla, Template ile rapor mesajını kur; pprint veya textwrap ile sun. logging ile normal bilgi ve uyarı satırlarının varsayılan görünüm farkını göster.

2. Aynı tasarımda zayıf cache neyi yaşatmamalı ve arka plan thread kullanılsaydı join nereye konmalı sorularını küçük sahiplik/akış çiziminde yanıtla.

3. Thread veya weak cache uygulamasını tekrar yazmak gerekmiyor.

### Geçiş ölçütleri

- [ ] Heap seçimi doğru iki işi veriyor; iç listenin tümden sıralı olduğu varsayılmamış.
- [ ] Decimal metinden oluşuyor, toplam ve gösterim ayrı.
- [ ] Şablon alanları veriden geliyor, eksik alan davranışı belirtilmiş.
- [ ] Logging görünürlüğüyle yürütme ayrılmış.
- [ ] Zayıf referans son güçlü sahibi yaşatmaz; son rapor thread tamamlanmasına bağlıysa join önce gelir.
- [ ] Binary struct bölümündeki alan sırasının rapor verisine doğrudan uygulanamayacağı ve ayrıca bir kayıt sözleşmesi gerektireceği açıklanmış.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md) · [Sıra](../../TASKS.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../12-virtual-environments-and-packages/12.1-introduction/README.md)
<!-- learning-milestone:end -->
