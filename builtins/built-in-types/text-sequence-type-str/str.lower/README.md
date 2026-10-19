## `str.lower`

```
str.lower()
```

Return a copy of the string with all the cased characters [^1] converted to
lowercase. For example:

``` python
>>> 'Lower Method Example'.lower()
'lower method example'
```
> Code: [example_01.py](example_01.py)

The lowercasing algorithm used is [described in section 3.13.2 'Default Case
Conversion' of the Unicode Standard](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-3/#G34078).

[^1]: Cased characters are those with general category property being one of "Lu" (Letter, uppercase), "Ll" (Letter, lowercase), or "Lt" (Letter, titlecase).

## Çözümlü kısa örnek

Dönüşüm yeni metni verir; yalnız cased karakterler değişir

```python
print(repr("ADA".lower()))
# Sonuç: 'ada'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.27: str.lower davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; dönüşüm yeni metni verir; yalnız cased karakterler değişir

```python
"İ A1!".lower()
"".lower()
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `'i̇ a1!'`; `''`.
- [ ] Dönüşüm yeni metni verir; yalnız cased karakterler değişir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.lstrip/README.md)
<!-- learning-task:end -->
