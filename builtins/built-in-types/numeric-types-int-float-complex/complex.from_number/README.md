## `complex.from_number`

```
complex.from_number(x)
```

Class method to convert a number to a complex number.

For a general Python object `x`, `complex.from_number(x)` delegates to
`x.__complex__()`.  If [__complex__()](https://docs.python.org/3.15/reference/datamodel.html#object.__complex__) is not defined then it falls back
to [__float__()](https://docs.python.org/3.15/reference/datamodel.html#object.__float__).  If `__float__()` is not defined then it falls back
to [__index__()](https://docs.python.org/3.15/reference/datamodel.html#object.__index__).

> *Added in version 3.14.*

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.4.12: complex.from_number sınırını göster**

#### Önce

[b:2.4](../README.md) ve bu sayfanın açıklama/örnekleri.

Sürüm: Python 3.14 veya üzeri. Daha eski yorumlayıcıda yalnız bu sürüme bağlı kısmı gerekçeli yazılı iz ile çözebilirsin; çalıştırma kanıtını bekleyen olarak kaydet.

#### Tek görev

`complex.from_number(7)`, `complex.from_number("7")` çağrılarını ve __complex__, __float__, __index__ metotlarının hepsi verilmiş nesnedeki önceliği çıkar.

#### Geçiş ölçütleri

- [ ] (7+0j), TypeError; öncelik __complex__, sonra __float__, sonra __index__ olur.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
