## 4.4. `break` and `continue` Statements

The `break` statement breaks out of the innermost enclosing `for` or `while` loop:

``` python
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(f"{n} equals {x} * {n//x}")
...             break
...
4 equals 2 * 2
6 equals 2 * 3
8 equals 2 * 4
9 equals 3 * 3
```
> Code: [example_01.py](example_01.py)

The `continue` statement continues with the next iteration of the loop:

``` python
>>> for num in range(2, 10):
...     if num % 2 == 0:
...         print(f"Found an even number {num}")
...         continue
...     print(f"Found an odd number {num}")
...
Found an even number 2
Found an odd number 3
Found an even number 4
Found an odd number 5
Found an even number 6
Found an odd number 7
Found an even number 8
Found an odd number 9
```
> Code: [example_02.py](example_02.py)

<!-- learning-task:start -->
### Bölüm görevi

**Görev 4.4: Atlama ile döngüyü bitirmeyi ayır**

**Odak:** continue turu atlar; break en içteki döngüyü bitirir.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:4.3](../4.3-the-range-function/README.md).
- Ön bilgi: [t:4.1](../4.1-if-statements/README.md).

#### Tek görev

1. groups = [[2, 0, 4, 9, 6], [0, 3, 9, 5]] için iç içe for yaz.

2. Her grupta 0 gelince turu atla, 9 gelince yalnızca o grubun döngüsünü bitir, diğer sayıları yazdır.

3. Çıktıyı çalıştırmadan önce çıkar.

4. Sonra if num == 0 bloğunu tamamen kaldırıp 0 değerlerinin davranışını yeniden incele.

#### Geçiş ölçütleri

- [ ] Asıl çıktı sırayla 2, 4, 3; 6 ve 5 basılmıyor.
- [ ] İlk 9 dış döngüyü bitirmiyor; ikinci grup işleniyor.
- [ ] continue sonrası aynı turun kalan satırlarının çalışmadığı gösterilmiş.
- [ ] continue kaldırıldığında 0 değerlerinin de yazdırılacağı açıklanmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../4.5-else-clauses-on-loops/README.md)
<!-- learning-task:end -->
