## `str.upper`

```
str.upper()
```

Return a copy of the string with all the cased characters [^1] converted to
uppercase.  Note that `s.upper().isupper()` might be `False` if `s`
contains uncased characters or if the Unicode category of the resulting
character(s) is not "Lu" (Letter, uppercase), but e.g. "Lt" (Letter,
titlecase).

The uppercasing algorithm used is [described in section 3.13.2 'Default Case
Conversion' of the Unicode Standard](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-3/#G34078).

[^1]: Cased characters are those with general category property being one of "Lu" (Letter, uppercase), "Ll" (Letter, lowercase), or "Lt" (Letter, titlecase).

## Çözümlü kısa örnek

Unicode büyütme uzunluğu artırabilir

```python
print(repr("ada".upper()))
# Sonuç: 'ADA'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.47: str.upper davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; unicode büyütme uzunluğu artırabilir

```python
"straße".upper()
"a1!".upper()
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `'STRASSE'`; `'A1!'`.
- [ ] Unicode büyütme uzunluğu artırabilir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.zfill/README.md)
<!-- learning-task:end -->
