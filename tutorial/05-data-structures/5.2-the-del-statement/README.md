## 5.2. The `del` statement

There is a way to remove an item from a list given its index instead of its value: the `del` statement. This differs from the `pop()` method which returns a value. The `del` statement can also be used to remove slices from a list or clear the entire list (which we did earlier by assignment of an empty list to the slice). For example:

``` python
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
```
> Code: [a.py](a.py)

`del` can also be used to delete entire variables:

``` python
>>> del a
```
> Code: [example_01.py](example_01.py)

Referencing the name `a` hereafter is an error (at least until another value is assigned to it). We'll find other uses for `del` later.

<!-- learning-task:start -->
### Bölüm görevi

**Görev 5.2: Öğeyi silmekle adı silmeyi ayır**

**Odak:** del ile indeks, dilim, içerik ve ad silme; pop ile fark.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:5.1](../5.1-more-on-lists/README.md).

#### Tek görev

1. a = [10, 20, 30, 40, 50] ve other = a kur. del ile ilk öğeyi, sonra [1:3] dilimini, sonra bütün içeriği sil.

2. Her adımda other üzerinden sonucu kontrol et.

3. En sonda del a yap ve a ile other adlarını ayrı girişlerde değerlendir.

#### Geçiş ölçütleri

- [ ] İçerikler sırasıyla [20, 30, 40, 50], [20, 50], [].
- [ ] del a[:] bütün ortak listenin içeriğini silerken del a yalnız bir adı kaldırıyor.
- [ ] a NameError; other hâlâ boş liste.
- [ ] pop değer döndürürken del bir değer üretmek amacıyla kullanılmamış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../5.3-tuples-and-sequences/README.md)
<!-- learning-task:end -->
