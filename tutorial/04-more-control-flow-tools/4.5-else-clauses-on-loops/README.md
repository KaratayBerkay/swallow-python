## 4.5. `else` Clauses on Loops

In a `for` or `while` loop the `break` statement may be paired with an `else` clause. If the loop finishes without executing the `break`, the `else` clause executes.

In a `for` loop, the `else` clause is executed after the loop finishes its final iteration, that is, if no break occurred.

In a `while` loop, it's executed after the loop's condition becomes false.

In either kind of loop, the `else` clause is **not** executed if the loop was terminated by a `break`. Of course, other ways of ending the loop early, such as a `return` or a raised exception, will also skip execution of the `else` clause.

This is exemplified in the following `for` loop, which searches for prime numbers:

``` python
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(n, 'equals', x, '*', n//x)
...             break
...     else:
...         # loop fell through without finding a factor
...         print(n, 'is a prime number')
...
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```
> Code: [example_01.py](example_01.py)

(Yes, this is the correct code. Look closely: the `else` clause belongs to the `for` loop, **not** the `if` statement.)

One way to think of the else clause is to imagine it paired with the `if` inside the loop. As the loop executes, it will run a sequence like if/if/if/else. The `if` is inside the loop, encountered a number of times. If the condition is ever true, a `break` will happen. If the condition is never true, the `else` clause outside the loop will execute.

When used with a loop, the `else` clause has more in common with the `else` clause of a `try` statement than it does with that of `if` statements: a `try` statement's `else` clause runs when no exception occurs, and a loop's `else` clause runs when no `break` occurs. For more on the `try` statement and exceptions, see Handling Exceptions.

<!-- learning-task:start -->
### Bölüm görevi

**Görev 4.5: Arama bittiğinde doğru mesajı üret**

**Odak:** Döngü else dalı, normal tamamlanma, boş döngü ve break ile çıkış.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:4.4](../4.4-break-and-continue-statements/README.md).

#### Tek görev

1. Bir listede 7 arayan for döngüsü yaz: bulunca "found" yazıp break ile çık; döngü aramayı tamamladıysa else içinde "missing" yaz. [2, 7, 9], [2, 9] ve [] verilerini dene. else girintisinin ait olduğu bloğu işaretle.

2. Aynı kuralın while koşulu yanlış olduğunda nasıl uygulanacağını anlat.

#### Geçiş ölçütleri

- [ ] Üç senaryo sırasıyla found, missing, missing üretiyor.
- [ ] else, if yerine for ile aynı girintide.
- [ ] Boş liste için de break olmadığı açıklanmış.
- [ ] continue eklemenin tek başına else dalını engellemeyeceği kontrol akışıyla açıklanmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../4.6-pass-statements/README.md)
<!-- learning-task:end -->
