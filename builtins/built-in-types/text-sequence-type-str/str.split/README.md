## `str.split`

```
str.split(sep=None, maxsplit=-1)
```

Return a list of the words in the string, using *sep* as the delimiter
string.  If *maxsplit* is given, at most *maxsplit* splits are done (thus,
the list will have at most `maxsplit+1` elements).  If *maxsplit* is not
specified or `-1`, then there is no limit on the number of splits
(all possible splits are made).

If *sep* is given, consecutive delimiters are not grouped together and are
deemed to delimit empty strings (for example, `'1,,2'.split(',')` returns
`['1', '', '2']`).  The *sep* argument may consist of multiple characters
as a single delimiter (to split with multiple delimiters, use
[re.split()](https://docs.python.org/3.15/library/re.html#re.split)). Splitting an empty string with a specified separator
returns `['']`.

For example:

``` python
>>> '1,2,3'.split(',')
['1', '2', '3']
>>> '1,2,3'.split(',', maxsplit=1)
['1', '2,3']
>>> '1,2,,3,'.split(',')
['1', '2', '', '3', '']
>>> '1<>2<>3<4'.split('<>')
['1', '2', '3<4']
```
> Code: [example_01.py](example_01.py)

If *sep* is not specified or is `None`, a different splitting algorithm is
applied: runs of consecutive [whitespace](../str.isspace/README.md) are regarded
as a single separator,
and the result will contain no empty strings at the start or end if the
string has leading or trailing whitespace.  Consequently, splitting an empty
string or a string consisting of just whitespace with a `None` separator
returns `[]`.

For example:

``` python
>>> '1 2 3'.split()
['1', '2', '3']
>>> '1 2 3'.split(maxsplit=1)
['1', '2 3']
>>> '   1   2   3   '.split()
['1', '2', '3']
```
> Code: [example_02.py](example_02.py)

If *sep* is not specified or is `None` and  *maxsplit* is `0`, only
leading runs of consecutive whitespace are considered.

For example:

``` python
>>> "".split(None, 0)
[]
>>> "   ".split(None, 0)
[]
>>> "   foo   ".split(maxsplit=0)
['foo   ']
```
> Code: [example_03.py](example_03.py)

See also `join()` and `rsplit()`.

## Çözümlü kısa örnek

Sep verilmezse boşluklar birleşir; açık sep boş alanları korur

```python
print(repr("a b".split()))
# Sonuç: ['a', 'b']
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.40: str.split davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; sep verilmezse boşluklar birleşir; açık sep boş alanları korur

```python
"  a  b  ".split()
"a,,b,".split(",")
"".split()
"".split(",")
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `['a', 'b']`; `['a', '', 'b', '']`; `[]`; `['']`.
- [ ] Sep verilmezse boşluklar birleşir; açık sep boş alanları korur

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.splitlines/README.md)
<!-- learning-task:end -->
