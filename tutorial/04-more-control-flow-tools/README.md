# 4. More Control Flow Tools

As well as the `while` statement just introduced, Python uses a few more that we will encounter in this chapter.

## Sections

- [4.1. `if` Statements](4.1-if-statements/README.md)
- [4.2. `for` Statements](4.2-for-statements/README.md)
- [4.3. The `range()` Function](4.3-the-range-function/README.md)
- [4.4. `break` and `continue` Statements](4.4-break-and-continue-statements/README.md)
- [4.5. `else` Clauses on Loops](4.5-else-clauses-on-loops/README.md)
- [4.6. `pass` Statements](4.6-pass-statements/README.md)
- [4.7. `match` Statements](4.7-match-statements/README.md)
- [4.8. Defining Functions](4.8-defining-functions/README.md)
- [4.9. More on Defining Functions](4.9-more-on-defining-functions/README.md)
- [4.10. Intermezzo: Coding Style](4.10-intermezzo-coding-style/README.md)

<!-- learning-milestone:start -->
## Klasör milestone görevi

**Milestone: Arama yapan küçük bir fonksiyon kur**

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Koşullar, döngüler, aralık, break/continue/else ve fonksiyon sözleşmesini birleştirme.

### Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

### Tek görev

1. find_even(values, /, *, start=0) fonksiyonunu yaz: start indeksinden itibaren range ile dolaş, negatif sayıları continue ile geç, ilk çift sayıyı bulunca break yap; döngünün else dalında None döndür.

2. Bulunan sayıyı döndür.

3. Değerleri [ -2, 3, 8, 10 ], [3, 5] ve [] ile; ayrıca start=3 ile dene. match, pass ve lambda için kendi bölüm görevlerindeki birer kararın bu algoritmada neden gerekli olmadığını veya nerede yer alabileceğini kısa notta belirt.

### Geçiş ölçütleri

- [ ] İlk sonuç 8, bulunamama/boş liste None; start=3 sonucu 10.
- [ ] Koşul, atlama, ilk eşleşmede durma ve loop else ayrı anlamlarıyla doğru.
- [ ] Çağrı kısıtları ve varsayılan yalnız önceki bilgilerle kurulmuş.
- [ ] En az bir çağrı sonucunu çalıştırmadan önce çıkarıp sonra doğrulamış; algoritmanın neden sonraki çiftte durmadığını açıklamış.
- [ ] Kod stili okunabilir; gereksiz class/import/exception altyapısı yok.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md) · [Sıra](../../TASKS.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../05-data-structures/5.1-more-on-lists/README.md)
<!-- learning-milestone:end -->
