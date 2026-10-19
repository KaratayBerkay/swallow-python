### 3.1.1. Numbers

The interpreter acts as a simple calculator: you can type an expression into it and it will write the value. Expression syntax is straightforward: the operators `+`, `-`, `*` and `/` can be used to perform arithmetic; parentheses (`()`) can be used for grouping. For example:

``` python
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5  # division always returns a floating-point number
1.6
```
> Code: [example_01.py](example_01.py)

The integer numbers (e.g. `2`, `4`, `20`) have type `int`, the ones with a fractional part (e.g. `5.0`, `1.6`) have type `float`. We will see more about numeric types later in the tutorial.

Division (`/`) always returns a float. To do floor division and get an integer result you can use the `//` operator; to calculate the remainder you can use `%`:

``` python
>>> 17 / 3  # classic division returns a float
5.666666666666667
>>>
>>> 17 // 3  # floor division discards the fractional part
5
>>> 17 % 3  # the % operator returns the remainder of the division
2
>>> 5 * 3 + 2  # floored quotient * divisor + remainder
17
```
> Code: [example_02.py](example_02.py)

With Python, it is possible to use the `**` operator to calculate powers (Since `**` has higher precedence than `-`, `-3**2` will be interpreted as `-(3**2)` and thus result in `-9`. To avoid this and get `9`, you can use `(-3)**2`.) :

``` python
>>> 5 ** 2  # 5 squared
25
>>> 2 ** 7  # 2 to the power of 7
128
```
> Code: [example_03.py](example_03.py)

The equal sign (`=`) is used to assign a value to a variable. Afterwards, no result is displayed before the next interactive prompt:

``` python
>>> width = 20
>>> height = 5 * 9
>>> width * height
900
```
> Code: [width.py](width.py)

If a variable is not "defined" (assigned a value), trying to use it will give you an error:

``` python
>>> n  # try to access an undefined variable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
```
> Code: [example_04.py](example_04.py)

There is full support for floating point; operators with mixed type operands convert the integer operand to floating point:

``` python
>>> 4 * 3.75 - 1
14.0
```
> Code: [example_05.py](example_05.py)

In interactive mode, the last printed expression is assigned to the variable `_`. This means that when you are using Python as a desk calculator, it is somewhat easier to continue calculations, for example:

``` python
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
```
> Code: [tax.py](tax.py)

This variable should be treated as read-only by the user. Don't explicitly assign a value to it --- you would create an independent local variable with the same name masking the built-in variable with its magic behavior.

In addition to `int` and `float`, Python supports other types of numbers, such as `Decimal` and `Fraction`. Python also has built-in support for complex numbers, and uses the `j` or `J` suffix to indicate the imaginary part (e.g. `3+5j`).

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 3.1.1: Bir siparişin hesabını yorumlayıcıda çıkar**

**Odak:** Aritmetik, işlem önceliği, int/float, atama, bölüm-kalan, üs ve REPL içindeki _.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:3](../../README.md).
- Ön bilgi: [t:2.1](../../../02-using-the-python-interpreter/2.1-invoking-the-interpreter/README.md).

##### Tek görev

1. Yeni bir REPL oturumunda 29 ürünü 4 kişilik paketlere ayıran hesabı yap: gerçek bölüm, tam paket sayısı, kalan ve geri birleştirilen toplam.

2. Sonra fiyatı 80.0 ve vergi oranı 0.125 olan tek ürünün vergisini hesapla; bir sonraki ifadede _ ile vergili toplamı bul ve iki basamağa yuvarla.

3. Son olarak -4**2 ile (-4)**2 ve 30 - 6*3 ile (30 - 6)*3 sonuçlarını karşılaştır.

4. Tanımlanmamış bir adı ayrı bir girişte dene.

##### Geçiş ölçütleri

- [ ] Bölüm 7.25, tam paket 7, kalan 1, geri birleştirme 29.
- [ ] Atama satırlarının REPL içinde kendiliğinden çıktı vermediği ve / sonucunun float olduğu açıklanmış.
- [ ] Vergi 10.0, toplam 90.0; _ önceki gösterilen sonucu kullanıyor ve ona doğrudan atama yapılmamış.
- [ ] Üs sonuçları -16 ve 16; parantezin önceliği değiştirmesi açıklanmış.
- [ ] Tanımsız ad NameError veriyor; Decimal ve Fraction yalnızca adı geçen türler olarak kalıyor.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../3.1.2-text/README.md)
<!-- learning-task:end -->
