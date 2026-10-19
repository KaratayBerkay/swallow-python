# Görev 5.1.3: Dönüştürme ve filtreyi tek ifadede kur

**Odak:** Comprehension ifade/for/if sırası, yeni liste, değişken kapsamı ve birden çok for.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:5.1](../README.md).
- Ön bilgi: [t:4.2](../../../04-more-control-flow-tools/4.2-for-statements/README.md).

## Tek görev

1. values = [-3, 0, 2, 5] için negatif olmayanların (sayı, karesi) çiftlerini hem append kullanan döngüyle hem comprehension ile üret.

2. İki sürümün sonucunu karşılaştır.

3. Sonra [[1, 2], [], [3]] listesini iki for ile düzleştir; comprehension ifadendeki for sırasının iç içe döngüyle eşleşmesini göster.

4. Çalıştırmadan önce x = "outside" tanımlayıp comprehension içinde x kullanmanın dış değere etkisini dene.

## Geçiş ölçütleri

- [ ] Çiftler [(0, 0), (2, 4), (5, 25)]; tuple ifadesi parantezli.
- [ ] Düzleştirme [1, 2, 3]; dış for grup, iç for öğe üzerinde.
- [ ] Kaynak listeler değişmemiş; comprehension yeni liste üretiyor.
- [ ] Comprehension x değerini dışarı sızdırmıyor; normal döngü değişkeninin davranışıyla farkı açıklanmış.
- [ ] Filtre koşulunun hangi öğeleri, ifade kısmının hangi dönüşümü belirlediği açıklanmış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
