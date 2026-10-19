## `str.find`

```
str.find(sub[, start[, end]])
```

Return the lowest index in the string where substring *sub* is found within
the slice `s[start:end]`.  Optional arguments *start* and *end* are
interpreted as in slice notation.  Return `-1` if *sub* is not found.
For example:

``` python
>>> 'spam, spam, spam'.find('sp')
0
>>> 'spam, spam, spam'.find('sp', 5)
6
```
> Code: [example_01.py](example_01.py)

See also `rfind()` and `index()`.

> **Note**
>
> The find() method should be used only if you need to know the
> position of *sub*.  To check if *sub* is a substring or not, use the
> `in` operator:
>
> ``` python
> >>> 'Py' in 'Python'
> True
> ```
> > Code: [example_02.py](example_02.py)

## Çözümlü kısa örnek

Bulunamama -1 olur; bulunan indeks özgün metne aittir

```python
print(repr("ababa".find("ba")))
# Sonuç: 1
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.11: str.find davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; bulunamama -1 olur; bulunan indeks özgün metne aittir

```python
"ababa".find("ba",2)
"ababa".find("x")
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `3`; `-1`.
- [ ] Bulunamama -1 olur; bulunan indeks özgün metne aittir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.format_map/README.md)
<!-- learning-task:end -->
