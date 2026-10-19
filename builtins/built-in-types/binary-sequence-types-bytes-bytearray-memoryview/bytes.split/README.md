## `bytes.split`

```
bytes.split(sep=None, maxsplit=-1)
bytearray.split(sep=None, maxsplit=-1)
```

Split the binary sequence into subsequences of the same type, using *sep*
as the delimiter string. If *maxsplit* is given and non-negative, at most
*maxsplit* splits are done (thus, the list will have at most `maxsplit+1`
elements).  If *maxsplit* is not specified or is `-1`, then there is no
limit on the number of splits (all possible splits are made).

If *sep* is given, consecutive delimiters are not grouped together and are
deemed to delimit empty subsequences (for example, `b'1,,2'.split(b',')`
returns `[b'1', b'', b'2']`).  The *sep* argument may consist of a
multibyte sequence as a single delimiter. Splitting an empty sequence with
a specified separator returns `[b'']` or `[bytearray(b'')]` depending
on the type of object being split.  The *sep* argument may be any
[bytes-like object](https://docs.python.org/3.15/glossary.html#term-bytes-like-object).

For example:

``` python
>>> b'1,2,3'.split(b',')
[b'1', b'2', b'3']
>>> b'1,2,3'.split(b',', maxsplit=1)
[b'1', b'2,3']
>>> b'1,2,,3,'.split(b',')
[b'1', b'2', b'', b'3', b'']
>>> b'1<>2<>3<4'.split(b'<>')
[b'1', b'2', b'3<4']
```
> Code: [example_01.py](example_01.py)

If *sep* is not specified or is `None`, a different splitting algorithm
is applied: runs of consecutive [ASCII whitespace](../bytes.isspace/README.md)
are regarded as a single
separator, and the result will contain no empty strings at the start or
end if the sequence has leading or trailing whitespace.  Consequently,
splitting an empty sequence or a sequence consisting solely of ASCII
whitespace without a specified separator returns `[]`.

For example:

``` python
>>> b'1 2 3'.split()
[b'1', b'2', b'3']
>>> b'1 2 3'.split(maxsplit=1)
[b'1', b'2 3']
>>> b'   1   2   3   '.split()
[b'1', b'2', b'3']
```
> Code: [example_02.py](example_02.py)

## Çözümlü kısa örnek

ASCII bayt kurallarıyla çalış; sep verilmezse boşluklar birleşir; açık sep boş alanları korur

```python
print(repr(b'a b'.split()))
# Sonuç: [b'a', b'b']
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.48: bytes.split davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; sep verilmezse boşluklar birleşir; açık sep boş alanları korur

```python
b'  a  b  '.split()
b'a,,b,'.split(b',')
b''.split()
b''.split(b',')
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `[b'a', b'b']`; `[b'a', b'', b'b', b'']`; `[]`; `[b'']`.
- [ ] ASCII bayt kurallarıyla çalış; sep verilmezse boşluklar birleşir; açık sep boş alanları korur
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytes.strip/README.md)
<!-- learning-task:end -->
