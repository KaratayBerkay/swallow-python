## 5.6. Looping Techniques

When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the `items()` method.

``` python
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave
```
> Code: [knights.py](knights.py)

When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the `enumerate()` function.

``` python
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe
```
> Code: [example_01.py](example_01.py)

To loop over two or more sequences at the same time, the entries can be paired with the `zip()` function.

``` python
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
```
> Code: [questions.py](questions.py)

To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the `reversed()` function.

``` python
>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1
```
> Code: [example_02.py](example_02.py)

To loop over a sequence in sorted order, use the `sorted()` function which returns a new sorted list while leaving the source unaltered.

``` python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for i in sorted(basket):
...     print(i)
...
apple
apple
banana
orange
orange
pear
```
> Code: [basket.py](basket.py)

Using `set()` on a sequence eliminates duplicate elements. The use of `sorted()` in combination with `set()` over a sequence is an idiomatic way to loop over unique elements of the sequence in sorted order.

``` python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print(f)
...
apple
banana
orange
pear
```
> Code: [basket_2.py](basket_2.py)

It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to create a new list instead.

``` python
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...     if not math.isnan(value):
...         filtered_data.append(value)
...
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]
```
> Code: [raw_data.py](raw_data.py)

<!-- learning-task:start -->
### Bölüm görevi

**Görev 5.6: Aynı veriden farklı dolaşım görünümleri üret**

**Odak:** items, enumerate, zip, reversed, sorted/set ve kaynak üzerinde değişiklik yapmadan filtreleme.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:5.5](../5.5-dictionaries/README.md).

#### Tek görev

1. names = ["Ece", "Ada", "Ada"], scores = [8, 5, 9] ve rooms = {"Ada": "A1", "Ece": "B2"} ile küçük rapor oluştur. enumerate ile sıra numarası/ad, zip ile ad/puan, items ile ad/oda satırlarını bas.

2. Adları tersten ve tekrarsız sıralı biçimde ayrıca göster.

3. README içindeki NaN filtreleme iskeletini [2.0, float("NaN"), 4.0] için kullan; kaynak listenin korunmasını kontrol et.

#### Geçiş ölçütleri

- [ ] enumerate indeksleri 0, 1, 2; zip çiftleri Ece-8, Ada-5, Ada-9.
- [ ] items her anahtarı kendi değeriyle eşleştiriyor.
- [ ] Tersten görünüm Ada, Ada, Ece; tekrarsız sıralı görünüm Ada, Ece. Kaynak liste Ece, Ada, Ada olarak korunmuş.
- [ ] Filtre [2.0, 4.0] oluşturuyor; asıl veri değiştirilmemiş.
- [ ] Dolaşma araçlarının her birinin hangi eşleştirme ihtiyacını karşıladığı açıklanmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../5.7-more-on-conditions/README.md)
<!-- learning-task:end -->
