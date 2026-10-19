## `str.isidentifier`

```
str.isidentifier()
```

Return `True` if the string is a valid identifier according to the language
definition, section [Names (identifiers and keywords)](https://docs.python.org/3.15/reference/lexical_analysis.html#identifiers).

[keyword.iskeyword()](https://docs.python.org/3.15/library/keyword.html#keyword.iskeyword) can be used to test whether string `s` is a reserved
identifier, such as `def` and `class`.

Example:

``` python
>>> from keyword import iskeyword

>>> 'hello'.isidentifier(), iskeyword('hello')
(True, False)
>>> 'def'.isidentifier(), iskeyword('def')
(True, True)
```
> Code: [example_01.py](example_01.py)

## Çözümlü kısa örnek

Identifier biçimi uygun olmak, keyword olmamakla aynı değildir

```python
print(repr("ad_1".isidentifier()))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.19: str.isidentifier davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; identifier biçimi uygun olmak, keyword olmamakla aynı değildir

```python
"2ad".isidentifier()
"class".isidentifier()
"".isidentifier()
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `False`; `True`; `False`.
- [ ] Identifier biçimi uygun olmak, keyword olmamakla aynı değildir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.islower/README.md)
<!-- learning-task:end -->
