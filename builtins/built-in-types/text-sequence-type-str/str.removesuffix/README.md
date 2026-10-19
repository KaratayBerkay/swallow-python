## `str.removesuffix`

```
str.removesuffix(suffix, /)
```

If the string ends with the *suffix* string and that *suffix* is not empty,
return `string[:-len(suffix)]`. Otherwise, return a copy of the
original string:

``` python
>>> 'MiscTests'.removesuffix('Tests')
'Misc'
>>> 'TmpDirMixin'.removesuffix('Tests')
'TmpDirMixin'
```
> Code: [example_01.py](example_01.py)

> *Added in version 3.9.*

See also `removeprefix()` and `endswith()`.

## Çözümlü kısa örnek

Tam son ek yalnız bir kez kaldırılır; boş ek metni silmez

```python
print(repr("ad.txt".removesuffix(".txt")))
# Sonuç: 'ad'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.32: str.removesuffix davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; tam son ek yalnız bir kez kaldırılır; boş ek metni silmez

```python
"ababa".removesuffix("ba")
"abc".removesuffix("")
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `'aba'`; `'abc'`.
- [ ] Tam son ek yalnız bir kez kaldırılır; boş ek metni silmez

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.replace/README.md)
<!-- learning-task:end -->
