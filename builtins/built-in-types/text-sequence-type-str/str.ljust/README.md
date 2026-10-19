## `str.ljust`

```
str.ljust(width, fillchar=' ', /)
```

Return the string left justified in a string of length *width*. Padding is
done using the specified *fillchar* (default is an ASCII space). The
original string is returned if *width* is less than or equal to `len(s)`.

For example:

``` python
>>> 'Python'.ljust(10)
'Python    '
>>> 'Python'.ljust(10, '.')
'Python....'
>>> 'Monty Python'.ljust(10, '.')
'Monty Python'
```
> Code: [example_01.py](example_01.py)

See also `rjust()`.

## Çözümlü kısa örnek

Genişlik küçülünce metin kesilmez; dolgu sağa eklenir

```python
print(repr("ab".ljust(4,".")))
# Sonuç: 'ab..'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.26: str.ljust davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; genişlik küçülünce metin kesilmez; dolgu sağa eklenir

```python
"ab".ljust(1,".")
"ab".ljust(4,"..")
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `'ab'`; `TypeError`.
- [ ] Genişlik küçülünce metin kesilmez; dolgu sağa eklenir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.lower/README.md)
<!-- learning-task:end -->
