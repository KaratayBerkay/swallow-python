# 8. Errors and Exceptions

Until now error messages haven't been more than mentioned, but if you have tried out the examples you have probably seen some. There are (at least) two distinguishable kinds of errors: *syntax errors* and *exceptions*.

## Sections

- [8.1. Syntax Errors](8.1-syntax-errors/README.md)
- [8.2. Exceptions](8.2-exceptions/README.md)
- [8.3. Handling Exceptions](8.3-handling-exceptions/README.md)
- [8.4. Raising Exceptions](8.4-raising-exceptions/README.md)
- [8.5. Exception Chaining](8.5-exception-chaining/README.md)
- [8.6. User-defined Exceptions](8.6-user-defined-exceptions/README.md)
- [8.7. Defining Clean-up Actions](8.7-defining-clean-up-actions/README.md)
- [8.8. Predefined Clean-up Actions](8.8-predefined-clean-up-actions/README.md)
- [8.9. Raising and Handling Multiple Unrelated Exceptions](8.9-raising-and-handling-multiple-unrelated-exceptions/README.md)
- [8.10. Enriching Exceptions with Notes](8.10-enriching-exceptions-with-notes/README.md)

<!-- learning-milestone:start -->
## Klasör milestone görevi

**Milestone: Kötü kayıtları kaybetmeden içe al**

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Hata yakalama/yükseltme, not, grup ve kaynak temizliğini birlikte kullanma.

### Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

### Tek görev

1. Bir yerel dosyaya "7\nbad\n0\n-2\n" yaz. with ile satırları oku; her satırı int yap, negatif için ValueError yükselt.

2. Geçerli sayıları topla; dönüşüm veya negatif hatasına satır numarası notu ekleyip listeye al.

3. Okuma bitince hatalar varsa ExceptionGroup ile yükselt.

4. Çağıranda except* ValueError ile ilgili grubu işle ve finally içinde son durum mesajı göster.

5. Dosya açılmaması gibi ilgisiz hataların aynı handler tarafından yutulmadığını ayrı senaryoda göster.

### Geçiş ölçütleri

- [ ] Geçerli değerler 7 ve 0; bad ve -2 için iki ayrı hata var.
- [ ] Hatalar kendi satır bağlamını taşıyor; ilk hatada bütün okuma durmuyor.
- [ ] Dosya hatadan önce veya sonra da doğru kapanıyor.
- [ ] except* yalnız hedef alt hataları işliyor; finally çalışması başarıyla karıştırılmamış.
- [ ] Özel alan hatası sınıfının hangi tabana oturacağı tasarım notunda açıklanmış; sınıf yazımı zorunlu değil.
- [ ] Tamamlanan, hatalı ve yayılan durumlar ayrı kanıtlarla gösterilmiş.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md) · [Sıra](../../TASKS.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../09-classes/README.md)
<!-- learning-milestone:end -->
