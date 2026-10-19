### 4.9.6. Lambda Expressions

Small anonymous functions can be created with the `lambda` keyword. This function returns the sum of its two arguments: `lambda a, b: a+b`. Lambda functions can be used wherever function objects are required. They are syntactically restricted to a single expression. Semantically, they are just syntactic sugar for a normal function definition. Like nested function definitions, lambda functions can reference variables from the containing scope:

``` python
>>> def make_incrementor(n):
...     return lambda x: x + n
...
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43
```
> Code: [make_incrementor.py](make_incrementor.py)

The above example uses a lambda expression to return a function. Another use is to pass a small function as an argument. For instance, `list.sort()` takes a sorting key function *key* which can be a lambda function:

``` python
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```
> Code: [pairs.py](pairs.py)

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 4.9.6: Küçük bir işlevi değer olarak taşı**

**Odak:** Tek ifadeli lambda, dış kapsamı kullanma ve key işleviyle sıralama.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:4.9.5](../4.9.5-unpacking-argument-lists/README.md).

##### Tek görev

1. make_adder(n) fonksiyonundan x değerine n ekleyen lambda döndür; n=3 ve n=8 ile iki işlev oluşturup aynı x=2 girdisiyle çağır.

2. Sonra pairs = [(1, "pear"), (2, "apple"), (3, "fig")] listesini ikinci öğeye göre lambda key kullanarak sırala. lambda ile eşdeğer normal def biçimini yaz.

##### Geçiş ölçütleri

- [ ] İki işlev 5 ve 10 döndürüyor, oluşturuldukları n değerleriyle ilişkileri açıklanmış.
- [ ] Sıralama apple, fig, pear adlarına göre; sayısal ilk öğeler anahtar olarak kullanılmamış.
- [ ] lambda gövdesi tek ifade; key parametresine çağrı sonucu yerine işlev nesnesi verilmiş.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../4.9.7-documentation-strings/README.md)
<!-- learning-task:end -->
