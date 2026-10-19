# 15. Floating-Point Arithmetic: Issues and Limitations

Floating-point numbers are represented in computer hardware as base 2 (binary) fractions. For example, the **decimal** fraction `0.625` has value 6/10 + 2/100 + 5/1000, and in the same way the **binary** fraction `0.101` has value 1/2 + 0/4 + 1/8. These two fractions have identical values, the only real difference being that the first is written in base 10 fractional notation, and the second in base 2.

Unfortunately, most decimal fractions cannot be represented exactly as binary fractions. A consequence is that, in general, the decimal floating-point numbers you enter are only approximated by the binary floating-point numbers actually stored in the machine.

The problem is easier to understand at first in base 10. Consider the fraction 1/3. You can approximate that as a base 10 fraction, and each extra digit gets you closer:

``` python
>>> print(0.3)
0.3
>>> print(0.33)
0.33
>>> print(0.333)
0.333
>>> print(0.3333)
0.3333
>>> print(0.33333)
0.33333
```
> Code: [example_01.py](example_01.py)

and so on. No matter how many digits you're willing to write down, the result will never be exactly 1/3, but will be an increasingly better approximation of 1/3.

In the same way, no matter how many base 2 digits you're willing to use, the decimal value 0.1 cannot be represented exactly as a base 2 fraction. In base 2, 1/10 is the infinitely repeating fraction below, and the full decimal value of the binary approximation stored for `0.1` is the long number at the end:

``` python
>>> print("0.0001100110011001100110011001100110011001100110011...")
0.0001100110011001100110011001100110011001100110011...
>>> print(0.1)
0.1
>>> print("0.1000000000000000055511151231257827021181583404541015625")
0.1000000000000000055511151231257827021181583404541015625
```
> Code: [example_02.py](example_02.py)

Stop at any finite number of bits, and you get an approximation. On most machines today, floats are approximated using a binary fraction with the numerator using the first 53 bits starting with the most significant bit and with the denominator as a power of two. In the case of 1/10, the binary fraction is `3602879701896397 / 2 ** 55` which is close to but not exactly equal to the true value of 1/10.

Many users are not aware of the approximation because of the way values are displayed. Python only prints a decimal approximation to the true decimal value of the binary approximation stored by the machine. On most machines, the true decimal value of the binary approximation stored for 0.1 is the long number shown above.

That is more digits than most people find useful, so Python keeps the number of digits manageable by displaying a rounded value instead:

``` python
>>> 1 / 10
0.1
```
> Code: [example_03.py](example_03.py)

Just remember, even though the printed result looks like the exact value of 1/10, the actual stored value is the nearest representable binary fraction.

Interestingly, there are many different decimal numbers that share the same nearest approximate binary fraction. For example, the numbers `0.1` and `0.10000000000000001` and `0.1000000000000000055511151231257827021181583404541015625` are all approximated by `3602879701896397 / 2 ** 55`. Since all of these decimal values share the same approximation, any one of them could be displayed while still preserving the invariant `eval(repr(x)) == x`.

Historically, the Python prompt and built-in `repr()` function would choose the one with 17 significant digits, `0.10000000000000001`. Starting with Python 3.1, Python (on most systems) is now able to choose the shortest of these and simply display `0.1`.

Note that this is in the very nature of binary floating point: this is not a bug in Python, and it is not a bug in your code either. You'll see the same kind of thing in all languages that support your hardware's floating-point arithmetic (although some languages may not *display* the difference by default, or in all output modes).

For more pleasant output, you may wish to use string formatting to produce a limited number of significant digits:

``` python
>>> format(math.pi, '.12g')  # give 12 significant digits
'3.14159265359'

>>> format(math.pi, '.2f')   # give 2 digits after the point
'3.14'

>>> repr(math.pi)
'3.141592653589793'
```
> Code: [example_04.py](example_04.py)

It's important to realize that this is, in a real sense, an illusion: you're simply rounding the *display* of the true machine value.

One illusion may beget another. For example, since 0.1 is not exactly 1/10, summing three values of 0.1 may not yield exactly 0.3, either:

``` python
>>> 0.1 + 0.1 + 0.1 == 0.3
False
```
> Code: [example_05.py](example_05.py)

Also, since the 0.1 cannot get any closer to the exact value of 1/10 and 0.3 cannot get any closer to the exact value of 3/10, then pre-rounding with `round()` function cannot help:

``` python
>>> round(0.1, 1) + round(0.1, 1) + round(0.1, 1) == round(0.3, 1)
False
```
> Code: [example_06.py](example_06.py)

Though the numbers cannot be made closer to their intended exact values, the `math.isclose()` function can be useful for comparing inexact values:

``` python
>>> math.isclose(0.1 + 0.1 + 0.1, 0.3)
True
```
> Code: [example_07.py](example_07.py)

Alternatively, the `round()` function can be used to compare rough approximations:

``` python
>>> round(math.pi, ndigits=2) == round(22 / 7, ndigits=2)
True
```
> Code: [example_08.py](example_08.py)

Binary floating-point arithmetic holds many surprises like this. The problem with "0.1" is explained in precise detail below, in the "Representation Error" section. See [Examples of Floating Point Problems](https://jvns.ca/blog/2023/01/13/examples-of-floating-point-problems/) for a pleasant summary of how binary floating point works and the kinds of problems commonly encountered in practice. Also see [The Perils of Floating Point](http://www.indowsway.com/floatingpoint.htm) for a more complete account of other common surprises.

As that says near the end, "there are no easy answers." Still, don't be unduly wary of floating point! The errors in Python float operations are inherited from the floating-point hardware, and on most machines are on the order of no more than 1 part in 2\*\*53 per operation. That's more than adequate for most tasks, but you do need to keep in mind that it's not decimal arithmetic and that every float operation can suffer a new rounding error.

While pathological cases do exist, for most casual use of floating-point arithmetic you'll see the result you expect in the end if you simply round the display of your final results to the number of decimal digits you expect. `str()` usually suffices, and for finer control see the `str.format()` method's format specifiers in Format string syntax.

For use cases which require exact decimal representation, try using the `decimal` module which implements decimal arithmetic suitable for accounting applications and high-precision applications.

Another form of exact arithmetic is supported by the `fractions` module which implements arithmetic based on rational numbers (so the numbers like 1/3 can be represented exactly).

If you are a heavy user of floating-point operations you should take a look at the NumPy package and many other packages for mathematical and statistical operations supplied by the SciPy project. See \<[https://scipy.org](https://scipy.org)\>.

Python provides tools that may help on those rare occasions when you really *do* want to know the exact value of a float. The `float.as_integer_ratio()` method expresses the value of a float as a fraction:

``` python
>>> x = 3.14159
>>> x.as_integer_ratio()
(3537115888337719, 1125899906842624)
```
> Code: [x.py](x.py)

Since the ratio is exact, it can be used to losslessly recreate the original value:

``` python
>>> x == 3537115888337719 / 1125899906842624
True
```
> Code: [example_09.py](example_09.py)

The `float.hex()` method expresses a float in hexadecimal (base 16), again giving the exact value stored by your computer:

``` python
>>> x.hex()
'0x1.921f9f01b866ep+1'
```
> Code: [example_10.py](example_10.py)

This precise hexadecimal representation can be used to reconstruct the float value exactly:

``` python
>>> x == float.fromhex('0x1.921f9f01b866ep+1')
True
```
> Code: [example_11.py](example_11.py)

Since the representation is exact, it is useful for reliably porting values across different versions of Python (platform independence) and exchanging data with other languages that support the same format (such as Java and C99).

Another helpful tool is the `sum()` function which helps mitigate loss-of-precision during summation. It uses extended precision for intermediate rounding steps as values are added onto a running total. That can make a difference in overall accuracy so that the errors do not accumulate to the point where they affect the final total:

``` python
>>> 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 == 1.0
False
>>> sum([0.1] * 10) == 1.0
True
```
> Code: [example_12.py](example_12.py)

The `math.fsum()` goes further and tracks all of the "lost digits" as values are added onto a running total so that the result has only a single rounding. This is slower than `sum()` but will be more accurate in uncommon cases where large magnitude inputs mostly cancel each other out leaving a final sum near zero:

``` python
>>> arr = [-0.10430216751806065, -266310978.67179024, 143401161448607.16,
...        -143401161400469.7, 266262841.31058735, -0.003244936839808227]
>>> float(sum(map(Fraction, arr)))   # Exact summation with single rounding
8.042173697819788e-13
>>> math.fsum(arr)                   # Single rounding
8.042173697819788e-13
>>> sum(arr)                         # Multiple roundings in extended precision
8.042178034628478e-13
>>> total = 0.0
>>> for x in arr:
...     total += x                   # Multiple roundings in standard precision
...
>>> total                            # Straight addition has no correct digits!
-0.0051575902860057365
```
> Code: [arr.py](arr.py)


<!-- learning-task:start -->
## Bölüm görevi

**Görev 15: Gösterimi gerçek sayı değeriyle karıştırma**

**Odak:** Binary yaklaşım, gösterim yuvarlaması, isclose, tam geri kurma ve toplama hassasiyeti.

### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:11.8](../11-brief-tour-of-the-standard-library-part-ii/11.8-decimal-floating-point-arithmetic/README.md).
- Ön bilgi: [t:9.10](../09-classes/9.10-generator-expressions/README.md).

**Kaynak/ortam notu:** Kaynak yeni Python sürümündeki sum iyileştirmelerini anlatıyor. Python 3.11 üzerinde sum([0.1] * 10) == 1.0 yanlış çıkabilir; sonucu sürümüyle değerlendir.

### Tek görev

1. Tek bir sayı inceleme notu hazırla. 0.1 + 0.1 + 0.1 ile 0.3 için ==, math.isclose ve format(..., ".2f") sonuçlarını karşılaştır; round ile her girdiyi önceden yuvarlamanın neden aynı sorunu çözmediğini dene. x=0.1 için as_integer_ratio ve hex/fromhex ile değeri geri kur.

2. Ardından on adet 0.1 için açık toplama, sum ve math.fsum sonuçlarını mevcut Python sürümüyle birlikte kaydet.

3. README içindeki büyük değerlerin birbirini götürdüğü arr örneğini, gerekli math/Fraction importlarını ekleyerek aynı ölçütle incele.

### Geçiş ölçütleri

- [ ] Doğrudan eşitlik yanlış, isclose doğru; aynı görünen iki biçimlenmiş metnin altında farklı değerler bulunabiliyor.
- [ ] Ön yuvarlama temsil sorununu ortadan kaldırmıyor.
- [ ] Kesirden ve hex metninden geri kurulan float, ilk float ile tam eşit; gerçek 1/10 ile eşit olduğu iddia edilmemiş.
- [ ] sum davranışının 3.11 ve 3.12+ arasında farklılaşabileceği belirtilmiş; math.fsum ile açık toplama ayrılmış.
- [ ] arr için hangi yöntemin kayıp basamakları daha iyi koruduğu gözlemle açıklanmış; sürüme bağlı son basamaklar ezber ölçütü yapılmamış.
- [ ] Decimal metin girdisi ile Fraction tam kesir amaçları, gösterim biçimlemeyle karıştırılmamış.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md) · [Sıra](../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](15.1-representation-error/README.md)
<!-- learning-task:end -->
## Sections

- [15.1. Representation Error](15.1-representation-error/README.md)

<!-- learning-milestone:start -->
## Klasör milestone görevi

**Milestone: Yaklaşık değer için doğrulama ölçütünü seç**

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Yeni sayılarda tam geri kurma, yaklaşık hesap ve gösterim için ayrı doğrulama ölçütü seçme.

### Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

### Tek görev

1. Bir ölçüm kaydı için exact = 0.125 ve measured = 0.2 + 0.4 oluştur. Matematiksel hedefler sırasıyla 1/8 ve 3/5 olsun. Önceki 0.1 hesabını yeniden yapmadan iki floatın as_integer_ratio sonuçlarını incele.

2. İlk kesirde numerator * 8 - denominator, ikincide numerator * 5 - 3 * denominator tamsayı hesaplarıyla hedefe tam eşitlik veya farkın yönünü belirle. İki kaydın .3f metin gösterimini al; ayrıca measured ile hedef 0.6 değerinin aynı .3f metnini vermesinin tam sayısal eşitlik kanıtı olup olmadığını açıkla.

3. measured değerini 0.6 ile == ve math.isclose kullanarak karşılaştır. Ayrıca Decimal("0.2") + Decimal("0.4") sonucunu Decimal("0.6") ile karşılaştır; seçtiğin sayı modelinin neyi değiştirdiğini açıkla.

4. İki floatı da hex/fromhex ile geri kur. Tam kesir hesabı, yaklaşık ölçüm karşılaştırması ve aynı floatın kayıpsız geri kurulması için neden farklı kanıtlar kullandığını tek kısa karar notunda birleştir.

### Geçiş ölçütleri

- [ ] exact kesri 1/8; ilk çapraz çarpım 0. measured kesri hedef 3/5'in biraz üzerinde; ikinci çapraz çarpım pozitif.
- [ ] .3f gösterimleri 0.125 ve 0.600; ikinci görünüm temsil farkını ortadan kaldırmıyor.
- [ ] measured == 0.6 yanlış, math.isclose sonucu doğru; Decimal metin girdileriyle toplam Decimal("0.6") değerine eşit.
- [ ] Her iki hex geri kurmasında tam eşitlik doğru; bunun bağımsız bir yaklaşık hesabı hedefle karşılaştırmaktan farkı açıklanmış.
- [ ] Sayı modeli, gösterim ve karşılaştırma yöntemi gerekçeyle seçilmiş; tek bir yöntemin bütün denetimlere uygun olduğu varsayılmamış.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md) · [Sıra](../../TASKS.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../16-appendix/16.1-interactive-mode/README.md)
<!-- learning-milestone:end -->
