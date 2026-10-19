### 4.9.2. Keyword Arguments

Functions can also be called using keyword arguments of the form `kwarg=value`. For instance, the following function:

``` python
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
```
> Code: [parrot.py](parrot.py)

accepts one required argument (`voltage`) and three optional arguments (`state`, `action`, and `type`). This function can be called in any of the following ways:

``` python
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
```
> Code: [example_01.py](example_01.py)

but all the following calls would be invalid:

``` python
parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument
```
> Code: [example_02.py](example_02.py)

In a function call, keyword arguments must follow positional arguments. All the keyword arguments passed must match one of the arguments accepted by the function (e.g. `actor` is not a valid argument for the `parrot` function), and their order is not important. This also includes non-optional arguments (e.g. `parrot(voltage=1000)` is valid too). No argument may receive a value more than once. Here's an example that fails due to this restriction:

``` python
>>> def function(a):
...     pass
...
>>> function(0, a=0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: function() got multiple values for argument 'a'
```
> Code: [function.py](function.py)

When a final formal parameter of the form `**name` is present, it receives a dictionary (see Mapping types --- dict, frozendict) containing all keyword arguments except for those corresponding to a formal parameter. This may be combined with a formal parameter of the form `*name` (described in the next subsection) which receives a tuple containing the positional arguments beyond the formal parameter list. (`*name` must occur before `**name`.) For example, if we define a function like this:

``` python
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
```
> Code: [cheeseshop.py](cheeseshop.py)

It could be called like this:

``` python
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
```
> Code: [shopkeeper.py](shopkeeper.py)

and of course it would print:

``` text
-- Do you have any Limburger ?
-- I'm sorry, we're all out of Limburger
It's very runny, sir.
It's really very, VERY runny, sir.
----------------------------------------
shopkeeper : Michael Palin
client : John Cleese
sketch : Cheese Shop Sketch
```

Note that the order in which the keyword arguments are printed is guaranteed to match the order in which they were provided in the function call.

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 4.9.2: Çağrıdaki değerleri parametrelere bağla**

**Odak:** Konumsal/anahtar kelimeli argüman, varsayılan, eksik/tekrar/bilinmeyen argüman ve `*arguments`/`**keywords`.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:4.9.1](../4.9.1-default-argument-values/README.md).

##### Tek görev

1. def label(name, color="blue", size=1) imzasına print(name, color, size) gövdesi ver. name değeri "box", color değeri "red", size değeri 2 olacak üç farklı geçerli çağrı yaz.

2. Sonra eksik zorunlu argüman, tekrarlı name, bilinmeyen anahtar ve anahtardan sonra konumsal argüman içeren birer geçersiz çağrıyı ayrı girişlerde dene.

3. README içindeki cheeseshop iskeletine iki ek konumsal ve iki ek anahtarlı değer vererek hangi gruba gittiklerini izle.

##### Geçiş ölçütleri

- [ ] Üç geçerli çağrı aynı değerleri doğru parametreye bağlıyor; anahtarların sırası sonucu değiştirmiyor.
- [ ] Geçersiz çağrıların her birinin hangi bağlama kuralını bozduğu açıklanmış.
- [ ] `*arguments` fazladan konumsalları, `**keywords` fazladan anahtarları topluyor.
- [ ] Anahtarlı eklerin yazdırılma sırası çağrıda verilme sırasıyla eşleşiyor.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../4.9.3-special-parameters/README.md)
<!-- learning-task:end -->
