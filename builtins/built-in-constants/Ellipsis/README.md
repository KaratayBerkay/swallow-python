## `Ellipsis`

```
Ellipsis
```

The same as the ellipsis literal "`...`", an object frequently used to
indicate that something is omitted. Assignment to `Ellipsis` is possible, but
assignment to  `...` raises a [SyntaxError](https://docs.python.org/3.15/builtins/exceptions.html#SyntaxError).
`Ellipsis` is the sole instance of the [types.EllipsisType](https://docs.python.org/3.15/library/types.html#types.EllipsisType) type.

## Çözümlü kısa örnek

Üç nokta aynı tekil nesneyi verir; Ellipsis adı ile literal ayrıdır

```python
print(repr(Ellipsis is ...))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:1.5: Ellipsis davranışını ayırt et**

#### Önce

[b:1](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; üç nokta aynı tekil nesneyi verir; Ellipsis adı ile literal ayrıdır

```python
type(Ellipsis) is type(...)
[Ellipsis,...][0] is ...
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `True`.
- [ ] Üç nokta aynı tekil nesneyi verir; Ellipsis adı ile literal ayrıdır

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../__debug__/README.md)
<!-- learning-task:end -->
