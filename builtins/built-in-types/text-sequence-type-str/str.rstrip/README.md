## `str.rstrip`

```
str.rstrip(chars=None, /)
```

Return a copy of the string with trailing characters removed.  The *chars*
argument is a string specifying the set of characters to be removed.  If omitted
or `None`, the *chars* argument defaults to removing whitespace.  The *chars*
argument is not a suffix; rather, all combinations of its values are stripped.
For example:

``` python
>>> '   spacious   '.rstrip()
'   spacious'
>>> 'mississippi'.rstrip('ipz')
'mississ'
```
> Code: [example_01.py](example_01.py)

See `removesuffix()` for a method that will remove a single suffix
string rather than all of a set of characters.  For example:

``` python
>>> 'Monty Python'.rstrip(' Python')
'M'
>>> 'Monty Python'.removesuffix(' Python')
'Monty'
```
> Code: [example_02.py](example_02.py)

See also `strip()`.

## Çözümlü kısa örnek

Chars tek bir son ek değil karakter kümesidir

```python
print(repr(" a  ".rstrip()))
# Sonuç: ' a'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.39: str.rstrip davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; chars tek bir son ek değil karakter kümesidir

```python
"abXabba".rstrip("ab")
"abXba".rstrip("ab")
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `'abX'`; `'abX'`.
- [ ] Chars tek bir son ek değil karakter kümesidir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.split/README.md)
<!-- learning-task:end -->
