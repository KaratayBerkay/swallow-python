## `set()`

```
set(iterable=(), /)
```

Return a new set object, optionally with elements taken from
*iterable*.  set is a built-in class.  See also
[Set Types — set, frozenset](https://docs.python.org/3.15/builtins/stdtypes.html#types-set) for documentation about this class.

For other containers see the built-in [frozenset](../frozenset/README.md), [list](../list/README.md),
[tuple](../tuple/README.md), and [dict](../dict/README.md) classes, as well as the [collections](https://docs.python.org/3.15/library/collections.html#module-collections)
module.

## Çözümlü kısa örnek

Tekrarsız üyelikte öğe sırası sonuç ölçütü değildir.

```python
print(repr(sorted(set([2,1,2]))))
# Sonuç: [1, 2]
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.60: set davranışını ayırt et**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; tekrarsız üyelikte öğe sırası sonuç ölçütü değildir.

```python
set("banana")=={"b","a","n"}
set([[1]])
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `TypeError`.
- [ ] Tekrarsız üyelikte öğe sırası sonuç ölçütü değildir.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../setattr/README.md)
<!-- learning-task:end -->
