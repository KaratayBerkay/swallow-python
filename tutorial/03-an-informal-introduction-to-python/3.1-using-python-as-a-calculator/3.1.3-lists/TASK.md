# Görev 3.1.3: Ortak liste ile kopyayı ayır

**Odak:** Liste kurma, indeks/dilim, birleştirme, yerinde değişiklik, append, alias, dilim kopyası ve iç içe liste.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:3.1.2](../3.1.2-text/README.md).

## Tek görev

1. items = [2, 4, 7] ile başla. alias = items ve copied = items[:] oluştur. alias üzerinden son sayıyı 6 yapıp 8 ekle; copied üzerinden ilk sayıyı 0 yap.

2. Her adımda üç ismin gösterdiği içeriği kaydet.

3. Ardından items[1:3] dilimini [9] ile değiştir, ilk/son öğeyi ve uzunluğu kontrol et. [items, copied] içinden copied listesinin ikinci öğesini indeksle al.

4. Son olarak copied[:] = [] ile boşalt ve items + [10] sonucunu karşılaştır.

## Geçiş ölçütleri

- [ ] İlk değişikliklerden sonra items ve alias [2, 4, 6, 8], copied [0, 4, 7].
- [ ] Dilim atamasından sonra items ve alias [2, 9, 8], uzunluk 3; nested erişim 4.
- [ ] copied boşalınca items korunuyor; + yeni bir liste üretirken append mevcut listeyi değiştiriyor.
- [ ] Atamanın kopya üretmediği, [:] işleminin yeni dış liste ürettiği kendi sözcüklerinle açıklanmış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
