## 3.2. First Steps Towards Programming

Of course, we can use Python for more complicated tasks than adding two and two together. For instance, we can write an initial sub-sequence of the [Fibonacci series](https://en.wikipedia.org/wiki/Fibonacci_sequence) as follows:

``` python
>>> # Fibonacci series:
>>> # the sum of two elements defines the next
>>> a, b = 0, 1
>>> while a < 10:
...     print(a)
...     a, b = b, a+b
...
0
1
1
2
3
5
8
```
> Code: [example_01.py](example_01.py)

This example introduces several new features.

- The first line contains a *multiple assignment*: the variables `a` and `b` simultaneously get the new values 0 and 1. On the last line this is used again, demonstrating that the expressions on the right-hand side are all evaluated first before any of the assignments take place. The right-hand side expressions are evaluated from the left to the right.

- The `while` loop executes as long as the condition (here: `a < 10`) remains true. In Python, like in C, any non-zero integer value is true; zero is false. The condition may also be a string or list value, in fact any sequence; anything with a non-zero length is true, empty sequences are false. The test used in the example is a simple comparison. The standard comparison operators are written the same as in C: `<` (less than), `>` (greater than), `==` (equal to), `<=` (less than or equal to), `>=` (greater than or equal to) and `!=` (not equal to).

- The *body* of the loop is *indented*: indentation is Python's way of grouping statements. At the interactive prompt, you have to type a tab or space(s) for each indented line. In practice you will prepare more complicated input for Python with a text editor; all decent text editors have an auto-indent facility. When a compound statement is entered interactively, it must be followed by a blank line to indicate completion (since the parser cannot guess when you have typed the last line). Note that each line within a basic block must be indented by the same amount.

- The `print()` function writes the value of the argument(s) it is given. It differs from just writing the expression you want to write (as we did earlier in the calculator examples) in the way it handles multiple arguments, floating-point quantities, and strings. Strings are printed without quotes, and a space is inserted between items, so you can format things nicely, like this:

  ``` python
  >>> i = 256*256
  >>> print('The value of i is', i)
  The value of i is 65536
  ```

  The keyword argument *end* can be used to avoid the newline after the output, or end the output with a different string:

  ``` python
  >>> a, b = 0, 1
  >>> while a < 1000:
  ...     print(a, end=',')
  ...     a, b = b, a+b
  ...
  0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
  ```

<!-- learning-task:start -->
### Bölüm görevi

**Görev 3.2: Döngüdeki iki değerin değişimini izle**

**Odak:** while, karşılaştırma, doğruluk, girinti, eşzamanlı atama ve print end.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:3.1.3](../3.1-using-python-as-a-calculator/3.1.3-lists/README.md).

#### Tek görev

1. Fibonacci örneğini sınır 13 olacak biçimde yeniden yaz; sayıları aynı satırda virgülle ayır.

2. Çalıştırmadan önce her tur için a ve b başlangıç değerlerini ve sağ tarafta hesaplanan yeni çifti not et.

3. Aynı kodun kopyasında eşzamanlı atamayı a = b ve sonra b = a + b satırlarına ayırıp ilk üç turun neden değiştiğini göster.

4. Koşulda 0, boş metin ve boş listenin doğruluk karşılığını bölümün kuralıyla açıkla.

#### Geçiş ölçütleri

- [ ] Asıl kodun çıktısı 0,1,1,2,3,5,8,; sınırdaki 13 basılmıyor.
- [ ] Sağ tarafın eski a ve b ile, soldan sağa hesaplandığı açıklanmış.
- [ ] Ardışık atamada ikinci satırın yeni a kullandığı somut turla gösterilmiş.
- [ ] Girinti döngü gövdesini belirliyor; boş değerlerin neden döngü başlatmayacağı açıklanmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
