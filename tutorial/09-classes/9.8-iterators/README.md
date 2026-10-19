## 9.8. Iterators

By now you have probably noticed that most container objects can be looped over using a `for` statement:

``` python
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')
```
> Code: [example_01.py](example_01.py)

This style of access is clear, concise, and convenient. The use of iterators pervades and unifies Python. Behind the scenes, the `for` statement calls `iter()` on the container object. The function returns an iterator object that defines the method `__next__()` which accesses elements in the container one at a time. When there are no more elements, `__next__()` raises a `StopIteration` exception which tells the `for` loop to terminate. You can call the `__next__()` method using the `next()` built-in function; this example shows how it all works:

``` python
>>> s = 'abc'
>>> it = iter(s)
>>> it
<str_iterator object at 0x10c90e650>
>>> next(it)
'a'
>>> next(it)
'b'
>>> next(it)
'c'
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(it)
StopIteration
```
> Code: [s.py](s.py)

Having seen the mechanics behind the iterator protocol, it is easy to add iterator behavior to your classes. Define an `__iter__()` method which returns an object with a `__next__()` method. If the class defines `__next__()`, then `__iter__()` can just return `self`:

``` python
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
```
> Code: [init.py](init.py)

``` python
>>> rev = Reverse('spam')
>>> iter(rev)
<__main__.Reverse object at 0x00A1DB50>
>>> for char in rev:
...     print(char)
...
m
a
p
s
```
> Code: [rev.py](rev.py)

<!-- learning-task:start -->
### Bölüm görevi

**Görev 9.8: Tükenen iteratorü yeniden kullanmayı dene**

**Odak:** Iterable/iterator, iter/next, `__iter__`/`__next__`, saklanan durum ve StopIteration.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:9.7](../9.7-odds-and-ends/README.md).
- Ön bilgi: [t:8.4](../../08-errors-and-exceptions/8.4-raising-exceptions/README.md).

#### Tek görev

1. Bölümdeki Reverse sınıfından yola çıkarak sırayla 0 ile limit arasındaki sayıları, limit hariç, veren Counter iteratorü yaz. iter(self) kendisini döndürsün; sınırda StopIteration yükseltsin. limit=2 için iki next ve üçüncü hata girişini dene; aynı nesne üzerinde for çalıştır, sonra yeni Counter(2) ile tekrar for çalıştır.

2. Boş sınırı da dene.

#### Geçiş ölçütleri

- [ ] İlk iki değer 0 ve 1; üçüncü next StopIteration.
- [ ] Tükenmiş aynı nesnede for yeni değer üretmiyor; yeni nesne 0, 1 üretiyor.
- [ ] limit=0 hemen tükeniyor.
- [ ] Durum örnek üzerinde tutuluyor; for sona ermek için StopIteration kullanıyor.
- [ ] Yeni iterable üzerinde iter oluşturmakla tükenmiş iteratorü yeniden almak ayrılmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../9.9-generators/README.md)
<!-- learning-task:end -->
