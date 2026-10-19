## `str.partition`

```
str.partition(sep, /)
```

Split the string at the first occurrence of *sep*, and return a 3-tuple
containing the part before the separator, the separator itself, and the part
after the separator.  If the separator is not found, return a 3-tuple containing
the string itself, followed by two empty strings.

For example:

``` python
>>> 'Monty Python'.partition(' ')
('Monty', ' ', 'Python')
>>> "Monty Python's Flying Circus".partition(' ')
('Monty', ' ', "Python's Flying Circus")
>>> 'Monty Python'.partition('-')
('Monty Python', '', '')
```
> Code: [example_01.py](example_01.py)

See also `rpartition()`.

## Çözümlü kısa örnek

İlk eşleşmede üç parça döner; bulunmama sabit üçlüdür

```python
print(repr("a=b".partition("=")))
# Sonuç: ('a', '=', 'b')
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.30: str.partition davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; i̇lk eşleşmede üç parça döner; bulunmama sabit üçlüdür

```python
"a=b=c".partition("=")
"abc".partition("=")
"abc".partition("")
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `('a', '=', 'b=c')`; `('abc', '', '')`; `ValueError`.
- [ ] İlk eşleşmede üç parça döner; bulunmama sabit üçlüdür

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.removeprefix/README.md)
<!-- learning-task:end -->
