## 5.8. Comparing Sequences and Other Types

Sequence objects typically may be compared to other objects with the same sequence type. The comparison uses *lexicographical* ordering: first the first two items are compared, and if they differ this determines the outcome of the comparison; if they are equal, the next two items are compared, and so on, until either sequence is exhausted. If two items to be compared are themselves sequences of the same type, the lexicographical comparison is carried out recursively. If all items of two sequences compare equal, the sequences are considered equal. If one sequence is an initial sub-sequence of the other, the shorter sequence is the smaller (lesser) one. Lexicographical ordering for strings uses the Unicode code point number to order individual characters. Some examples of comparisons between sequences of the same type:

``` python
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
```
> Code: [example_01.py](example_01.py)

Note that comparing objects of different types with `<` or `>` is legal provided that the objects have appropriate comparison methods. For example, mixed numeric types are compared according to their numeric value, so 0 equals 0.0, etc. Otherwise, rather than providing an arbitrary ordering, the interpreter will raise a `TypeError` exception.

<!-- learning-task:start -->
### Bölüm görevi

**Görev 5.8: Sıralamanın ilk belirleyici öğesini bul**

**Odak:** Sözlük sırası anlamındaki lexicographic karşılaştırma, önek, iç içe diziler ve tür uyumu.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:5.7](../5.7-more-on-conditions/README.md).

#### Tek görev

1. Şu karşılaştırmaların her biri için yalnız sonucu değil, sonucu belirleyen ilk öğeyi yaz: [2, 9] < [3, 0]; [2, 9] < [2, 9, -1]; (1, ("ab", "c")) < (1, ("ac", "a")); (1, 2) == (1.0, 2.0); "B" < "a"; [1, "x"] < [1, 2].

2. Sonra ifadeleri ayrı girişlerde doğrula.

#### Geçiş ölçütleri

- [ ] İlk beş sonuç doğru; sonuncu str/int sıralaması nedeniyle TypeError.
- [ ] İlk fark bulunan yerde sonraki öğelerin karşılaştırılmadığı gösterilmiş.
- [ ] Önek durumunda kısa dizi küçük; iç içe karşılaştırma yine aynı kuralla.
- [ ] Metin sırası Unicode kod noktasıyla açıklanmış, alfabetik/yerel sıralama sanılmamış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
