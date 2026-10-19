## `oct()`

```
oct(integer, /)
```

Convert an integer number to an octal string prefixed with "0o".  The result
is a valid Python expression. If *integer* is not a Python [int](../int/README.md) object, it
has to define an [__index__()](https://docs.python.org/3.15/reference/datamodel.html#object.__index__) method that returns an integer. For
example:

``` python
>>> oct(8)
'0o10'
>>> oct(-56)
'-0o70'
```
> Code: [example_01.py](example_01.py)

If you want to convert an integer number to an octal string either with the prefix
"0o" or not, you can use either of the following ways.

``` python
>>> '%#o' % 10, '%o' % 10
('0o12', '12')
>>> format(10, '#o'), format(10, 'o')
('0o12', '12')
>>> f'{10:#o}', f'{10:o}'
('0o12', '12')
```
> Code: [example_02.py](example_02.py)

See also [format()](../format/README.md) for more information.

## Çözümlü kısa örnek

Sekizlik gösterim metindir; işaret basamaklardan önce kalır.

```python
print(repr(oct(8)))
# Sonuç: '0o10'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.50: oct davranışını ayırt et**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; sekizlik gösterim metindir; işaret basamaklardan önce kalır.

```python
oct(-9)
oct(0)
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `'-0o11'`; `'0o0'`.
- [ ] Sekizlik gösterim metindir; işaret basamaklardan önce kalır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../open/README.md)
<!-- learning-task:end -->
