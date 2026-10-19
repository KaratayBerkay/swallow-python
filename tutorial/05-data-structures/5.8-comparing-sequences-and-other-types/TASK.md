# Görev 5.8: Sıralamanın ilk belirleyici öğesini bul

**Odak:** Sözlük sırası anlamındaki lexicographic karşılaştırma, önek, iç içe diziler ve tür uyumu.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:5.7](../5.7-more-on-conditions/README.md).

## Tek görev

1. Şu karşılaştırmaların her biri için yalnız sonucu değil, sonucu belirleyen ilk öğeyi yaz: [2, 9] < [3, 0]; [2, 9] < [2, 9, -1]; (1, ("ab", "c")) < (1, ("ac", "a")); (1, 2) == (1.0, 2.0); "B" < "a"; [1, "x"] < [1, 2].

2. Sonra ifadeleri ayrı girişlerde doğrula.

## Geçiş ölçütleri

- [ ] İlk beş sonuç doğru; sonuncu str/int sıralaması nedeniyle TypeError.
- [ ] İlk fark bulunan yerde sonraki öğelerin karşılaştırılmadığı gösterilmiş.
- [ ] Önek durumunda kısa dizi küçük; iç içe karşılaştırma yine aynı kuralla.
- [ ] Metin sırası Unicode kod noktasıyla açıklanmış, alfabetik/yerel sıralama sanılmamış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
