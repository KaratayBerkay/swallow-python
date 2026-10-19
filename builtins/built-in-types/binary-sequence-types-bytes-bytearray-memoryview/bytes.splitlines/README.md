## `bytes.splitlines`

```
bytes.splitlines(keepends=False)
bytearray.splitlines(keepends=False)
```

Return a list of the lines in the binary sequence, breaking at ASCII
line boundaries. This method uses the [universal newlines](https://docs.python.org/3.15/glossary.html#term-universal-newlines) approach
to splitting lines. Line breaks are not included in the resulting list
unless *keepends* is given and true.

For example:

``` python
>>> b'ab c\n\nde fg\rkl\r\n'.splitlines()
[b'ab c', b'', b'de fg', b'kl']
>>> b'ab c\n\nde fg\rkl\r\n'.splitlines(keepends=True)
[b'ab c\n', b'\n', b'de fg\r', b'kl\r\n']
```
> Code: [example_01.py](example_01.py)

Unlike [split()](../bytes.split/README.md) when a delimiter string *sep* is given, this
method returns an empty list for the empty string, and a terminal line
break does not result in an extra line:

``` python
>>> b"".split(b'\n'), b"Two lines\n".split(b'\n')
([b''], [b'Two lines', b''])
>>> b"".splitlines(), b"One line\n".splitlines()
([], [b'One line'])
```
> Code: [example_02.py](example_02.py)

## Çözümlü kısa örnek

ASCII bayt kurallarıyla çalış; sondaki satır sonu ek boş satır üretmez; keepends sonlandırıcıyı korur

```python
print(repr(b'a\nb'.splitlines()))
# Sonuç: [b'a', b'b']
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.74: bytes.splitlines davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; sondaki satır sonu ek boş satır üretmez; keepends sonlandırıcıyı korur

```python
b'a\n'.splitlines()
b'a\n\nb'.splitlines(True)
b''.splitlines()
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `[b'a']`; `[b'a\n', b'\n', b'b']`; `[]`.
- [ ] ASCII bayt kurallarıyla çalış; sondaki satır sonu ek boş satır üretmez; keepends sonlandırıcıyı korur
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytes.swapcase/README.md)
<!-- learning-task:end -->
