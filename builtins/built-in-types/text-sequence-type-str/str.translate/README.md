## `str.translate`

```
str.translate(table, /)
```

Return a copy of the string in which each character has been mapped through
the given translation table.  The table must be an object that implements
indexing via [__getitem__()](https://docs.python.org/3.15/reference/datamodel.html#object.__getitem__), typically a [mapping](https://docs.python.org/3.15/glossary.html#term-mapping) or
[sequence](https://docs.python.org/3.15/glossary.html#term-sequence).  When indexed by a Unicode ordinal (an integer), the
table object can do any of the following: return a Unicode ordinal or a
string, to map the character to one or more other characters; return
`None`, to delete the character from the return string; or raise a
[LookupError](https://docs.python.org/3.15/builtins/exceptions.html#LookupError) exception, to map the character to itself.

You can use [str.maketrans()](../str.maketrans/README.md) to create a translation map from
character-to-character mappings in different formats.

The following example uses a mapping to replace `'a'` with `'X'`,
`'b'` with `'Y'`, and delete `'c'`:

``` python
>>> 'abc123'.translate({ord('a'): 'X', ord('b'): 'Y', ord('c'): None})
'XY123'
```
> Code: [example_01.py](example_01.py)

See also the [codecs](https://docs.python.org/3.15/library/codecs.html#module-codecs) module for a more flexible approach to custom
character mappings.

## Çözümlü kısa örnek

Tabloda eksik karakter korunur; None siler; metin birden çok karaktere dönüşebilir

```python
print(repr("ab".translate({ord("a"):"X"})))
# Sonuç: 'Xb'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.46: str.translate davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; tabloda eksik karakter korunur; None siler; metin birden çok karaktere dönüşebilir

```python
"abca".translate({ord("a"):"XY",ord("b"):None})
"abc".translate({})
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `'XYcXY'`; `'abc'`.
- [ ] Tabloda eksik karakter korunur; None siler; metin birden çok karaktere dönüşebilir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.upper/README.md)
<!-- learning-task:end -->
