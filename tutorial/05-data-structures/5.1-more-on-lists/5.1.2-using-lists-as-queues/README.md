### 5.1.2. Using Lists as Queues

It is also possible to use a list as a queue, where the first element added is the first element retrieved ("first-in, first-out"); however, lists are not efficient for this purpose. While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one). See Time complexity of operations on built-in types for more information.

To implement a queue, use `collections.deque` which was designed to have fast appends and pops from both ends. For example:

``` python
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```
> Code: [queue_example.py](queue_example.py)

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 5.1.2: Sıraya ilk gireni önce işle**

**Odak:** FIFO kuyruk ve deque ile soldan alma.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:5.1.1](../5.1.1-using-lists-as-stacks/README.md).

##### Tek görev

1. deque ile "Ada", "Ece" kuyruğunu kur; "Can" ekle, iki kişiyi popleft ile işle, sonra "Deniz" ekle.

2. İşlenen ve bekleyen kişileri göster.

3. Aynı sırayı listenin sonundan pop ile alsaydın ilk kimin çıkacağını ve neden yanlış model olacağını açıkla.

##### Geçiş ölçütleri

- [ ] İşlenenler Ada ve Ece; kalanlar Can, Deniz sırasıyla.
- [ ] Kuyruk append ve popleft kullanıyor.
- [ ] LIFO ile FIFO ayrımı somut sıra üzerinden; listede baştan alma sırasında öğe kaydırma maliyeti açıklanmış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../5.1.3-list-comprehensions/README.md)
<!-- learning-task:end -->
