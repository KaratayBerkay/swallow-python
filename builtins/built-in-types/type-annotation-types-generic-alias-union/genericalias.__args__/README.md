## `genericalias.__args__`

```
genericalias.__args__
```

This attribute is a [tuple](../../sequence-types-list-tuple-range/tuple/README.md) (possibly of length 1) of generic
types passed to the original [__class_getitem__()](https://docs.python.org/3.15/reference/datamodel.html#object.__class_getitem__) of the
generic class:

``` python
>>> dict[str, list[int]].__args__
(<class 'str'>, list[int])
```
> Code: [example_01.py](example_01.py)

## Çözümlü kısa örnek

Argüman tupleı iç içe yapıyı korur

```python
print(repr(list[int].__args__ == (int,)))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.14.1: genericalias.__args__ davranışını ayırt et**

#### Önce

[b:2.14](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; argüman tupleı iç içe yapıyı korur

```python
dict[str,list[int]].__args__ == (str,list[int])
tuple[int,str].__args__ == (int,str)
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `True`.
- [ ] Argüman tupleı iç içe yapıyı korur

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../genericalias.__origin__/README.md)
<!-- learning-task:end -->
