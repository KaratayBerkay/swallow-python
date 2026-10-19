## `int.bit_length`

```
int.bit_length()
```

Return the number of bits necessary to represent an integer in binary,
excluding the sign and leading zeros:

``` python
>>> n = -37
>>> bin(n)
'-0b100101'
>>> n.bit_length()
6
```
> Code: [example_01.py](example_01.py)

More precisely, if `x` is nonzero, then `x.bit_length()` is the
unique positive integer `k` such that `2**(k-1) <= abs(x) < 2**k`.
Equivalently, when `abs(x)` is small enough to have a correctly
rounded logarithm, then `k = 1 + int(log(abs(x), 2))`.
If `x` is zero, then `x.bit_length()` returns `0`.

Equivalent to:

``` python
def bit_length(self):
    s = bin(self)       # binary representation:  bin(-37) --> '-0b100101'
    s = s.lstrip('-0b') # remove leading zeros and minus sign
    return len(s)       # len('100101') --> 6
```

> *Added in version 3.1.*

## Çözümlü kısa örnek

İşaret ve baştaki sıfırlar sayılmaz; sıfırın uzunluğu sıfırdır

```python
print(repr((8).bit_length()))
# Sonuç: 4
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.4.1: int.bit_length davranışını ayırt et**

#### Önce

[b:2.4](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; i̇şaret ve baştaki sıfırlar sayılmaz; sıfırın uzunluğu sıfırdır

```python
(-9).bit_length()
(0).bit_length()
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `4`; `0`.
- [ ] İşaret ve baştaki sıfırlar sayılmaz; sıfırın uzunluğu sıfırdır

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../int.bit_count/README.md)
<!-- learning-task:end -->
