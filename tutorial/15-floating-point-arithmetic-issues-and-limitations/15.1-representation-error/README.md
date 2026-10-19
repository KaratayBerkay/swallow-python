## 15.1. Representation Error

This section explains the "0.1" example in detail, and shows how you can perform an exact analysis of cases like this yourself. Basic familiarity with binary floating-point representation is assumed.

*Representation error* refers to the fact that some (most, actually) decimal fractions cannot be represented exactly as binary (base 2) fractions. This is the chief reason why Python (or Perl, C, C++, Java, Fortran, and many others) often won't display the exact decimal number you expect.

Why is that? 1/10 is not exactly representable as a binary fraction. Since at least 2000, almost all machines use IEEE 754 binary floating-point arithmetic, and almost all platforms map Python floats to IEEE 754 binary64 "double precision" values. IEEE 754 binary64 values contain 53 bits of precision, so on input the computer strives to convert 0.1 to the closest fraction it can of the form *J*/2\*\**N* where *J* is an integer containing exactly 53 bits. Rewriting

``` python
1 / 10 ~= J / (2**N)
```
> Code: [representation_error.py:3](representation_error.py#L3)

as

``` python
J ~= 2**N / 10
```
> Code: [representation_error.py:5](representation_error.py#L5)

and recalling that *J* has exactly 53 bits (is `>= 2**52` but `< 2**53`), the best value for *N* is 56:

``` python
>>> 2**52 <=  2**56 // 10  < 2**53
True
```
> Code: [representation_error.py:6](representation_error.py#L6)

That is, 56 is the only value for *N* that leaves *J* with exactly 53 bits. The best possible value for *J* is then that quotient rounded:

``` python
>>> q, r = divmod(2**56, 10)
>>> r
6
```
> Code: [representation_error.py:9-10](representation_error.py#L9-L10)

Since the remainder is more than half of 10, the best approximation is obtained by rounding up:

``` python
>>> q+1
7205759403792794
```
> Code: [representation_error.py:13-14](representation_error.py#L13-L14)

Therefore the best possible approximation to 1/10 in IEEE 754 double precision is:

``` python
7205759403792794 / 2 ** 56
```
> Code: [representation_error.py:17](representation_error.py#L17)

Dividing both the numerator and denominator by two reduces the fraction to:

``` python
3602879701896397 / 2 ** 55
```
> Code: [representation_error.py:22](representation_error.py#L22)

Note that since we rounded up, this is actually a little bit larger than 1/10; if we had not rounded up, the quotient would have been a little bit smaller than 1/10. But in no case can it be *exactly* 1/10!

So the computer never "sees" 1/10: what it sees is the exact fraction given above, the best IEEE 754 double approximation it can get:

``` python
>>> 0.1 * 2 ** 55
3602879701896397.0
```
> Code: [representation_error.py:25](representation_error.py#L25)

If we multiply that fraction by 10\*\*55, we can see the value out to 55 decimal digits:

``` python
>>> 3602879701896397 * 10 ** 55 // 2 ** 55
1000000000000000055511151231257827021181583404541015625
```
> Code: [representation_error.py:28](representation_error.py#L28)

meaning that the exact number stored in the computer is equal to the decimal value 0.1000000000000000055511151231257827021181583404541015625. Instead of displaying the full decimal value, many languages (including older versions of Python), round the result to 17 significant digits:

``` python
>>> format(0.1, '.17f')
'0.10000000000000001'
```
> Code: [representation_error.py:31](representation_error.py#L31)

The `fractions` and `decimal` modules make these calculations easy:

``` python
>>> from decimal import Decimal
>>> from fractions import Fraction

>>> Fraction.from_float(0.1)
Fraction(3602879701896397, 36028797018963968)

>>> (0.1).as_integer_ratio()
(3602879701896397, 36028797018963968)

>>> Decimal.from_float(0.1)
Decimal('0.1000000000000000055511151231257827021181583404541015625')

>>> format(Decimal.from_float(0.1), '.17')
'0.10000000000000001'
```
> Code: [decimal_example.py](decimal_example.py)

<!-- learning-task:start -->
### Bölüm görevi

**Görev 15.1: Saklanan yaklaşık kesrin neden yukarıda kaldığını kanıtla**

**Odak:** 53 bitlik J, 2*`*N` paydası, bölüm/kalan ile en yakın temsil ve tam ondalık karşılık.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:15](../README.md).

#### Tek görev

1. Bölümdeki 0.1 hesabını bir kanıt zinciri olarak yeniden kur: N=56 için J sınırını kontrol et, divmod(2**56, 10) ile q/r bul, neden q+1 seçildiğini açıkla.

2. Elde edilen kesri ikiye sadeleştir; numerator * 10 - denominator tamsayı hesabıyla temsilin gerçek 1/10 değerinden hangi yönde farklı olduğunu göster.

3. Fraction.from_float, as_integer_ratio ve Decimal.from_float sonuçlarını bu hesapla eşleştir.

#### Geçiş ölçütleri

- [ ] 2**52 <= q < 2**53; kalan 6 olduğu için yukarı yuvarlama gerekçeli.
- [ ] İlk pay 7205759403792794; sadeleşmiş pay 3602879701896397, payda 2**55.
- [ ] Sadeleşmiş pay için numerator * 10 - denominator pozitif ve 2; değer gerçek 1/10 üzerinde.
- [ ] Fraction ile integer ratio aynı kesin float kesrini, Decimal.from_float gerçek saklanan ondalık değeri veriyor.
- [ ] repr çıktısının 0.1 olması saklanan değerin tam 1/10 olduğunu kanıtlamıyor; ikili sayı kuramından ek türetme gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
