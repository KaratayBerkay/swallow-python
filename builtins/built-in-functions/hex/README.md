## `hex()`

```
hex(integer, /)
```

Convert an integer number to a lowercase hexadecimal string prefixed with
"0x". If *integer* is not a Python [int](../int/README.md) object, it has to define an
[__index__()](https://docs.python.org/3.15/reference/datamodel.html#object.__index__) method that returns an integer. Some examples:

``` python
>>> hex(255)
'0xff'
>>> hex(-42)
'-0x2a'
```
> Code: [example_01.py](example_01.py)

If you want to convert an integer number to an uppercase or lower hexadecimal
string with prefix or not, you can use either of the following ways:

``` python
>>> '%#x' % 255, '%x' % 255, '%X' % 255
('0xff', 'ff', 'FF')
>>> format(255, '#x'), format(255, 'x'), format(255, 'X')
('0xff', 'ff', 'FF')
>>> f'{255:#x}', f'{255:x}', f'{255:X}'
('0xff', 'ff', 'FF')
```
> Code: [example_02.py](example_02.py)

See also [format()](../format/README.md) for more information.

See also `int()` for converting a hexadecimal string to an
integer using a base of 16.

> **Note**
>
> To obtain a hexadecimal string representation for a float, use the
> [float.hex()](https://docs.python.org/3.15/builtins/stdtypes.html#float.hex) method.

## Çözümlü kısa örnek

Negatif işaretle taban önekini ayır.

```python
print(repr(hex(15)))
# Sonuç: '0xf'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.34: hex davranışını ayırt et**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; negatif işaretle taban önekini ayır.

```python
hex(-31)
hex(0)
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `'-0x1f'`; `'0x0'`.
- [ ] Negatif işaretle taban önekini ayır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../id/README.md)
<!-- learning-task:end -->
