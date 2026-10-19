## `str.join`

```
str.join(iterable, /)
```

Return a string which is the concatenation of the strings in *iterable*.
A [TypeError](https://docs.python.org/3.15/builtins/exceptions.html#TypeError) will be raised if there are any non-string values in
*iterable*, including [bytes](../../binary-sequence-types-bytes-bytearray-memoryview/bytes/README.md) objects.  The separator between
elements is the string providing this method. For example:

``` python
>>> ', '.join(['spam', 'spam', 'spam'])
'spam, spam, spam'
>>> '-'.join('Python')
'P-y-t-h-o-n'
```
> Code: [example_01.py](example_01.py)

See also `split()`.

## Çözümlü kısa örnek

Ayırıcı öğeler arasına girer; öğeler metin olmalıdır

```python
print(repr("-".join(["a","b"])))
# Sonuç: 'a-b'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.2: str.join davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ayırıcı öğeler arasına girer; öğeler metin olmalıdır

```python
"|".join([])
"|".join(["a"])
"|".join(["a",2])
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `''`; `'a'`; `TypeError`.
- [ ] Ayırıcı öğeler arasına girer; öğeler metin olmalıdır

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.format/README.md)
<!-- learning-task:end -->
