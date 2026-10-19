## `bool()`

```
bool(object=False, /)
```

Return a Boolean value, i.e. one of `True` or `False`.  The argument
is converted using the standard [truth testing procedure](https://docs.python.org/3.15/builtins/stdtypes.html#truth).
If the argument is false
or omitted, this returns `False`; otherwise, it returns `True`.  The
bool class is a subclass of [int](../int/README.md) (see [Numeric Types — int, float, complex](https://docs.python.org/3.15/builtins/stdtypes.html#typesnumeric)).
It cannot be subclassed further.  Its only instances are `False` and
`True` (see [Boolean Type - bool](https://docs.python.org/3.15/builtins/stdtypes.html#typebool)).

> *Changed in version 3.7:* The parameter is now positional-only.

## Çözümlü kısa örnek

Boş nesneyle boş olmayan ama sıfır içeren koleksiyonu ayır.

```python
print(repr(bool(3)))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.8: bool davranışını ayırt et**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; boş nesneyle boş olmayan ama sıfır içeren koleksiyonu ayır.

```python
bool([])
bool([0])
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `False`; `True`.
- [ ] Boş nesneyle boş olmayan ama sıfır içeren koleksiyonu ayır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../breakpoint/README.md)
<!-- learning-task:end -->
