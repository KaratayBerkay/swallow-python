# Görev 5.1.4: Satırlarla sütunların yerini değiştir

**Odak:** İç içe comprehension, dış bağlam, matris boyutu ve zip(`*matrix`) karşılığı.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:5.1.3](../5.1.3-list-comprehensions/README.md).
- Ön bilgi: [t:4.9.5](../../../04-more-control-flow-tools/4.9-more-on-defining-functions/4.9.5-unpacking-argument-lists/README.md).

## Tek görev

1. matrix = [[1, 2, 3], [4, 5, 6]] için satırları sütunlara dönüştüren nested comprehension yaz.

2. Aynı dönüşümü açık döngülerle ve bölümdeki zip(`*matrix`) yaklaşımıyla üret.

3. Her sürümün hangi sırada hangi öğeye eriştiğini bir sütun için izle.

## Geçiş ölçütleri

- [ ] Sonuç [[1, 4], [2, 5], [3, 6]]; 2x3 girdi 3x2 oluyor.
- [ ] Dış indeks sabitken iç comprehension bütün satırları dolaşıyor.
- [ ] zip sürümü [(1, 4), (2, 5), (3, 6)] veriyor; iç liste/tuple farkı fark edilmiş.
- [ ] Boş matris için boş sonuç verecek boyut seçimi açıklanmış; sabit 4 kopyalanmamış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
