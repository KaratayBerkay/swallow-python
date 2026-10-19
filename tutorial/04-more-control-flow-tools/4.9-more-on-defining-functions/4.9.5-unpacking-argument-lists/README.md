### 4.9.5. Unpacking Argument Lists

The reverse situation occurs when the arguments are already in a list or tuple but need to be unpacked for a function call requiring separate positional arguments. For instance, the built-in `range()` function expects separate *start* and *stop* arguments. If they are not available separately, write the function call with the `*`-operator to unpack the arguments out of a list or tuple:

``` python
>>> list(range(3, 6))            # normal call with separate arguments
[3, 4, 5]
>>> args = [3, 6]
>>> list(range(*args))            # call with arguments unpacked from a list
[3, 4, 5]
```
> Code: [args.py](args.py)

In the same fashion, dictionaries can deliver keyword arguments with the `**`-operator:

``` python
>>> def parrot(voltage, state='a stiff', action='voom'):
...     print("-- This parrot wouldn't", action, end=' ')
...     print("if you put", voltage, "volts through it.", end=' ')
...     print("E's", state, "!")
...
>>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
>>> parrot(**d)
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
```
> Code: [parrot.py](parrot.py)

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 4.9.5: Hazır argümanları çağrıda aç**

**Odak:** Çağrıda * ile konumsalları, ** ile anahtarlı değerleri açma; tanımdaki toplama ile farkı.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:4.9.4](../4.9.4-arbitrary-argument-lists/README.md).
- Ön bilgi: [t:4.3](../../4.3-the-range-function/README.md).

##### Tek görev

1. bounds = [2, 9, 3] verisini tek tek indekslemeden range çağrısına geçir ve listeye dönüştür.

2. Sonra README içindeki parrot iskeletini kullanarak voltage, state ve action değerlerini bir sözlükten ** ile geçir.

3. Aynı çağrıya voltage değerini ayrıca verince olanı ayrı girişte dene.

##### Geçiş ölçütleri

- [ ] Aralık sonucu [2, 5, 8].
- [ ] Sözlük anahtarları parametre adlarına bağlanmış, veriler tek tek kopyalanmamış.
- [ ] voltage tekrar verildiğinde çift bağlama hatası açıklanmış.
- [ ] Tanımdaki `*args` toplar, çağrıdaki `*args` açar ayrımı yapılmış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../4.9.6-lambda-expressions/README.md)
<!-- learning-task:end -->
