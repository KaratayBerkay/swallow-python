## 4.2. `for` Statements

The `for` statement in Python differs a bit from what you may be used to in C or Pascal. Rather than always iterating over an arithmetic progression of numbers (like in Pascal), or giving the user the ability to define both the iteration step and halting condition (as C), Python's `for` statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence. For example (no pun intended):

``` python
>>> # Measure some strings:
>>> words = ['cat', 'window', 'defenestrate']
>>> for w in words:
...     print(w, len(w))
...
cat 3
window 6
defenestrate 12
```
> Code: [words.py](words.py)

Code that modifies a collection while iterating over that same collection can be tricky to get right. Instead, it is usually more straight-forward to loop over a copy of the collection or to create a new collection:

``` python
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
```
> Code: [users.py](users.py)

<!-- learning-task:start -->
### Bölüm görevi

**Görev 4.2: Sırayı koruyarak bir koleksiyonu işle**

**Odak:** for ile öğeler üzerinde sırayla dolaşma ve dolaşılan koleksiyonu değiştirirken güvenli strateji.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:4.1](../4.1-if-statements/README.md).
- Ön bilgi: [t:3.1.3](../../03-an-informal-introduction-to-python/3.1-using-python-as-a-calculator/3.1.3-lists/README.md).

#### Tek görev

1. words = ["sun", "river", "a"] için her sözcüğü ve uzunluğunu for ile yazdır.

2. Sonra README içindeki users örneğini yeni bir başlangıç verisiyle izle: Ada active, Ece inactive, Can inactive.

3. Örnekteki iki stratejiyi birbirinden bağımsız başlangıç verileri üzerinde uygula ve hangi koleksiyonun değiştiğini göster.

4. Sözlük işlemleri için örneğin iskeletini kullan; burada yeni bir sözlük tekniği tasarlaman beklenmiyor.

#### Geçiş ölçütleri

- [ ] Sözcüklerin sırası korunmuş, uzunluklar 3, 5, 1.
- [ ] Kopya üzerinde dolaşma stratejisi asıl users içinde yalnızca Ada bırakıyor.
- [ ] Yeni koleksiyon stratejisi users verisini koruyup yalnızca Ada içeren active_users oluşturuyor.
- [ ] for değişkeninin indeks yerine sıradaki öğeyi aldığı ve neden aynı koleksiyondan silme yapılmadığı açıklanmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../4.3-the-range-function/README.md)
<!-- learning-task:end -->
