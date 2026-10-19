## 5.5. Dictionaries

Another useful data type built into Python is the *dictionary* (see Mapping types --- dict, frozendict). Dictionaries are sometimes found in other languages as "associative memories" or "associative arrays". Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by *keys*, which can be any immutable type; strings and numbers can always be keys. Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. You can't use lists as keys, since lists can be modified in place using index assignments, slice assignments, or methods like `append()` and `extend()`.

It is best to think of a dictionary as a set of *key: value* pairs, with the requirement that the keys are unique (within one dictionary). A pair of braces creates an empty dictionary: `{}`. Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs to the dictionary; this is also the way dictionaries are written on output.

The main operations on a dictionary are storing a value with some key and extracting the value given the key. It is also possible to delete a key:value pair with `del`. If you store using a key that is already in use, the old value associated with that key is forgotten.

Extracting a value for a non-existent key by subscripting (`d[key]`) raises a `KeyError`. To avoid getting this error when trying to access a possibly non-existent key, use the `get()` method instead, which returns `None` (or a specified default value) if the key is not in the dictionary.

Performing `list(d)` on a dictionary returns a list of all the keys used in the dictionary, in insertion order (if you want it sorted, just use `sorted(d)` instead). To check whether a single key is in the dictionary, use the `in` keyword.

Here is a small example using a dictionary:

``` python
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> tel['irv']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'irv'
>>> print(tel.get('irv'))
None
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
```
> Code: [tel.py](tel.py)

The `dict()` constructor builds dictionaries directly from sequences of key-value pairs:

``` python
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```
> Code: [example_01.py](example_01.py)

In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:

``` python
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
```
> Code: [example_02.py](example_02.py)

And dictionary unpacking (via `**`) can be used to merge multiple dictionaries:

``` python
>>> odds = {i: i**2 for i in (1, 3, 5)}
>>> evens = {i: i**2 for i in (2, 4, 6)}
>>> {**odds, **evens}
{1: 1, 3: 9, 5: 25, 2: 4, 4: 16, 6: 36}

>>> all_values = [odds, evens, {0: 0}]
>>> {**i for i in all_values}
{1: 1, 3: 9, 5: 25, 2: 4, 4: 16, 6: 36, 0: 0}
```
> Code: [odds.py](odds.py)

When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:

``` python
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```
> Code: [example_03.py](example_03.py)

<!-- learning-task:start -->
### Bölüm görevi

**Görev 5.5: Anahtarın yaşam döngüsünü yönet**

**Odak:** Sözlük oluşturma, ekleme/güncelleme/silme, get, üyelik, anahtar sırası, uygun anahtar ve birleştirme.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:5.4](../5.4-sets/README.md).
- Ön bilgi: [t:5.2](../5.2-the-del-statement/README.md).

**Kaynak/ortam notu:** Yalnız son örnekteki {`**i` for ...} Python 3.15 gerektirir; sözlük oluşturma ve {`**left`, `**right`} birleştirmesi eski sürümlerde de kullanılabilir.

#### Tek görev

1. stock = {"pear": 2, "apple": 1} için pear miktarını 5 yap, fig ekle, apple sil.

2. Var olan ve olmayan anahtarları [] ve get ile ayrı ayrı sorgula; list(stock) ve sorted(stock) sonuçlarını karşılaştır.

3. Aynı veriyi çiftler listesinden dict ile yeniden kur. 1, 2, 3 için kareler sözlüğü üret; başka bir sözlükle aynı anahtarın da bulunduğu ** birleştirmesi yap.

4. Anahtar olarak metin, sayı, yalnız değişmez öğeler içeren tuple ve liste seçeneklerini değerlendir.

#### Geçiş ölçütleri

- [ ] Güncelleme yeni pear anahtarı üretmiyor; silme/ekleme sonrası anahtarlar pear, fig sırasıyla.
- [ ] Eksik [] KeyError; get varsayılanı None veya verilen değer; üyelik anahtarları kontrol ediyor.
- [ ] Comprehension {1: 1, 2: 4, 3: 9}; sağdaki sözlüğün çakışan değeri kazanıyor.
- [ ] Liste ve içinde liste bulunan tuple anahtar olarak kabul edilmiyor; değerler aynı kısıta tabi tutulmamış.
- [ ] {`**i` for i in all_values} örneğinin neyi birleştirdiği yazılı olarak açıklanmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../5.6-looping-techniques/README.md)
<!-- learning-task:end -->
