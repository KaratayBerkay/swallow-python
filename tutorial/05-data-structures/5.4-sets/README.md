## 5.4. Sets

Python also includes a data type for sets. A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

Curly braces or the `set()` function can be used to create sets. Note: to create an empty set you have to use `set()`, not `{}`; the latter creates an empty dictionary, a data structure that we discuss in the next section.

Because sets are unordered, iterating over them or printing them can produce the elements in a different order than you expect.

Here is a brief demonstration:

``` python
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # fast membership testing
True
>>> 'crabgrass' in basket
False

>>> # Demonstrate set operations on unique letters from two words
>>>
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
```
> Code: [basket.py](basket.py)

Similarly to list comprehensions, set comprehensions are also supported, including comprehensions with unpacking:

``` python
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}

>>> fruits = [{'apple', 'avocado', 'apricot'}, {'banana', 'blueberry'}]
>>> {*fruit for fruit in fruits}
{'blueberry', 'banana', 'avocado', 'apple', 'apricot'}
```
> Code: [a.py](a.py)

<!-- learning-task:start -->
### Bölüm görevi

**Görev 5.4: İki grubun ortak ve farklı üyelerini bul**

**Odak:** Tekrarsız ve sırasız set, üyelik, fark/birleşim/kesişim/simetrik fark ve comprehension.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:5.3](../5.3-tuples-and-sequences/README.md).
- Ön bilgi: [t:5.1.5](../5.1-more-on-lists/5.1.5-unpacking-in-lists-and-list-comprehensions/README.md).

**Kaynak/ortam notu:** Son unpacking comprehension Python 3.15 gerektirir; diğer işlemler Python 3.11 ile uygulanabilir. Son kısım eski yorumlayıcıda yazılı iz sürmedir.

#### Tek görev

1. a = set("banana"), b = set("band") için ortak, yalnız a içinde, iki gruptan herhangi birinde ve yalnız birinde olan harfleri hesapla. a içinden n harfini dışlayan set comprehension yaz.

2. Boş set ile {} farkını belirt.

3. Son olarak [{"a", "b"}, {"b", "c"}] için bölümde gösterilen unpacking comprehension sonucunu yazılı olarak çıkar.

#### Geçiş ölçütleri

- [ ] Kesişim {a, b, n}; a-b boş; birleşim {a, b, n, d}; simetrik fark {d}, öğe sırası önemsenmemiş.
- [ ] Filtre sonucu {a, b}; n üyeliği ile d üyeliği doğru.
- [ ] Boş set set() ile kurulmuş, {} sözlük olarak ayrılmış.
- [ ] Açılan gruplar tekrarsız {a, b, c} üretir; metin sırası üzerinden set sırası çıkarılmamış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../5.5-dictionaries/README.md)
<!-- learning-task:end -->
