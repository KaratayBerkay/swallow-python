## `iter()`

```
iter(iterable, /)
iter(callable, sentinel, /)
```

Return an [iterator](https://docs.python.org/3.15/glossary.html#term-iterator) object.  The first argument is interpreted very
differently depending on the presence of the second argument. Without a
second argument, the single argument must be a collection object which supports the
[iterable](https://docs.python.org/3.15/glossary.html#term-iterable) protocol (the [__iter__()](https://docs.python.org/3.15/reference/datamodel.html#object.__iter__) method),
or it must support
the sequence protocol (the [__getitem__()](https://docs.python.org/3.15/reference/datamodel.html#object.__getitem__) method with integer arguments
starting at `0`).  If it does not support either of those protocols,
[TypeError](https://docs.python.org/3.15/builtins/exceptions.html#TypeError) is raised. If the second argument, *sentinel*, is given,
then the first argument must be a callable object.  The iterator created in this case
will call *callable* with no arguments for each call to its
[__next__()](https://docs.python.org/3.15/builtins/stdtypes.html#iterator.__next__) method; if the value returned is equal to
*sentinel*, [StopIteration](https://docs.python.org/3.15/builtins/exceptions.html#StopIteration) will be raised, otherwise the value will
be returned.

See also [Iteration-related types](https://docs.python.org/3.15/builtins/stdtypes.html#typeiter).

One useful application of the second form of iter() is to build a
block-reader. For example, reading fixed-width blocks from a binary
database file until the end of file is reached:

``` python
from functools import partial
with open('mydata.db', 'rb') as f:
    for block in iter(partial(f.read, 64), b''):
        process_block(block)
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.40: iter sözleşmesini uygula**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

`it=iter([4,6])` için `iter(it) is it` kontrolünü ve tüketim sırasını göster. Ayrı olarak 4,6,"SON",8 döndüren hazır çağrılabilir bir fonksiyon verildiğini varsay; `iter(f,"SON")` hangi öğeleri verir?

#### Geçiş ölçütleri

- [ ] İlk iterator kendisini döndürür; 4 ve 6 sonrasında tükenir.
- [ ] İki argümanlı biçim 4 ve 6 verir, sentinel öğesini vermez; sonraki 8 için f çağrılmaz.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../len/README.md)
<!-- learning-task:end -->
