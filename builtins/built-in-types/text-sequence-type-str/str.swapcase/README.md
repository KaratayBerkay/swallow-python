## `str.swapcase`

```
str.swapcase()
```

Return a copy of the string with uppercase characters converted to lowercase and
vice versa. For example:

``` python
>>> 'Hello World'.swapcase()
'hELLO wORLD'
```
> Code: [example_01.py](example_01.py)

Note that it is not necessarily true that `s.swapcase().swapcase() == s`.
For example:

``` python
>>> 'straße'.swapcase().swapcase()
'strasse'
```
> Code: [example_02.py](example_02.py)

See also [str.lower()](../str.lower/README.md) and [str.upper()](../str.upper/README.md).

## Çözümlü kısa örnek

Unicode case dönüşümü her zaman tersinir değildir

```python
print(repr("aB".swapcase()))
# Sonuç: 'Ab'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.44: str.swapcase davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; unicode case dönüşümü her zaman tersinir değildir

```python
"Groß".swapcase()
"ß".swapcase().swapcase()=="ß"
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `'gROSS'`; `False`.
- [ ] Unicode case dönüşümü her zaman tersinir değildir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.title/README.md)
<!-- learning-task:end -->
