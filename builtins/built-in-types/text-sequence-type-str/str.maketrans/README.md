## `str.maketrans`

```
str.maketrans(dict, /)
str.maketrans(from, to, remove='', /)
```

This static method returns a translation table usable for [str.translate()](../str.translate/README.md).

If there is only one argument, it must be a dictionary mapping Unicode
ordinals (integers) or characters (strings of length 1) to Unicode ordinals,
strings (of arbitrary lengths) or `None`.  Character keys will then be
converted to ordinals.

If there are two arguments, they must be strings of equal length, and in the
resulting dictionary, each character in *from* will be mapped to the character at
the same position in *to*.  If there is a third argument, it must be a string,
whose characters will be mapped to `None` in the result.

> *Changed in version 3.15:* *dict* can now be a [frozendict](../../mapping-types-dict-frozendict/frozendict/README.md).

## Çözümlü kısa örnek

Tablo anahtarları ord olur; eşleştirme, silme ve uzunluk şartını ayır

```python
print(repr(str.maketrans("a","x")[ord("a")]))
# Sonuç: 120
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.29: str.maketrans davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

Sürüm: Python 3.15+ frozendict kabulü eski sürümde yalnız gerekçeli yazılı iz ile incelenebilir; temel dict/metin denemelerini çalıştır.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; tablo anahtarları ord olur; eşleştirme, silme ve uzunluk şartını ayır

```python
str.maketrans({"a":"XY","b":None})
str.maketrans("ab","x")
```

Üç argümanlı biçimde `str.maketrans("ab","xy","!")` oluştur; hangi anahtarların hangi değerlere bağlandığını göster. Python 3.15+ aynı tek argümanlı tabloyu frozendict ile oluşturma davranışını yazılı olarak incele.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `{97: 'XY', 98: None}`; `ValueError`.
- [ ] Tablo anahtarları ord olur; eşleştirme, silme ve uzunluk şartını ayır

- [ ] 97->120, 98->121, 33->None eşlemesi vardır; üç argümanlı biçim silme tablosu da üretir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.partition/README.md)
<!-- learning-task:end -->
