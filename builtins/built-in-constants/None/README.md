## `None`

```
None
```

An object frequently used to represent the absence of a value, as when
default arguments are not passed to a function. Assignments to `None`
are illegal and raise a [SyntaxError](https://docs.python.org/3.15/builtins/exceptions.html#SyntaxError).
`None` is the sole instance of the [NoneType](https://docs.python.org/3.15/library/types.html#types.NoneType) type.

## Çözümlü kısa örnek

None yokluk değeridir; sıfır ve boş metin ayrı değerlerdir

```python
print(repr(None is None))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:1.3: None davranışını ayırt et**

#### Önce

[b:1](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; none yokluk değeridir; sıfır ve boş metin ayrı değerlerdir

```python
None == 0
None == ""
type(None) is type(None)
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `False`; `False`; `True`.
- [ ] None yokluk değeridir; sıfır ve boş metin ayrı değerlerdir

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../NotImplemented/README.md)
<!-- learning-task:end -->
