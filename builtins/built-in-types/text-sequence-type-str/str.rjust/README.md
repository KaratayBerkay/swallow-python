## `str.rjust`

```
str.rjust(width, fillchar=' ', /)
```

Return the string right justified in a string of length *width*. Padding is
done using the specified *fillchar* (default is an ASCII space). The
original string is returned if *width* is less than or equal to `len(s)`.

For example:

``` python
>>> 'Python'.rjust(10)
'    Python'
>>> 'Python'.rjust(10, '.')
'....Python'
>>> 'Monty Python'.rjust(10, '.')
'Monty Python'
```
> Code: [example_01.py](example_01.py)

See also `ljust()` and `zfill()`.

## Çözümlü kısa örnek

Dolgu sola eklenir; kısa genişlik kesme yapmaz

```python
print(repr("ab".rjust(4,".")))
# Sonuç: '..ab'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.36: str.rjust davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; dolgu sola eklenir; kısa genişlik kesme yapmaz

```python
"ab".rjust(1,".")
"ab".rjust(4,"..")
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `'ab'`; `TypeError`.
- [ ] Dolgu sola eklenir; kısa genişlik kesme yapmaz

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.rpartition/README.md)
<!-- learning-task:end -->
