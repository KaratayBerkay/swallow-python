## `str.lstrip`

```
str.lstrip(chars=None, /)
```

Return a copy of the string with leading characters removed.  The *chars*
argument is a string specifying the set of characters to be removed.  If omitted
or `None`, the *chars* argument defaults to removing whitespace.  The *chars*
argument is not a prefix; rather, all combinations of its values are stripped:

``` python
>>> '   spacious   '.lstrip()
'spacious   '
>>> 'www.example.com'.lstrip('cmowz.')
'example.com'
```
> Code: [example_01.py](example_01.py)

See [str.removeprefix()](../str.removeprefix/README.md) for a method that will remove a single prefix
string rather than all of a set of characters.  For example:

``` python
>>> 'Arthur: three!'.lstrip('Arthur: ')
'ee!'
>>> 'Arthur: three!'.removeprefix('Arthur: ')
'three!'
```
> Code: [example_02.py](example_02.py)

## Çözümlü kısa örnek

Chars bir önek değil karakter kümesidir; yalnız solda çalışır

```python
print(repr("  a  ".lstrip()))
# Sonuç: 'a  '
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.28: str.lstrip davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; chars bir önek değil karakter kümesidir; yalnız solda çalışır

```python
"abbaXba".lstrip("ab")
"abXab".lstrip("ab")
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `'Xba'`; `'Xab'`.
- [ ] Chars bir önek değil karakter kümesidir; yalnız solda çalışır

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.maketrans/README.md)
<!-- learning-task:end -->
