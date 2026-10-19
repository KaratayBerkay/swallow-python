## `str.removeprefix`

```
str.removeprefix(prefix, /)
```

If the string starts with the *prefix* string, return
`string[len(prefix):]`. Otherwise, return a copy of the original
string:

``` python
>>> 'TestHook'.removeprefix('Test')
'Hook'
>>> 'BaseTestCase'.removeprefix('Test')
'BaseTestCase'
```
> Code: [example_01.py](example_01.py)

> *Added in version 3.9.*

See also `removesuffix()` and `startswith()`.

## Çözümlü kısa örnek

Yalnız tam bir önek kaldırılır; karakter kümesi gibi davranmaz

```python
print(repr("pre-ad".removeprefix("pre-")))
# Sonuç: 'ad'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.31: str.removeprefix davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; yalnız tam bir önek kaldırılır; karakter kümesi gibi davranmaz

```python
"ababa".removeprefix("ab")
"baX".removeprefix("ab")
"abc".removeprefix("")
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `'aba'`; `'baX'`; `'abc'`.
- [ ] Yalnız tam bir önek kaldırılır; karakter kümesi gibi davranmaz

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.removesuffix/README.md)
<!-- learning-task:end -->
