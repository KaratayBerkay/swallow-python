## 11.8. Decimal floating-point arithmetic

The `decimal` module offers a `Decimal` datatype for decimal floating-point arithmetic. Compared to the built-in `float` implementation of binary floating point, the class is especially helpful for

- financial applications and other uses which require exact decimal representation,

- control over precision,

- control over rounding to meet legal or regulatory requirements,

- tracking of significant decimal places, or

- applications where the user expects the results to match calculations done by hand.

For example, calculating a 5% tax on a 70 cent phone charge gives different results in decimal floating point and binary floating point. The difference becomes significant if the results are rounded to the nearest cent:

``` python
>>> from decimal import *
>>> round(Decimal('0.70') * Decimal('1.05'), 2)
Decimal('0.74')
>>> round(.70 * 1.05, 2)
0.73
```
> Code: [example_01.py](example_01.py)

The `Decimal` result keeps a trailing zero, automatically inferring four place significance from multiplicands with two place significance. Decimal reproduces mathematics as done by hand and avoids issues that can arise when binary floating point cannot exactly represent decimal quantities.

Exact representation enables the `Decimal` class to perform modulo calculations and equality tests that are unsuitable for binary floating point:

``` python
>>> Decimal('1.00') % Decimal('.10')
Decimal('0.00')
>>> 1.00 % 0.10
0.09999999999999995

>>> sum([Decimal('0.1')]*10) == Decimal('1.0')
True
>>> 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 == 1.0
False
```
> Code: [example_02.py](example_02.py)

The `decimal` module provides arithmetic with as much precision as needed:

``` python
>>> getcontext().prec = 36
>>> Decimal(1) / Decimal(7)
Decimal('0.142857142857142857142857142857142857')
```
> Code: [example_03.py](example_03.py)

<!-- learning-task:start -->
### Bölüm görevi

**Görev 11.8: Ondalık girdiyi nasıl oluşturduğunu karşılaştır**

**Odak:** Decimal metin girdisi, float farkı, round, kalan/eşitlik ve precision.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:11.7](../11.7-tools-for-working-with-lists/README.md).

#### Tek görev

1. Bölümdeki Decimal("0.70") * Decimal("1.05") hesabını float eşdeğeriyle birlikte iki basamağa yuvarla.

2. On tane Decimal("0.1") toplamını Decimal("1.0") ile, on float 0.1 değerinin açık toplamasını 1.0 ile karşılaştır.

3. Decimal("1.00") % Decimal(".10") işlemini dene. getcontext().prec değerini önce sakla, 6 yapıp Decimal(1)/Decimal(7) al, sonra eski değeri geri yükle.

#### Geçiş ölçütleri

- [ ] Yuvarlanan sonuçlar Decimal 0.74 ile float 0.73; aynı yazılı ondalığın farklı temsili açıklanmış.
- [ ] Decimal toplamı eşit; açık float toplaması eşit değil.
- [ ] Decimal kalan 0.00; ondalık basamakların korunması gözlenmiş.
- [ ] Hassasiyet 6 ile 0.142857, sonra bağlam geri yüklenmiş.
- [ ] Decimal kullanımı her hesapta sonsuz hassasiyet garantisi sayılmamış; ek finans/mevzuat bilgisi gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
