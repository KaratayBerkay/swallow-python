# Görev 11.8: Ondalık girdiyi nasıl oluşturduğunu karşılaştır

**Odak:** Decimal metin girdisi, float farkı, round, kalan/eşitlik ve precision.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:11.7](../11.7-tools-for-working-with-lists/README.md).

## Tek görev

1. Bölümdeki Decimal("0.70") * Decimal("1.05") hesabını float eşdeğeriyle birlikte iki basamağa yuvarla.

2. On tane Decimal("0.1") toplamını Decimal("1.0") ile, on float 0.1 değerinin açık toplamasını 1.0 ile karşılaştır.

3. Decimal("1.00") % Decimal(".10") işlemini dene. getcontext().prec değerini önce sakla, 6 yapıp Decimal(1)/Decimal(7) al, sonra eski değeri geri yükle.

## Geçiş ölçütleri

- [ ] Yuvarlanan sonuçlar Decimal 0.74 ile float 0.73; aynı yazılı ondalığın farklı temsili açıklanmış.
- [ ] Decimal toplamı eşit; açık float toplaması eşit değil.
- [ ] Decimal kalan 0.00; ondalık basamakların korunması gözlenmiş.
- [ ] Hassasiyet 6 ile 0.142857, sonra bağlam geri yüklenmiş.
- [ ] Decimal kullanımı her hesapta sonsuz hassasiyet garantisi sayılmamış; ek finans/mevzuat bilgisi gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
