## `int.bit_count`

```
int.bit_count()
```

Return the number of ones in the binary representation of the absolute
value of the integer. This is also known as the population count.
Example:

``` python
>>> n = 19
>>> bin(n)
'0b10011'
>>> n.bit_count()
3
>>> (-n).bit_count()
3
```
> Code: [example_01.py](example_01.py)

Equivalent to:

``` python
def bit_count(self):
    return bin(self).count("1")
```

> *Added in version 3.10.*

## Çözümlü kısa örnek

Mutlak değerdeki bir bitleri say; toplam bit sayısıyla karıştırma

```python
print(repr((7).bit_count()))
# Sonuç: 3
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.4.2: int.bit_count davranışını ayırt et**

#### Önce

[b:2.4](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; mutlak değerdeki bir bitleri say; toplam bit sayısıyla karıştırma

```python
(-10).bit_count()
(0).bit_count()
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `2`; `0`.
- [ ] Mutlak değerdeki bir bitleri say; toplam bit sayısıyla karıştırma

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../int.to_bytes/README.md)
<!-- learning-task:end -->
