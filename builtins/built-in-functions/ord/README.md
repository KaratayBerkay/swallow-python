## `ord()`

```
ord(character, /)
```

Return the ordinal value of a character.

If the argument is a one-character string, return the Unicode code point
of that character.  For example,
`ord('a')` returns the integer `97` and `ord('€')` (Euro sign)
returns `8364`.  This is the inverse of [chr()](../chr/README.md).

If the argument is a [bytes](../bytes/README.md) or [bytearray](../bytearray/README.md) object of
length 1, return its single byte value.
For example, `ord(b'a')` returns the integer `97`.

## Çözümlü kısa örnek

Tek Unicode karakterle uzun veya boş metni ayır.

```python
print(repr(ord("A")))
# Sonuç: 65
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.52: ord davranışını ayırt et**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; tek Unicode karakterle uzun veya boş metni ayır.

```python
ord("İ")
ord("ab")
ord("")
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `304`; `TypeError`; `TypeError`.
- [ ] Tek Unicode karakterle uzun veya boş metni ayır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../pow/README.md)
<!-- learning-task:end -->
