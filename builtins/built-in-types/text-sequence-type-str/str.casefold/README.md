## `str.casefold`

```
str.casefold()
```

Return a casefolded copy of the string. Casefolded strings may be used for
caseless matching.

Casefolding is similar to lowercasing but more aggressive because it is
intended to remove all case distinctions in a string. For example, the German
lowercase letter `'ß'` is equivalent to `"ss"`. Since it is already
lowercase, `lower()` would do nothing to `'ß'`; `casefold()`
converts it to `"ss"`.
For example:

``` python
>>> 'straße'.lower()
'straße'
>>> 'straße'.casefold()
'strasse'
```
> Code: [example_01.py](example_01.py)

The casefolding algorithm is [described in section 3.13.3 'Default Case
Folding' of the Unicode Standard](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-3/#G53253).

> *Added in version 3.3.*

## Çözümlü kısa örnek

Unicode casefold, lower ile aynı dönüşüm değildir

```python
print(repr("Ada".casefold()))
# Sonuç: 'ada'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.5: str.casefold davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; unicode casefold, lower ile aynı dönüşüm değildir

```python
"GROSS".casefold()
"Groß".casefold()
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `'gross'`; `'gross'`.
- [ ] Unicode casefold, lower ile aynı dönüşüm değildir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.center/README.md)
<!-- learning-task:end -->
