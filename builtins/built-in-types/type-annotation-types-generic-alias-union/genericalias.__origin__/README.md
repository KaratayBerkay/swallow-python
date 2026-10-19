## `genericalias.__origin__`

```
genericalias.__origin__
```

This attribute points at the non-parameterized generic class:

``` python
>>> list[int].__origin__
<class 'list'>
```
> Code: [example_01.py](example_01.py)

## Çözümlü kısa örnek

Origin parametresiz asıl sınıftır

```python
print(repr(list[int].__origin__ is list))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.14.2: genericalias.__origin__ davranışını ayırt et**

#### Önce

[b:2.14](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; origin parametresiz asıl sınıftır

```python
dict[str,int].__origin__ is dict
list[list[int]].__origin__ is list
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `True`.
- [ ] Origin parametresiz asıl sınıftır

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../genericalias.__parameters__/README.md)
<!-- learning-task:end -->
