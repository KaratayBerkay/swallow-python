# Milestone: Import sorununu doğru katmanda teşhis et

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Import sisteminin bütün işlenmiş katmanlarını tek inceleme ağacında kullanma.

## Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

## Tek görev

1. Bir geliştirici "aynı modülü değiştirip tekrar import ettim ama eski değeri gördüm; -m ile dosyadan çalıştırma da farklı" diyor.

2. Teşhis kaydında yerel ad bağlama, sys.modules, reload, meta path/path cache, bytecode geçerliliği, parent alt modül bağı, göreli import bağlamı ve `__main__.__spec__` katmanlarını ayır.

3. Üç kontrollü varyant için beklenen iz yaz: aynı oturumda tekrar import; yeni süreçte kaynak değişimi; -m ile ana giriş.

4. Hookları değiştirerek çözmek yerine eldeki bulgudan hangi katmanın sorumlu olduğunu gerekçelendir.

## Geçiş ölçütleri

- [ ] Aynı oturumun eski değerini önce modül cacheiyle açıklıyor; .pyc otomatik suçlanmıyor.
- [ ] Yeni süreçte kaynak/bytecode geçerliliği ayrı; finder cache modül nesnesi tutuyor sanılmamış.
- [ ] Reload kimliği, namespace/parent bağı ve göreli import tabanı tutarlı.
- [ ] -m ile dosya yolunun ana spec farkı doğru; import edilebilir nesneyle ana nesne ayrılmış.
- [ ] Güncel exec_module ile tarihsel load_module karıştırılmamış; bilgi eksikliği boş referans bölümlerinden tamamlanmış sayılmamış.
- [ ] Her öneri ilgili gözlemle destekli; gerçek import hook veya sistem ayarı değiştirilmemiş.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md) · [Sıra](../../TASKS.md)
