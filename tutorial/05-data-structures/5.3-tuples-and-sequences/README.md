## 5.3. Tuples and Sequences

We saw that lists and strings have many common properties, such as indexing and slicing operations. They are two examples of *sequence* data types (see Sequence Types --- list, tuple, range). Since Python is an evolving language, other sequence data types may be added. There is also another standard sequence data type: the *tuple*.

A tuple consists of a number of values separated by commas, for instance:

``` python
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # Tuples may be nested:
>>> u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuples are immutable:
>>> t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # but they can contain mutable objects:
>>> v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])
>>> # they support unpacking just like lists:
>>> x = [1, 2, 3]
>>> 0, *x, 4
(0, 1, 2, 3, 4)
```
> Code: [t.py](t.py)

As you see, on output tuples are always enclosed in parentheses, so that nested tuples are interpreted correctly; they may be input with or without surrounding parentheses, although often parentheses are necessary anyway (if the tuple is part of a larger expression). It is not possible to assign to the individual items of a tuple, however it is possible to create tuples which contain mutable objects, such as lists.

Though tuples may seem similar to lists, they are often used in different situations and for different purposes. Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking (see later in this section) or indexing (or even by attribute in the case of `namedtuples`). Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.

A special problem is the construction of tuples containing 0 or 1 items: the syntax has some extra quirks to accommodate these. Empty tuples are constructed by an empty pair of parentheses; a tuple with one item is constructed by following a value with a comma (it is not sufficient to enclose a single value in parentheses). Ugly, but effective. For example:

``` python
>>> empty = ()
>>> singleton = 'hello',    # <-- note trailing comma
>>> len(empty)
0
>>> len(singleton)
1
>>> singleton
('hello',)
```
> Code: [empty.py](empty.py)

The statement `t = 12345, 54321, 'hello!'` is an example of *tuple packing*: the values `12345`, `54321` and `'hello!'` are packed together in a tuple. The reverse operation is also possible:

``` python
>>> x, y, z = t
```
> Code: [example_01.py](example_01.py)

This is called, appropriately enough, *sequence unpacking* and works for any sequence on the right-hand side. Sequence unpacking requires that there are as many variables on the left side of the equals sign as there are elements in the sequence. Note that multiple assignment is really just a combination of tuple packing and sequence unpacking.

<!-- learning-task:start -->
### Bölüm görevi

**Görev 5.3: Değişmeyen kaydın içindeki listeyi izle**

**Odak:** Tuple packing/unpacking, virgül, boş/tek öğeli tuple ve değiştirilebilir içerik.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:5.2](../5.2-the-del-statement/README.md).
- Ön bilgi: [t:3.1.3](../../03-an-informal-introduction-to-python/3.1-using-python-as-a-calculator/3.1.3-lists/README.md).

#### Tek görev

1. record = "Ada", [3, 4] kaydını kur; name, scores = record ile aç. scores listesine 5 ekle ve record içeriğini göster. record[0] değerine yeni ad atamayı ayrı girişte dene.

2. Boş tuple, tek öğeli tuple ve yalnız parantezlenmiş metin oluşturup uzunluklarını karşılaştır.

3. İki öğeli kaydı üç değişkene açmayı da ayrı dene.

#### Geçiş ölçütleri

- [ ] record içindeki liste [3, 4, 5] oluyor; tuple öğesinin kendisine atama TypeError.
- [ ] () uzunluğu 0; ("Ada",) uzunluğu 1; ("Ada") bir metin ve uzunluğu 3.
- [ ] Tuple oluşturanın virgül olduğu, packing ve unpacking yönleri açıklanmış.
- [ ] Fazla değişkenle açma ValueError; tuple değişmezliğinin içindeki listeyi değişmez yapmadığı açıklanmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../5.4-sets/README.md)
<!-- learning-task:end -->
