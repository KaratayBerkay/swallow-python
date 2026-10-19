## `tuple`

```
tuple(iterable=(), /)
```

Tuples may be constructed in a number of ways:

- Using a pair of parentheses to denote the empty tuple: `()`

- Using a trailing comma for a singleton tuple: `a,` or `(a,)`

- Separating items with commas: `a, b, c` or `(a, b, c)`

- Using the [tuple()](../../../built-in-functions/tuple/README.md) built-in: `tuple()` or `tuple(iterable)`

The constructor builds a tuple whose items are the same and in the same
order as *iterable*'s items.  *iterable* may be either a sequence, a
container that supports iteration, or an iterator object.  If *iterable*
is already a tuple, it is returned unchanged. For example,
`tuple('abc')` returns `('a', 'b', 'c')` and
`tuple( [1, 2, 3] )` returns `(1, 2, 3)`.
If no argument is given, the constructor creates a new empty tuple, `()`.

Note that it is actually the comma which makes a tuple, not the parentheses.
The parentheses are optional, except in the empty tuple case, or
when they are needed to avoid syntactic ambiguity. For example,
`f(a, b, c)` is a function call with three arguments, while
`f((a, b, c))` is a function call with a 3-tuple as the sole argument.

Tuples implement all of the [common](https://docs.python.org/3.15/builtins/stdtypes.html#typesseq-common) sequence
operations.

Tuples are [generic](https://docs.python.org/3.15/library/typing.html#generics) over the types of their contents.
For more information, refer to
[the typing documentation on annotating tuples](https://docs.python.org/3.15/library/typing.html#annotating-tuples).

## Çözümlü kısa örnek

Tuple kurma ile parantez kullanma aynı şey değildir

```python
t=(1,2)
print(repr(tuple([1,2])))
# Sonuç: (1, 2)
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.7.1: tuple davranışını ayırt et**

#### Önce

[b:2.7](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; tuple kurma ile parantez kullanma aynı şey değildir

```python
t=(1,2)
type((7,)) is tuple
type((7)) is int
tuple(t) is t
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `True`; `True`.
- [ ] Tuple kurma ile parantez kullanma aynı şey değildir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../list/README.md)
<!-- learning-task:end -->
