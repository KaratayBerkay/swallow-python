## `str.istitle`

```
str.istitle()
```

Return `True` if the string is a titlecased string and there is at least one
character, for example uppercase characters may only follow uncased characters
and lowercase characters only cased ones.  Return `False` otherwise.

For example:

``` python
>>> 'Spam, Spam, Spam'.istitle()
True
>>> 'spam, spam, spam'.istitle()
False
>>> 'SPAM, SPAM, SPAM'.istitle()
False
```
> Code: [example_01.py](example_01.py)

See also `title()`.

## Çözümlü kısa örnek

Başlık düzeni, tüm harfleri büyütmek değildir

```python
print(repr("Ada Ece".istitle()))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.24: str.istitle davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; başlık düzeni, tüm harfleri büyütmek değildir

```python
"Ada 2Ece".istitle()
"ADA".istitle()
"".istitle()
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `False`; `False`.
- [ ] Başlık düzeni, tüm harfleri büyütmek değildir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.isupper/README.md)
<!-- learning-task:end -->
