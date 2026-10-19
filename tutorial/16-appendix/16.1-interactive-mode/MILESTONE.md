# Milestone: Yorumlayıcı başlangıcını değiştirmeden teşhis et

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** REPL sürümü, betik başlığı, hata akışı ve başlangıç özelleştirme kapsamı.

## Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

## Tek görev

1. Bir betik terminalde farklı, REPLde farklı davranıyor senaryosu için inceleme kaydı hazırla.

2. Kod hatasını, stdout/stderr ayrımını, shebang/PATH/izin durumunu ve PYTHONSTARTUP ile usercustomize/sitecustomize etkilerini ayrı kanıt kaynaklarına ayır.

3. Bir örnek olarak marker değişkeninin yalnız etkileşimli startup dosyasında tanımlı olduğu durumda betikten erişimi açıklayıp yerel minimal taslağı yaz.

4. Kullanıcı başlangıç dosyalarını değiştirmek gerekmiyor.

## Geçiş ölçütleri

- [ ] REPL destek sınırı sürümle ilişkilendirilmiş.
- [ ] Betik hatasıyla giriş arayüzü ve çalıştırma izni sorunları karıştırılmamış.
- [ ] Startup marker normal betiğe otomatik taşınmıyor.
- [ ] Customization sırası ve -s kullanıcı sınırı doğru.
- [ ] Önerilen inceleme gerçek dosya/başlangıç düzenini değiştirmeden yapılabilir.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
