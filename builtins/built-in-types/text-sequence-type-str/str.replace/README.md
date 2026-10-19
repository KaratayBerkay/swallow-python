## `str.replace`

```
str.replace(old, new, /, count=-1)
```

Return a copy of the string with all occurrences of substring *old* replaced by
*new*.  If *count* is given, only the first *count* occurrences are replaced.
If *count* is not specified or `-1`, then all occurrences are replaced.
For example:

``` python
>>> 'spam, spam, spam'.replace('spam', 'eggs')
'eggs, eggs, eggs'
>>> 'spam, spam, spam'.replace('spam', 'eggs', 1)
'eggs, spam, spam'
```
> Code: [example_01.py](example_01.py)

> *Changed in version 3.13:* *count* is now supported as a keyword argument.

## Çözümlü kısa örnek

Count sınırı ve özgün metnin korunmasını açıkla

```python
print(repr("aba".replace("a","x")))
# Sonuç: 'xbx'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.33: str.replace davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; count sınırı ve özgün metnin korunmasını açıkla

```python
"aaaa".replace("aa","x",1)
"abc".replace("z","x")
"abc".replace("a","x",0)
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `'xaa'`; `'abc'`; `'abc'`.
- [ ] Count sınırı ve özgün metnin korunmasını açıkla

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.rfind/README.md)
<!-- learning-task:end -->
