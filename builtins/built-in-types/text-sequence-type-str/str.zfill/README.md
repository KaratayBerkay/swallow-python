## `str.zfill`

```
str.zfill(width, /)
```

Return a copy of the string left filled with ASCII `'0'` digits to
make a string of length *width*. A leading sign prefix (`'+'`/`'-'`)
is handled by inserting the padding *after* the sign character rather
than before. The original string is returned if *width* is less than
or equal to `len(s)`.

For example:

``` python
>>> "42".zfill(5)
'00042'
>>> "-42".zfill(5)
'-0042'
```
> Code: [example_01.py](example_01.py)

See also `rjust()`.

## Çözümlü kısa örnek

Sıfırlar işaretten sonra eklenir; kısa genişlik kesmez

```python
print(repr("42".zfill(4)))
# Sonuç: '0042'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.48: str.zfill davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; sıfırlar işaretten sonra eklenir; kısa genişlik kesmez

```python
"-7".zfill(4)
"+7".zfill(4)
"123".zfill(2)
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `'-007'`; `'+007'`; `'123'`.
- [ ] Sıfırlar işaretten sonra eklenir; kısa genişlik kesmez

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
