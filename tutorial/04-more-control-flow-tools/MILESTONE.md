# Milestone: Arama yapan küçük bir fonksiyon kur

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Koşullar, döngüler, aralık, break/continue/else ve fonksiyon sözleşmesini birleştirme.

## Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

## Tek görev

1. find_even(values, /, *, start=0) fonksiyonunu yaz: start indeksinden itibaren range ile dolaş, negatif sayıları continue ile geç, ilk çift sayıyı bulunca break yap; döngünün else dalında None döndür.

2. Bulunan sayıyı döndür.

3. Değerleri [ -2, 3, 8, 10 ], [3, 5] ve [] ile; ayrıca start=3 ile dene. match, pass ve lambda için kendi bölüm görevlerindeki birer kararın bu algoritmada neden gerekli olmadığını veya nerede yer alabileceğini kısa notta belirt.

## Geçiş ölçütleri

- [ ] İlk sonuç 8, bulunamama/boş liste None; start=3 sonucu 10.
- [ ] Koşul, atlama, ilk eşleşmede durma ve loop else ayrı anlamlarıyla doğru.
- [ ] Çağrı kısıtları ve varsayılan yalnız önceki bilgilerle kurulmuş.
- [ ] En az bir çağrı sonucunu çalıştırmadan önce çıkarıp sonra doğrulamış; algoritmanın neden sonraki çiftte durmadığını açıklamış.
- [ ] Kod stili okunabilir; gereksiz class/import/exception altyapısı yok.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md) · [Sıra](../../TASKS.md)
