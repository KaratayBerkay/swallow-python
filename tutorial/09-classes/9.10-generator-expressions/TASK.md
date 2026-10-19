# Görev 9.10: Liste üretmeden hesapla ve tüketimi izle

**Odak:** Generator expression, kapsamlı parantez, tek argüman istisnası ve tüketim.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:9.9](../9.9-generators/README.md).
- Ön bilgi: [t:5.1.3](../../05-data-structures/5.1-more-on-lists/5.1.3-list-comprehensions/README.md).

**Kaynak/ortam notu:** Yalnız yıldızlı generator expression Python 3.15 gerektirir; normal generator deneyi 3.11 ile yapılabilir.

## Tek görev

1. numbers = [1, 2, 3] için kareleri veren generator expression g oluştur. next(g), sum(g), list(g) sırasını izle.

2. Aynı toplamı yeni expressionı doğrudan sum içine vererek al; liste comprehension karşılığıyla üretim/tüketim farkını açıkla. [[1, 2], [], [3]] için bölümdeki yıldızlı generator biçiminin verdiği diziyi yazılı çıkar.

## Geçiş ölçütleri

- [ ] next 1, kalan toplam 13, son liste []; yeni expression toplamı 14.
- [ ] Tek argümanlı sum içine expression ek parantezsiz verilebiliyor.
- [ ] Liste biriktirme ile gerektiğinde öğe üretme farkı açıklanmış.
- [ ] Yıldızlı expression 1, 2, 3 sağlar; boş alt liste atlanır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
