### 7.1.2. The string format() method

Basic usage of the `str.format()` method looks like this:

``` python
>>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"
```
> Code: [example_01.py](example_01.py)

The brackets and characters within them (called format fields) are replaced with the objects passed into the `str.format()` method. A number in the brackets can be used to refer to the position of the object passed into the `str.format()` method.

``` python
>>> print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam
```
> Code: [example_02.py](example_02.py)

If keyword arguments are used in the `str.format()` method, their values are referred to by using the name of the argument.

``` python
>>> print('This {food} is {adjective}.'.format(
...       food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.
```
> Code: [food.py](food.py)

Positional and keyword arguments can be arbitrarily combined:

``` python
>>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
...                                                    other='Georg'))
The story of Bill, Manfred, and Georg.
```
> Code: [other.py](other.py)

If you have a really long format string that you don't want to split up, it would be nice if you could reference the variables to be formatted by name instead of by position. This can be done by simply passing the dict and using square brackets `'[]'` to access the keys.

``` python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
...       'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```
> Code: [table.py](table.py)

This could also be done by passing the `table` dictionary as keyword arguments with the `**` notation.

``` python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```
> Code: [table_2.py](table_2.py)

This is particularly useful in combination with the built-in function `vars()`, which returns a dictionary containing all local variables:

``` python
>>> table = {k: str(v) for k, v in vars().items()}
>>> message = " ".join([f'{k}: ' + '{' + k +'};' for k in table.keys()])
>>> print(message.format(**table))
__name__: __main__; __doc__: None; __package__: None; __loader__: ...
```
> Code: [table_3.py](table_3.py)

As an example, the following lines produce a tidily aligned set of columns giving integers and their squares and cubes:

``` python
>>> for x in range(1, 11):
...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```
> Code: [example_03.py](example_03.py)

For a complete overview of string formatting with `str.format()`, see Format string syntax.

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 7.1.2: Şablon alanlarını argümana bağla**

**Odak:** Otomatik/numaralı/anahtarlı format alanları, sözlük erişimi, ** ve alan genişliği.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:7.1.1](../7.1.1-formatted-string-literals/README.md).
- Ön bilgi: [t:4.9.5](../../../04-more-control-flow-tools/4.9-more-on-defining-functions/4.9.5-unpacking-argument-lists/README.md).

##### Tek görev

1. data = {"name": "Ada", "count": 7} için "Ada:   7" satırını format ile üç yoldan üret: konumsal numaralar, {0[name]} gibi sözlük alanı, `**data` ile anahtar alanları.

2. İlk yolda argümanları ters sırayla verip alan numaralarını düzelt.

3. Ayrıca iki küçük işaretçi değişken için vars() içinden adlara erişimin şablona veri sağlamasını bölümdeki örnek üzerinden açıkla.

##### Geçiş ölçütleri

- [ ] Üç yol aynı metni ve genişliği üretiyor.
- [ ] Konum sırası değişince doğru değerler numarayla seçiliyor.
- [ ] Sözlük alanı erişimiyle ** açma aynı mekanizma sanılmamış.
- [ ] vars() sözlük sağlıyor; bütün ortam çıktısının sabit olması beklenmemiş.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../7.1.3-manual-string-formatting/README.md)
<!-- learning-task:end -->
