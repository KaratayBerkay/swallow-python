## 9.9. Generators

Generators are a simple and powerful tool for creating iterators. They are written like regular functions but use the `yield` statement whenever they want to return data. Each time `next()` is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed). An example shows that generators can be trivially easy to create:

``` python
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
```
> Code: [reverse.py](reverse.py)

``` python
>>> for char in reverse('golf'):
...     print(char)
...
f
l
o
g
```
> Code: [example_01.py](example_01.py)

Anything that can be done with generators can also be done with class-based iterators as described in the previous section. What makes generators so compact is that the `__iter__()` and `__next__()` methods are created automatically.

Another key feature is that the local variables and execution state are automatically saved between calls. This made the function easier to write and much more clear than an approach using instance variables like `self.index` and `self.data`.

In addition to automatic method creation and saving program state, when generators terminate, they automatically raise `StopIteration`. In combination, these features make it easy to create iterators with no more effort than writing a regular function.

<!-- learning-task:start -->
### Bölüm görevi

**Görev 9.9: Durumu yield aralarında koru**

**Odak:** Generator fonksiyonu, ertelenen yürütme, yield ile durma/devam ve otomatik tükenme.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:9.8](../9.8-iterators/README.md).

#### Tek görev

1. 0 ile limit arasındaki sayıları veren generator yaz.

2. Gövde başına "started", her yield sonrasına "resumed" mesajı koy. limit=2 için generator oluştur, bir next yap, ikinci next yap, üçüncü next dene.

3. Mesajların hangi olayda basıldığını önce tahmin et.

4. Boş sınır için yeni generator oluşturup listele.

#### Geçiş ölçütleri

- [ ] Nesne oluşturmak started basmıyor; ilk next gövdeyi başlatıyor.
- [ ] İlk değer 0; ikinci 1; sonraki next son resumed ardından StopIteration.
- [ ] Yerel değişken ve yürütme konumu çağrılar arasında korunuyor.
- [ ] Boş generator [] üretiyor; `__iter__`/`__next__` elle yazılmamış.
- [ ] yield ile return farkı durma/devam edebilme üzerinden açıklanmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../9.10-generator-expressions/README.md)
<!-- learning-task:end -->
