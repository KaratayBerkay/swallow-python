## 9.10. Generator Expressions

Some simple generators can be coded succinctly as expressions using a syntax similar to list comprehensions but with parentheses instead of square brackets. These expressions are designed for situations where the generator is used right away by an enclosing function. Generator expressions are more compact but less versatile than full generator definitions and tend to be more memory friendly than equivalent list comprehensions.

Examples:

``` python
>>> sum(i*i for i in range(10))                 # sum of squares
285

>>> xvec = [10, 20, 30]
>>> yvec = [7, 5, 3]
>>> sum(x*y for x,y in zip(xvec, yvec))         # dot product
260

>>> unique_words = set(word for line in page  for word in line.split())

>>> valedictorian = max((student.gpa, student.name) for student in graduates)

>>> data = 'golf'
>>> list(data[i] for i in range(len(data)-1, -1, -1))
['f', 'l', 'o', 'g']

>>> x = [[1,2,3], [], [4, 5]]
>>> g = (*i for i in x)
>>> list(g)
[1, 2, 3, 4, 5]
```
> Code: [xvec.py](xvec.py)

In most cases, generator expressions must be wrapped in parentheses. As a special case, however, when provided as the sole argument to a function (as in the examples involving `sum`, `set`, `max`, and `list` above), the generator expression does not need to be wrapped in an additional set of parentheses. That is to say, the following two pieces of code are semantically equivalent:

``` python
>>> f(x for x in y)
>>> f((x for x in y))
```
> Code: [example_01.py](example_01.py)

as are the following:

``` python
>>> f(*x for x in y)
>>> f((*x for x in y))
```
> Code: [example_02.py](example_02.py)

<!-- learning-task:start -->
### Bölüm görevi

**Görev 9.10: Liste üretmeden hesapla ve tüketimi izle**

**Odak:** Generator expression, kapsamlı parantez, tek argüman istisnası ve tüketim.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:9.9](../9.9-generators/README.md).
- Ön bilgi: [t:5.1.3](../../05-data-structures/5.1-more-on-lists/5.1.3-list-comprehensions/README.md).

**Kaynak/ortam notu:** Yalnız yıldızlı generator expression Python 3.15 gerektirir; normal generator deneyi 3.11 ile yapılabilir.

#### Tek görev

1. numbers = [1, 2, 3] için kareleri veren generator expression g oluştur. next(g), sum(g), list(g) sırasını izle.

2. Aynı toplamı yeni expressionı doğrudan sum içine vererek al; liste comprehension karşılığıyla üretim/tüketim farkını açıkla. [[1, 2], [], [3]] için bölümdeki yıldızlı generator biçiminin verdiği diziyi yazılı çıkar.

#### Geçiş ölçütleri

- [ ] next 1, kalan toplam 13, son liste []; yeni expression toplamı 14.
- [ ] Tek argümanlı sum içine expression ek parantezsiz verilebiliyor.
- [ ] Liste biriktirme ile gerektiğinde öğe üretme farkı açıklanmış.
- [ ] Yıldızlı expression 1, 2, 3 sağlar; boş alt liste atlanır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
