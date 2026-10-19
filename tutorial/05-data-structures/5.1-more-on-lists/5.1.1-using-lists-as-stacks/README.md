### 5.1.1. Using Lists as Stacks

The list methods make it very easy to use a list as a stack, where the last element added is the first element retrieved ("last-in, first-out"). To add an item to the top of the stack, use `append()`. To retrieve an item from the top of the stack, use `pop()` without an explicit index. For example:

``` python
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
```
> Code: [stack.py](stack.py)

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 5.1.1: Son eklenen işi geri al**

**Odak:** LIFO yığın davranışı, append ve pop.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:5.1](../README.md).

##### Tek görev

1. Bir işlem geçmişini listeyle modelle: "open", "edit", "save" işlemlerini sırayla ekle; iki geri alma işlemi yap ve geri alınan değerleri yazdır.

2. Kalan geçmişi göster.

3. Aynı nesne üzerinde her adımın etkisini takip et.

##### Geçiş ölçütleri

- [ ] Geri alınanlar save ve edit; kalan geçmiş ["open"].
- [ ] Ekleme ve alma aynı uçtan append/pop ile yapılmış.
- [ ] Bir sonraki geri almanın open vereceği, boşken pop yapılmasının sonucu açıklanmış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../5.1.2-using-lists-as-queues/README.md)
<!-- learning-task:end -->
