## `all()`

```
all(iterable, /)
```

Return `True` if all elements of the *iterable* are true (or if the iterable
is empty).  Equivalent to:

``` python
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
```

## Çözümlü kısa örnek

Boş iterable ile ilk yanlış öğede durma kuralını açıkla.

```python
print(repr(all([1,2])))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.3: all davranışını ayırt et**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; boş iterable ile ilk yanlış öğede durma kuralını açıkla.

```python
all([])
all([2,0,3])
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `False`.
- [ ] Boş iterable ile ilk yanlış öğede durma kuralını açıkla.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../anext/README.md)
<!-- learning-task:end -->
