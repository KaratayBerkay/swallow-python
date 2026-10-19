## `enumerate()`

```
enumerate(iterable, start=0)
```

Return an enumerate object. *iterable* must be a sequence, an
[iterator](https://docs.python.org/3.15/glossary.html#term-iterator), or some other object which supports iteration.
The [__next__()](https://docs.python.org/3.15/builtins/stdtypes.html#iterator.__next__) method of the iterator returned by
enumerate() returns a tuple containing a count (from *start* which
defaults to 0) and the values obtained from iterating over *iterable*.

``` python
>>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
```
> Code: [example_01.py](example_01.py)

Equivalent to:

``` python
def enumerate(iterable, start=0):
    n = start
    for elem in iterable:
        yield n, elem
        n += 1
```

## Çözümlü kısa örnek

Başlangıç sayacı veri sırasını değiştirmez.

```python
print(repr(list(enumerate(["x","y"]))))
# Sonuç: [(0, 'x'), (1, 'y')]
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.21: enumerate davranışını ayırt et**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; başlangıç sayacı veri sırasını değiştirmez.

```python
list(enumerate(["a","b"],start=4))
list(enumerate([]))
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `[(4, 'a'), (5, 'b')]`; `[]`.
- [ ] Başlangıç sayacı veri sırasını değiştirmez.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../eval/README.md)
<!-- learning-task:end -->
