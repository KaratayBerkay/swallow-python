## `float.from_number`

```
float.from_number(x)
```

Class method to return a floating-point number constructed from a number *x*.

If the argument is an integer or a floating-point number, a
floating-point number with the same value (within Python's floating-point
precision) is returned.  If the argument is outside the range of a Python
float, an [OverflowError](https://docs.python.org/3.15/builtins/exceptions.html#OverflowError) will be raised.

For a general Python object `x`, `float.from_number(x)` delegates to
`x.__float__()`.
If [__float__()](https://docs.python.org/3.15/reference/datamodel.html#object.__float__) is not defined then it falls back
to [__index__()](https://docs.python.org/3.15/reference/datamodel.html#object.__index__).

> *Added in version 3.14.*

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.4.7: float.from_number sınırını göster**

#### Önce

[b:2.4](../README.md) ve bu sayfanın açıklama/örnekleri.

Sürüm: Python 3.14 veya üzeri. Daha eski yorumlayıcıda yalnız bu sürüme bağlı kısmı gerekçeli yazılı iz ile çözebilirsin; çalıştırma kanıtını bekleyen olarak kaydet.

#### Tek görev

`float.from_number(7)`, `float.from_number("7")` ve yalnız __index__ döndüren hazır nesne için çağrı akışını çıkar. __float__ da varsa önceliği belirt.

#### Geçiş ölçütleri

- [ ] 7.0, TypeError; __float__ varsa önce o, yoksa __index__ kullanılır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../float.as_integer_ratio/README.md)
<!-- learning-task:end -->
