## `frozenset()`

```
frozenset(iterable=(), /)
```

Return a new frozenset object, optionally with elements taken from
*iterable*.  frozenset is a built-in class.  See also
[Set Types — set, frozenset](https://docs.python.org/3.15/builtins/stdtypes.html#types-set) for documentation about this class.

For other containers see the built-in [set](../set/README.md), [list](../list/README.md),
[tuple](../tuple/README.md), and [dict](../dict/README.md) classes, as well as the [collections](https://docs.python.org/3.15/library/collections.html#module-collections)
module.

## Çözümlü kısa örnek

Tekrarların silinmesiyle sonradan değiştirilememe özelliğini ayır.

```python
print(repr(sorted(frozenset([2,1,2]))))
# Sonuç: [1, 2]
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.28: frozenset davranışını ayırt et**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; tekrarların silinmesiyle sonradan değiştirilememe özelliğini ayır.

```python
frozenset([1,2])==frozenset([2,1])
frozenset([1]).add(2)
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `AttributeError`.
- [ ] Tekrarların silinmesiyle sonradan değiştirilememe özelliğini ayır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../getattr/README.md)
<!-- learning-task:end -->
