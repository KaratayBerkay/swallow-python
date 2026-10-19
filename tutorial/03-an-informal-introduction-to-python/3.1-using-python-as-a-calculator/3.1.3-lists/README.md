### 3.1.3. Lists

Python knows a number of *compound* data types, used to group together other values. The most versatile is the *list*, which can be written as a list of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type.

``` python
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
```
> Code: [squares.py](squares.py)

Like strings (and all other built-in sequence types), lists can be indexed and sliced:

``` python
>>> squares[0]  # indexing returns the item
1
>>> squares[-1]
25
>>> squares[-3:]  # slicing returns a new list
[9, 16, 25]
```
> Code: [example_01.py](example_01.py)

Lists also support operations like concatenation:

``` python
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
> Code: [example_02.py](example_02.py)

Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:

``` python
>>> cubes = [1, 8, 27, 65, 125]  # something's wrong here
>>> 4 ** 3  # the cube of 4 is 64, not 65!
64
>>> cubes[3] = 64  # replace the wrong value
>>> cubes
[1, 8, 27, 64, 125]
```
> Code: [cubes.py](cubes.py)

You can also add new items at the end of the list, by using the `list.append()` *method* (we will see more about methods later):

``` python
>>> cubes.append(216)  # add the cube of 6
>>> cubes.append(7 ** 3)  # and the cube of 7
>>> cubes
[1, 8, 27, 64, 125, 216, 343]
```
> Code: [example_03.py](example_03.py)

Simple assignment in Python never copies data. When you assign a list to a variable, the variable refers to the *existing list*. Any changes you make to the list through one variable will be seen through all other variables that refer to it.:

``` python
>>> rgb = ["Red", "Green", "Blue"]
>>> rgba = rgb
>>> id(rgb) == id(rgba)  # they reference the same object
True
>>> rgba.append("Alph")
>>> rgb
["Red", "Green", "Blue", "Alph"]
```
> Code: [rgb.py](rgb.py)

All slice operations return a new list containing the requested elements. This means that the following slice returns a shallow copy of the list:

``` python
>>> correct_rgba = rgba[:]
>>> correct_rgba[-1] = "Alpha"
>>> correct_rgba
["Red", "Green", "Blue", "Alpha"]
>>> rgba
["Red", "Green", "Blue", "Alph"]
```
> Code: [correct_rgba.py](correct_rgba.py)

Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:

``` python
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> # replace some values
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> # now remove them
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> # clear the list by replacing all the elements with an empty list
>>> letters[:] = []
>>> letters
[]
```
> Code: [letters.py](letters.py)

The built-in function `len()` also applies to lists:

``` python
>>> letters = ['a', 'b', 'c', 'd']
>>> len(letters)
4
```
> Code: [letters_2.py](letters_2.py)

It is possible to nest lists (create lists containing other lists), for example:

``` python
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
```
> Code: [a.py](a.py)

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 3.1.3: Ortak liste ile kopyayı ayır**

**Odak:** Liste kurma, indeks/dilim, birleştirme, yerinde değişiklik, append, alias, dilim kopyası ve iç içe liste.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:3.1.2](../3.1.2-text/README.md).

##### Tek görev

1. items = [2, 4, 7] ile başla. alias = items ve copied = items[:] oluştur. alias üzerinden son sayıyı 6 yapıp 8 ekle; copied üzerinden ilk sayıyı 0 yap.

2. Her adımda üç ismin gösterdiği içeriği kaydet.

3. Ardından items[1:3] dilimini [9] ile değiştir, ilk/son öğeyi ve uzunluğu kontrol et. [items, copied] içinden copied listesinin ikinci öğesini indeksle al.

4. Son olarak copied[:] = [] ile boşalt ve items + [10] sonucunu karşılaştır.

##### Geçiş ölçütleri

- [ ] İlk değişikliklerden sonra items ve alias [2, 4, 6, 8], copied [0, 4, 7].
- [ ] Dilim atamasından sonra items ve alias [2, 9, 8], uzunluk 3; nested erişim 4.
- [ ] copied boşalınca items korunuyor; + yeni bir liste üretirken append mevcut listeyi değiştiriyor.
- [ ] Atamanın kopya üretmediği, [:] işleminin yeni dış liste ürettiği kendi sözcüklerinle açıklanmış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
