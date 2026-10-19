## `genericalias.__unpacked__`

```
genericalias.__unpacked__
```

A boolean that is true if the alias has been unpacked using the
`*` operator (see `TypeVarTuple`).

> *Added in version 3.11.*

## Çözümlü kısa örnek

Aliası yıldızla açınca elde edilen alias __unpacked__ işaretini taşır; asıl alias değişmez. Burada yıldız bir nesneyi çağırmak değil, tuple ifadesinin içine açmaktır.

```python
normal = tuple[int, str]
unpacked = (*normal,)[0]
print(normal.__unpacked__, unpacked.__unpacked__)
# False True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.14.4: genericalias.__unpacked__ davranışını ayırt et**

#### Önce

[b:2.14](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; unpacked alias işaretiyle normal aliası ayır

```python
(*tuple[float,str],)[0].__unpacked__
(*tuple[float,str],)[0].__origin__ is tuple
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `True`.
- [ ] Unpacked alias işaretiyle normal aliası ayır

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
