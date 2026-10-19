## `str.capitalize`

```
str.capitalize()
```

Return a copy of the string with its first character capitalized and the
rest lowercased.

> *Changed in version 3.8:* The first character is now put into titlecase rather than uppercase.
> This means that characters like digraphs will only have their first
> letter capitalized, instead of the full character.

## Çözümlü kısa örnek

Yalnız ilk karakter büyür; kalan bölüm küçülür

```python
print(repr("ada".capitalize()))
# Sonuç: 'Ada'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.4: str.capitalize davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; yalnız ilk karakter büyür; kalan bölüm küçülür

```python
"pYTHON 3".capitalize()
"".capitalize()
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `'Python 3'`; `''`.
- [ ] Yalnız ilk karakter büyür; kalan bölüm küçülür

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.casefold/README.md)
<!-- learning-task:end -->
