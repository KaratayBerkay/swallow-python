## `str.center`

```
str.center(width, fillchar=' ', /)
```

Return centered in a string of length *width*. Padding is done using the
specified *fillchar* (default is an ASCII space). The original string is
returned if *width* is less than or equal to `len(s)`.  For example:

``` python
>>> 'Python'.center(10)
'  Python  '
>>> 'Python'.center(10, '-')
'--Python--'
>>> 'Python'.center(4)
'Python'
```
> Code: [example_01.py](example_01.py)

## Çözümlü kısa örnek

Genişlik alt sınırdır; dolgu tek karakter olmalıdır

```python
print(repr("ab".center(4,"-")))
# Sonuç: '-ab-'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.6: str.center davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; genişlik alt sınırdır; dolgu tek karakter olmalıdır

```python
"ab".center(2,"-")
"ab".center(6,"--")
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `'ab'`; `TypeError`.
- [ ] Genişlik alt sınırdır; dolgu tek karakter olmalıdır

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.count/README.md)
<!-- learning-task:end -->
