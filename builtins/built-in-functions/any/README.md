## `any()`

```
any(iterable, /)
```

Return `True` if any element of the *iterable* is true.  If the iterable
is empty, return `False`.  Equivalent to:

``` python
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
```

## Çözümlü kısa örnek

Boş iterable ile herhangi bir doğru öğe bulunmasını ayır.

```python
print(repr(any([0,2])))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.5: any davranışını ayırt et**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; boş iterable ile herhangi bir doğru öğe bulunmasını ayır.

```python
any([])
any([0,"",3])
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `False`; `True`.
- [ ] Boş iterable ile herhangi bir doğru öğe bulunmasını ayır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../ascii/README.md)
<!-- learning-task:end -->
