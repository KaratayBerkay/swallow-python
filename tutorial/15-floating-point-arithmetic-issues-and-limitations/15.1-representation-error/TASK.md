# Görev 15.1: Saklanan yaklaşık kesrin neden yukarıda kaldığını kanıtla

**Odak:** 53 bitlik J, 2*`*N` paydası, bölüm/kalan ile en yakın temsil ve tam ondalık karşılık.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:15](../README.md).

## Tek görev

1. Bölümdeki 0.1 hesabını bir kanıt zinciri olarak yeniden kur: N=56 için J sınırını kontrol et, divmod(2**56, 10) ile q/r bul, neden q+1 seçildiğini açıkla.

2. Elde edilen kesri ikiye sadeleştir; numerator * 10 - denominator tamsayı hesabıyla temsilin gerçek 1/10 değerinden hangi yönde farklı olduğunu göster.

3. Fraction.from_float, as_integer_ratio ve Decimal.from_float sonuçlarını bu hesapla eşleştir.

## Geçiş ölçütleri

- [ ] 2**52 <= q < 2**53; kalan 6 olduğu için yukarı yuvarlama gerekçeli.
- [ ] İlk pay 7205759403792794; sadeleşmiş pay 3602879701896397, payda 2**55.
- [ ] Sadeleşmiş pay için numerator * 10 - denominator pozitif ve 2; değer gerçek 1/10 üzerinde.
- [ ] Fraction ile integer ratio aynı kesin float kesrini, Decimal.from_float gerçek saklanan ondalık değeri veriyor.
- [ ] repr çıktısının 0.1 olması saklanan değerin tam 1/10 olduğunu kanıtlamıyor; ikili sayı kuramından ek türetme gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
