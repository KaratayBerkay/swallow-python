### 5.1.4. Nested List Comprehensions

The initial expression in a list comprehension can be any arbitrary expression, including another list comprehension.

Consider the following example of a 3x4 matrix implemented as a list of 3 lists of length 4:

``` python
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
```
> Code: [matrix.py](matrix.py)

The following list comprehension will transpose rows and columns:

``` python
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```
> Code: [example_01.py](example_01.py)

As we saw in the previous section, the inner list comprehension is evaluated in the context of the `for` that follows it, so this example is equivalent to:

``` python
>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```
> Code: [transposed.py](transposed.py)

which, in turn, is the same as:

``` python
>>> transposed = []
>>> for i in range(4):
...     # the following 3 lines implement the nested listcomp
...     transposed_row = []
...     for row in matrix:
...         transposed_row.append(row[i])
...     transposed.append(transposed_row)
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```
> Code: [transposed_2.py](transposed_2.py)

In the real world, you should prefer built-in functions to complex flow statements. The `zip()` function would do a great job for this use case:

``` python
>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```
> Code: [example_02.py](example_02.py)

See Unpacking Argument Lists for details on the asterisk in this line.

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 5.1.4: Satırlarla sütunların yerini değiştir**

**Odak:** İç içe comprehension, dış bağlam, matris boyutu ve zip(`*matrix`) karşılığı.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:5.1.3](../5.1.3-list-comprehensions/README.md).
- Ön bilgi: [t:4.9.5](../../../04-more-control-flow-tools/4.9-more-on-defining-functions/4.9.5-unpacking-argument-lists/README.md).

##### Tek görev

1. matrix = [[1, 2, 3], [4, 5, 6]] için satırları sütunlara dönüştüren nested comprehension yaz.

2. Aynı dönüşümü açık döngülerle ve bölümdeki zip(`*matrix`) yaklaşımıyla üret.

3. Her sürümün hangi sırada hangi öğeye eriştiğini bir sütun için izle.

##### Geçiş ölçütleri

- [ ] Sonuç [[1, 4], [2, 5], [3, 6]]; 2x3 girdi 3x2 oluyor.
- [ ] Dış indeks sabitken iç comprehension bütün satırları dolaşıyor.
- [ ] zip sürümü [(1, 4), (2, 5), (3, 6)] veriyor; iç liste/tuple farkı fark edilmiş.
- [ ] Boş matris için boş sonuç verecek boyut seçimi açıklanmış; sabit 4 kopyalanmamış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../5.1.5-unpacking-in-lists-and-list-comprehensions/README.md)
<!-- learning-task:end -->
