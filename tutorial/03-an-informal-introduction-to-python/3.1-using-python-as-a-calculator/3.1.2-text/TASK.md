# Görev 3.1.2: Bir metin etiketini parçalarından kur

**Odak:** Tırnaklar, kaçışlar, raw ve çok satırlı metin, birleştirme, indeks, dilim, uzunluk ve değişmezlik.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:3.1.1](../3.1.1-numbers/README.md).

## Tek görev

1. word = "Swallow" ile bir etiket deneyi yap.

2. İlk ve son karakteri, ilk üç ve son dört karakteri ayrı alıp yeniden birleştir; ilk karakteri değiştirmeden "swallow" üreten yeni bir metin kur.

3. Etikete + ve * ile ayraç ekle.

4. Aynı notta tek/çift tırnakla apostrof içeren bir mesaj, \n içeren iki satırlı mesaj, aynı ters eğik çizgileri koruyan raw metin ve ilk satırı boş olmayan üç tırnaklı mesaj hazırla.

5. REPL gösterimiyle print sonucunu karşılaştır. word[70], word[70:] ve word[0] = "s" denemelerini ayrı girişlerde yap.

## Geçiş ölçütleri

- [ ] İndeksler S ve w; dilimler Swa ve llow, birleşimleri Swallow; yeni metin swallow, asıl word değişmemiş.
- [ ] Dilim son sınırının dışarıda kaldığı, eksik sınırların anlamı ve len(word) değerinin 7 olduğu açıklanmış.
- [ ] Taşan indeks hata verirken taşan dilim boş metin veriyor; metne öğe ataması TypeError veriyor.
- [ ] Yan yana iki literal ile değişken + literal ayrımı ve raw metnin tek ters eğik çizgiyle bitememesi açıklanmış.
- [ ] Tırnak, kaçış ve satır sonları hem REPL gösteriminde hem print çıktısında doğru ayırt edilmiş.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
