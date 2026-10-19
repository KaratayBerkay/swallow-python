## `bin()`

```
bin(integer, /)
```

Convert an integer number to a binary string prefixed with "0b". The result
is a valid Python expression. If *integer* is not a Python [int](../int/README.md) object, it
has to define an [__index__()](https://docs.python.org/3.15/reference/datamodel.html#object.__index__) method that returns an integer. Some
examples:

``` python
>>> bin(3)
'0b11'
>>> bin(-10)
'-0b1010'
```
> Code: [example_01.py](example_01.py)

If the prefix "0b" is desired or not, you can use either of the following ways.

``` python
>>> format(14, '#b'), format(14, 'b')
('0b1110', '1110')
>>> f'{14:#b}', f'{14:b}'
('0b1110', '1110')
```
> Code: [example_02.py](example_02.py)

See also [enum.bin()](https://docs.python.org/3.15/library/enum.html#enum.bin) to represent negative values as twos-complement.

See also [format()](../format/README.md) for more information.

## Çözümlü kısa örnek

Negatif işaretiyle ikilik basamakları ve öneki ayır.

```python
print(repr(bin(5)))
# Sonuç: '0b101'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.7: bin davranışını ayırt et**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; negatif işaretiyle ikilik basamakları ve öneki ayır.

```python
bin(-9)
bin(0)
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `'-0b1001'`; `'0b0'`.
- [ ] Negatif işaretiyle ikilik basamakları ve öneki ayır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bool/README.md)
<!-- learning-task:end -->
