# Milestone: Hem içe aktarılan hem çalıştırılan modülü izle

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Modül başlangıcı, main koruması, ad bağlama, yol ve bytecode cache ilişkisi.

## Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

## Tek görev

1. numbers_tool.py içinde listeden toplam döndüren işlev ve yalnız ana çalıştırmada iki sabit sayı için sonuç yazdıran koruma kur.

2. Yeni oturumdan iki import, işlev çağrısı ve doğrudan dosya çalıştırmasını karşılaştır.

3. Aynı adlı başka dosya betik klasöründe olsaydı arama seçimini, kaynak değişseydi yeni süreçte .pyc kontrolünü not et.

## Geçiş ölçütleri

- [ ] Importta ana rapor basılmıyor, doğrudan betikte basılıyor.
- [ ] İki import aynı modül nesnesine gidiyor; işlev açıkça çağrılabiliyor.
- [ ] İsim bağlama, modül arama ve bytecode cache üç ayrı olay olarak açıklanmış.
- [ ] .pyc çalışma algoritmasını hızlandırma garantisi sayılmamış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
