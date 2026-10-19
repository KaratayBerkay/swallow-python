## `str.isspace`

```
str.isspace()
```

Return `True` if there are only whitespace characters in the string and there is
at least one character, `False` otherwise.

For example:

``` python
>>> ''.isspace()
False
>>> ' '.isspace()
True
>>> '\t\n'.isspace() # TAB and BREAK LINE
True
>>> '\u3000'.isspace() # IDEOGRAPHIC SPACE
True
```
> Code: [example_01.py](example_01.py)

A character is *whitespace* if in the Unicode character database
(see [unicodedata](https://docs.python.org/3.15/library/unicodedata.html#module-unicodedata)), either its general category is `Zs`
("Separator, space"), or its bidirectional class is one of `WS`,
`B`, or `S`.

See also `isprintable()`.

## Çözümlü kısa örnek

En az bir karakter gerekir; Unicode boşluklar da kapsanır

```python
print(repr(" ".isspace()))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.23: str.isspace davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; en az bir karakter gerekir; Unicode boşluklar da kapsanır

```python
"\t\n".isspace()
"　".isspace()
"".isspace()
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `True`; `False`.
- [ ] En az bir karakter gerekir; Unicode boşluklar da kapsanır

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.istitle/README.md)
<!-- learning-task:end -->
