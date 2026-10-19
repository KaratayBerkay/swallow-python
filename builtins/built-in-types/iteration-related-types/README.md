Python supports a concept of iteration over containers.  This is implemented
using two distinct methods; these are used to allow user-defined classes to
support iteration.  Sequences, described below in more detail, always support
the iteration methods.

## Iterables

One method needs to be defined for container objects to provide [iterable](https://docs.python.org/3.15/glossary.html#term-iterable)
support:

- [`container.__iter__`](container.__iter__/README.md) — Return an iterator object.

## Iterators

The iterator objects themselves are required to support the following two
methods, which together form the iterator protocol:

- [`iterator.__iter__`](iterator.__iter__/README.md) — Return the iterator object itself.
- [`iterator.__next__`](iterator.__next__/README.md) — Return the next item from the iterator.

Python defines several iterator objects to support iteration over general and
specific sequence types, dictionaries, and other more specialized forms.  The
specific types are not important beyond their implementation of the iterator
protocol.

Once an iterator's [__next__()](iterator.__next__/README.md) method raises
[StopIteration](https://docs.python.org/3.15/builtins/exceptions.html#StopIteration), it must continue to do so on subsequent calls.
Implementations that do not obey this property are deemed broken.

## Generator types

Python's [generators](https://docs.python.org/3.15/glossary.html#term-generator) -- or more precisely,
[generator functions](https://docs.python.org/3.15/glossary.html#term-generator-function) and
[generator iterators](https://docs.python.org/3.15/glossary.html#term-generator-iterator) -- provide a convenient way
to implement the iterator protocol.

A function that contains one or more [yield expressions](https://docs.python.org/3.15/reference/expressions.html#yieldexpr)
is a [generator function](https://docs.python.org/3.15/glossary.html#term-generator-function).
For example:

``` python
>>> def count_to_three():
...     yield 0
...     yield 1
...     yield 2
...     yield 3
>>> count_to_three()
<generator object count_to_three at 0x7f33a2305000>
>>> for number in count_to_three():
...     print(number)
0
1
2
3

>>> list(count_to_three())
[0, 1, 2, 3]
```
> Code: [example_01.py](example_01.py)

Generator functions behave as regular
[user-defined functions](https://docs.python.org/3.15/reference/datamodel.html#user-defined-funcs)
(for example, they have the same attributes), except that calling a generator
function returns a [generator iterator](https://docs.python.org/3.15/builtins/stdtypes.html#generator-methods):

Iterating a generator iterator executes code of the underlying
generator function, producing each `yield`ed value in turn:

One common use for generator functions is implementing the
[__iter__()](https://docs.python.org/3.15/reference/datamodel.html#object.__iter__) method of custom iterable objects.
For example:

``` python
>>> class CardDeck:
...     def __iter__(self):
...         yield 'three of clubs'
...         yield 'ace of hearts'

>>> list(CardDeck())
['three of clubs', 'ace of hearts']
```
> Code: [example_02.py](example_02.py)

### Generator iterators

Generator iterators implement the
[iterator protocol](https://docs.python.org/3.15/builtins/stdtypes.html#stdtypes-iterators).
Iterating them drives execution of the underlying generator function.

- [`generator.__next__`](generator.__next__/README.md) — Starts the execution of a generator function or resumes it at the yield expression where the function is currently suspended.

Generator iterators have a few more methods than generic iterators, which
can be used to control the execution of the underlying generator function:

- [`generator.send`](generator.send/README.md) — "Sends" a value into the generator function: the *value* argument becomes the result of the current yield expression.
- [`generator.throw`](generator.throw/README.md) — Raises an exception at the point where the generator is currently suspended.
- [`generator.close`](generator.close/README.md) — Raises a GeneratorExit exception at the point where the generator function is currently suspended (equivalent to calling throw(GeneratorExit)).

Calling any of the generator methods ([__next__()](generator.__next__/README.md),
[send()](generator.send/README.md), [throw()](generator.throw/README.md), [close()](generator.close/README.md))
while one of these methods is already executing
raises a [ValueError](https://docs.python.org/3.15/builtins/exceptions.html#ValueError) exception.

### Asynchronous generator iterators

This subsection describes the methods of an asynchronous generator iterator,
which are used to control the execution of an asynchronous generator function.

- [`agen.__anext__`](agen.__anext__/README.md) — Returns an awaitable which when run starts to execute the asynchronous generator function or resumes it at the yield expression where the function…

Asynchronous generator-iterators have a few more methods than generic
asynchronous iterators, which can be used to control the execution of
the underlying generator function:

- [`agen.asend`](agen.asend/README.md) — Returns an awaitable which, when run, "sends" a value into the underlying asynchronous generator function: the *value* argument becomes the result…
- [`agen.athrow`](agen.athrow/README.md) — Returns an awaitable that, when run, raises an exception at the point where the underlying asynchronous generator function is currently suspended.
- [`agen.aclose`](agen.aclose/README.md) — Returns an awaitable that when run will throw a GeneratorExit into the underlying asynchronous generator function at the point where it is…

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.6: Iterator durumunu kaybetmeden tüket**

#### Önce

[b:2](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Bir [4,6] listesi, bu listeyi gezen tek iterator ve ikinci bağımsız iterator oluştur. İlk iteratordan bir öğe tüket; onu list ile tüket; yeniden tüket; ikinci iteratorı tüket. Aynı veri ile aynı tüketim durumunu ayır.

#### Geçiş ölçütleri

- [ ] Sonuçlar 4, [6], [], [4,6] olur; liste değişmez.
- [ ] Iterable veri kaynağıyla iteratorın kalan konumu ayrı nesne sorumluluklarıdır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](container.__iter__/README.md)
<!-- learning-task:end -->

<!-- learning-milestone:start -->
### Klasör milestone görevi

**Milestone: Tüketim protokolünü birleştir**

#### Önce

Bu klasördeki bütün bölüm görevleri ve alt klasör milestone kontrolleri tamamlanmış olmalı. Sırayı [görev dizininden](../../../TASKS.md) kontrol et.

#### Tek görev

Bir generator önce hazır bilgisini yield etsin, send ile aldığı sayıyı yield etsin, sonra return 9 yapsın. Oluşturma, ilk next, send, son next ve close durumlarını kaydet. Aynı işlemin async karşılıklarını, hazır verilen asend/anext sözleşmeleriyle yazılı eşleştir.

#### Geçiş ölçütleri

- [ ] Gönderilen değer yield ifadesine bağlanır; StopIteration.value=9 okunur.
- [ ] Iterator yeniden başlamaz; async awaitable oluşturma ve çalıştırma anları ayrılır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../sequence-types-list-tuple-range/README.md)
<!-- learning-milestone:end -->
