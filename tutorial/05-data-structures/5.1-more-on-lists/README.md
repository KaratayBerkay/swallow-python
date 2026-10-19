## 5.1. More on Lists

The list data type has some more methods. Here are all of the methods of list objects:

`list.append(value, /)`

Add an item to the end of the list. Similar to `a[len(a):] = [x]`.

`list.extend(iterable, /)`

Extend the list by appending all the items from the iterable. Similar to `a[len(a):] = iterable`.

`list.insert(index, value, /)`

Insert an item at a given position. The first argument is the index of the element before which to insert, so `a.insert(0, x)` inserts at the front of the list, and `a.insert(len(a), x)` is equivalent to `a.append(x)`.

`list.remove(value, /)`

Remove the first item from the list whose value is equal to *value*. It raises a `ValueError` if there is no such item.

`list.pop(index=-1, /)`

Remove the item at the given position in the list, and return it. If no index is specified, `a.pop()` removes and returns the last item in the list. It raises an `IndexError` if the list is empty or the index is outside the list range.

`list.clear()`

Remove all items from the list. Similar to `del a[:]`.

`list.index(value[, start[, stop]])`

Return zero-based index of the first occurrence of *value* in the list. Raises a `ValueError` if there is no such item.

The optional arguments *start* and *end* are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the *start* argument.

`list.count(value, /)`

Return the number of times *value* appears in the list.

`list.sort(*, key=None, reverse=False)`

Sort the items of the list in place (the arguments can be used for sort customization, see `sorted()` for their explanation).

`list.reverse()`

Reverse the elements of the list in place.

`list.copy()`

Return a shallow copy of the list. Similar to `a[:]`.

An example that uses most of the list methods:

``` python
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4)  # Find next banana starting at position 4
6
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'
```
> Code: [fruits.py](fruits.py)

You might have noticed that methods like `insert`, `remove` or `sort` that only modify the list have no return value printed -- they return the default `None`. (Other languages may return the mutated object, which allows method chaining, such as `d->insert("a")->remove("b")->sort();`.) This is a design principle for all mutable data structures in Python.

Another thing you might notice is that not all data can be sorted or compared. For instance, `[None, 'hello', 10]` doesn't sort because integers can't be compared to strings and `None` can't be compared to other types. Also, there are some types that don't have a defined ordering relation. For example, `3+4j < 5+7j` isn't a valid comparison.


<!-- learning-task:start -->
### Bölüm görevi

**Görev 5.1: Liste düzenleme günlüğü tut**

**Odak:** Liste metotlarının öğe/değer/indeks ayrımı, yerinde değişim, dönüş değeri ve sığ kopya.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:3.1.3](../../03-an-informal-introduction-to-python/3.1-using-python-as-a-calculator/3.1.3-lists/README.md).
- Ön bilgi: [t:4.8](../../04-more-control-flow-tools/4.8-defining-functions/README.md).

#### Tek görev

1. Bir stok listesi üzerinde işlem günlüğü hazırla: stock = ["pear", "apple", "pear"]. count ve index ile tekrarları incele; insert ile başa "fig" koy; extend ile ["plum", "lime"] ekle; remove ile ilk "pear" değerini sil; pop ile son öğeyi al; sort ve reverse uygula.

2. Her satır için önce listeyi ve varsa dönüş değerini tahmin et, sonra dene.

3. Bağımsız kopyalarda append ile extend, copy ile atama ve clear ile boş listeye yeniden bağlama farkını göster.

4. Olmayan değeri arama/silme ve boş listeden pop denemelerini ayrı yap.

#### Geçiş ölçütleri

- [ ] İlk count 2 ve index 0; ikinci pear için arama başlangıcı kullanılmış.
- [ ] remove ilk eşleşmeyi, pop son öğeyi seçiyor ve lime döndürüyor.
- [ ] Sıralama sonrası apple, fig, pear, plum; tersinde plum, pear, fig, apple.
- [ ] Yerinde düzenleyen metotların None dönüşü listeyle karıştırılmamış.
- [ ] append tek öğe, extend ayrı öğeler ekliyor; kopya ile ortak nesne farkı gösterilmiş.
- [ ] Eksik değer ValueError, boş pop IndexError; karışık sıralanamayan türlerin neden sorun olduğu açıklanmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](5.1.1-using-lists-as-stacks/README.md)
<!-- learning-task:end -->
### Sections

- [5.1.1. Using Lists as Stacks](5.1.1-using-lists-as-stacks/README.md)
- [5.1.2. Using Lists as Queues](5.1.2-using-lists-as-queues/README.md)
- [5.1.3. List Comprehensions](5.1.3-list-comprehensions/README.md)
- [5.1.4. Nested List Comprehensions](5.1.4-nested-list-comprehensions/README.md)
- [5.1.5. Unpacking in Lists and List Comprehensions](5.1.5-unpacking-in-lists-and-list-comprehensions/README.md)

<!-- learning-milestone:start -->
### Klasör milestone görevi

**Milestone: Bekleyen işleri iki farklı sırayla işle**

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Liste metotları, stack/queue ve comprehensionla yeni veri üretimini birleştirme.

#### Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

#### Tek görev

1. groups = [[3, 1], [], [2, 3]] için düz listeyi comprehension ile üret.

2. Kaynağı koruyarak sıralı kopya oluştur.

3. Aynı düz veriden bir liste yığını ve bir deque kuyruğu kur; ikisinden de iki öğe alıp kalanları karşılaştır.

4. İki satırlı bir matrisin transpose iskeletinde neden farklı for sırası gerektiğini bu akışın düzleştirmesiyle karşılaştır.

5. Yıldızlı comprehensionun karşılığını yazılı göster.

#### Geçiş ölçütleri

- [ ] Düz veri [3, 1, 2, 3], kaynak iç içe yapı korunmuş.
- [ ] Yığın 3 sonra 2; kuyruk 3 sonra 1 çıkarıyor.
- [ ] Sıralı kopya [1, 2, 3, 3]; sort dönüşü liste sanılmamış.
- [ ] Transpose sütun oluşturur, flatten öğeleri tek sıraya açar; for sırası açıklanmış.
- [ ] Sürüm gerektiren yıldızlı biçim eski yorumlayıcıya zorla çalıştırılmamış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../5.2-the-del-statement/README.md)
<!-- learning-milestone:end -->
