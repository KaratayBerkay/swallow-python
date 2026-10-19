# Milestone: Yaklaşık değer için doğrulama ölçütünü seç

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Yeni sayılarda tam geri kurma, yaklaşık hesap ve gösterim için ayrı doğrulama ölçütü seçme.

## Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

## Tek görev

1. Bir ölçüm kaydı için exact = 0.125 ve measured = 0.2 + 0.4 oluştur. Matematiksel hedefler sırasıyla 1/8 ve 3/5 olsun. Önceki 0.1 hesabını yeniden yapmadan iki floatın as_integer_ratio sonuçlarını incele.

2. İlk kesirde numerator * 8 - denominator, ikincide numerator * 5 - 3 * denominator tamsayı hesaplarıyla hedefe tam eşitlik veya farkın yönünü belirle. İki kaydın .3f metin gösterimini al; ayrıca measured ile hedef 0.6 değerinin aynı .3f metnini vermesinin tam sayısal eşitlik kanıtı olup olmadığını açıkla.

3. measured değerini 0.6 ile == ve math.isclose kullanarak karşılaştır. Ayrıca Decimal("0.2") + Decimal("0.4") sonucunu Decimal("0.6") ile karşılaştır; seçtiğin sayı modelinin neyi değiştirdiğini açıkla.

4. İki floatı da hex/fromhex ile geri kur. Tam kesir hesabı, yaklaşık ölçüm karşılaştırması ve aynı floatın kayıpsız geri kurulması için neden farklı kanıtlar kullandığını tek kısa karar notunda birleştir.

## Geçiş ölçütleri

- [ ] exact kesri 1/8; ilk çapraz çarpım 0. measured kesri hedef 3/5'in biraz üzerinde; ikinci çapraz çarpım pozitif.
- [ ] .3f gösterimleri 0.125 ve 0.600; ikinci görünüm temsil farkını ortadan kaldırmıyor.
- [ ] measured == 0.6 yanlış, math.isclose sonucu doğru; Decimal metin girdileriyle toplam Decimal("0.6") değerine eşit.
- [ ] Her iki hex geri kurmasında tam eşitlik doğru; bunun bağımsız bir yaklaşık hesabı hedefle karşılaştırmaktan farkı açıklanmış.
- [ ] Sayı modeli, gösterim ve karşılaştırma yöntemi gerekçeyle seçilmiş; tek bir yöntemin bütün denetimlere uygun olduğu varsayılmamış.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md) · [Sıra](../../TASKS.md)
