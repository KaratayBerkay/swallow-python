## 11.7. Tools for working with lists

Many data structure needs can be met with the built-in list type. However, sometimes there is a need for alternative implementations with different performance trade-offs.

The `array` module provides an `array` object that is like a list that stores only homogeneous data and stores it more compactly. The following example shows an array of numbers stored as two byte unsigned binary numbers (typecode `"H"`) rather than the usual 16 bytes per entry for regular lists of Python int objects:

``` python
>>> from array import array
>>> a = array('H', [4000, 10, 700, 22222])
>>> sum(a)
26932
>>> a[1:3]
array('H', [10, 700])
```
> Code: [a.py](a.py)

The `collections` module provides a `deque` object that is like a list with faster appends and pops from the left side but slower lookups in the middle. These objects are well suited for implementing queues and breadth first tree searches:

``` python
>>> from collections import deque
>>> d = deque(["task1", "task2", "task3"])
>>> d.append("task4")
>>> print("Handling", d.popleft())
Handling task1
```
> Code: [d.py](d.py)

``` python
unsearched = deque([starting_node])
def breadth_first_search(unsearched):
    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)
```
> Code: [breadth_first_search.py](breadth_first_search.py)

In addition to alternative list implementations, the library also offers other tools such as the `bisect` module with functions for manipulating sorted lists:

``` python
>>> import bisect
>>> scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
>>> bisect.insort(scores, (300, 'ruby'))
>>> scores
[(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]
```
> Code: [scores.py](scores.py)

The `heapq` module provides functions for implementing heaps based on regular lists. The lowest valued entry is always kept at position zero. This is useful for applications which repeatedly access the smallest element but do not want to run a full list sort:

``` python
>>> from heapq import heapify, heappop, heappush
>>> data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
>>> heapify(data)                      # rearrange the list into heap order
>>> heappush(data, -5)                 # add a new entry
>>> [heappop(data) for i in range(3)]  # fetch the three smallest entries
[-5, 0, 1]
```
> Code: [data.py](data.py)

<!-- learning-task:start -->
### Bölüm görevi

**Görev 11.7: Veri yapısını erişim ihtiyacına göre seç**

**Odak:** array H, deque, bisect.insort ve heapq minimum alma.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:11.6](../11.6-weak-references/README.md).
- Ön bilgi: [t:5.1.2](../../05-data-structures/5.1-more-on-lists/5.1.2-using-lists-as-queues/README.md).

#### Tek görev

1. Tek bir görev listesi için dört görünüm üret: [4, 1, 3] sayılarını array("H", ...) içine koyup toplam ve dilimini al; üç adı deque kuyruğunda işleyip ilkini çıkar; sıralı [(10, "a"), (30, "c")] listesine bisect.insort ile (20, "b") ekle; [4, 1, 3] üzerinde heapify, heappush(0) ve iki heappop yap.

2. Her aracı hangi erişim ihtiyacı için seçtiğini açıkla.

#### Geçiş ölçütleri

- [ ] array toplamı 8, dilimi aynı türde sayısal veri; homojen saklama belirtilmiş.
- [ ] Kuyruk ilk geleni çıkarıyor; orta indeks performansı listeyle aynı varsayılmamış.
- [ ] insort sıralı diziyi 10, 20, 30 düzeninde tutuyor.
- [ ] heapten çıkanlar 0, 1; bütün heap listesinin sıralı olması şart sayılmamış.
- [ ] BFS örneğini yeniden yazmak yerine bölümde gerçekten gösterilen işlemler değerlendirilmiş.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../11.8-decimal-floating-point-arithmetic/README.md)
<!-- learning-task:end -->
