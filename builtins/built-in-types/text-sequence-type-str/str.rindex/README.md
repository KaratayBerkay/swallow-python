## `str.rindex`

```
str.rindex(sub[, start[, end]])
```

Like `rfind()` but raises [ValueError](https://docs.python.org/3.15/builtins/exceptions.html#ValueError) when the substring *sub* is not
found.
For example:

``` python
>>> 'spam, spam, spam'.rindex('spam')
12
>>> 'spam, spam, spam'.rindex('eggs')
Traceback (most recent call last):
  File "<stdin-0>", line 1, in <module>
    'spam, spam, spam'.rindex('eggs')
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^
ValueError: substring not found
```
> Code: [example_01.py](example_01.py)

See also `index()` and `find()`.

## Çözümlü kısa örnek

Sağdan arama bulunamazsa ValueError verir

```python
print(repr("ababa".rindex("ba")))
# Sonuç: 3
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.35: str.rindex davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; sağdan arama bulunamazsa ValueError verir

```python
"ababa".rindex("ba",0,4)
"abc".rindex("x")
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `1`; `ValueError`.
- [ ] Sağdan arama bulunamazsa ValueError verir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.rjust/README.md)
<!-- learning-task:end -->
