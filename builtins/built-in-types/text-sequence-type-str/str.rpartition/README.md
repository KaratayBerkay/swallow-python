## `str.rpartition`

```
str.rpartition(sep, /)
```

Split the string at the last occurrence of *sep*, and return a 3-tuple
containing the part before the separator, the separator itself, and the part
after the separator.  If the separator is not found, return a 3-tuple containing
two empty strings, followed by the string itself.

For example:

``` python
>>> 'Monty Python'.rpartition(' ')
('Monty', ' ', 'Python')
>>> "Monty Python's Flying Circus".rpartition(' ')
("Monty Python's Flying", ' ', 'Circus')
>>> 'Monty Python'.rpartition('-')
('', '', 'Monty Python')
```
> Code: [example_01.py](example_01.py)

See also `partition()`.

## Çözümlü kısa örnek

Sağdaki ayırıcı seçilir; bulunamazsa özgün metin son parçadır

```python
print(repr("a=b".rpartition("=")))
# Sonuç: ('a', '=', 'b')
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.37: str.rpartition davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; sağdaki ayırıcı seçilir; bulunamazsa özgün metin son parçadır

```python
"a=b=c".rpartition("=")
"abc".rpartition("=")
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `('a=b', '=', 'c')`; `('', '', 'abc')`.
- [ ] Sağdaki ayırıcı seçilir; bulunamazsa özgün metin son parçadır

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.rsplit/README.md)
<!-- learning-task:end -->
