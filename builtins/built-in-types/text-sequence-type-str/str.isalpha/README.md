## `str.isalpha`

```
str.isalpha()
```

Return `True` if all characters in the string are alphabetic and there is at least
one character, `False` otherwise.  Alphabetic characters are those characters defined
in the Unicode character database as "Letter", i.e., those with general category
property being one of "Lm", "Lt", "Lu", "Ll", or "Lo".  Note that this is different
from the [Alphabetic property defined in section 4.10 'Letters, Alphabetic, and
Ideographic' of the Unicode Standard](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-4/#G91002).
For example:

``` python
>>> 'Letters and spaces'.isalpha()
False
>>> 'LettersOnly'.isalpha()
True
>>> 'µ'.isalpha()  # non-ASCII characters can be considered alphabetical too
True
```
> Code: [example_01.py](example_01.py)

See [Unicode Properties](https://docs.python.org/3.15/howto/unicode.html#unicode-properties).

## Çözümlü kısa örnek

Unicode harfler kabul edilir; boşluk ve boş metin edilmez

```python
print(repr("ab".isalpha()))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.15: str.isalpha davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; unicode harfler kabul edilir; boşluk ve boş metin edilmez

```python
"İpek".isalpha()
"a b".isalpha()
"".isalpha()
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `False`; `False`.
- [ ] Unicode harfler kabul edilir; boşluk ve boş metin edilmez

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.isascii/README.md)
<!-- learning-task:end -->
