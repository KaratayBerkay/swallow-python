## `bytes.expandtabs`

```
bytes.expandtabs(tabsize=8)
bytearray.expandtabs(tabsize=8)
```

Return a copy of the sequence where all ASCII tab characters are replaced
by one or more ASCII spaces, depending on the current column and the given
tab size.  Tab positions occur every *tabsize* bytes (default is 8,
giving tab positions at columns 0, 8, 16 and so on).  To expand the
sequence, the current column is set to zero and the sequence is examined
byte by byte.  If the byte is an ASCII tab character (`b'\t'`), one or
more space characters are inserted in the result until the current column
is equal to the next tab position. (The tab character itself is not
copied.)  If the current byte is an ASCII newline (`b'\n'`) or
carriage return (`b'\r'`), it is copied and the current column is reset
to zero.  Any other byte value is copied unchanged and the current column
is incremented by one regardless of how the byte value is represented when
printed:

``` python
>>> b'01\t012\t0123\t01234'.expandtabs()
b'01      012     0123    01234'
>>> b'01\t012\t0123\t01234'.expandtabs(4)
b'01  012 0123    01234'
```
> Code: [example_01.py](example_01.py)

> **Note**
>
> The bytearray version of this method does *not* operate in place - it
> always produces a new object, even if no changes were made.

## Çözümlü kısa örnek

ASCII bayt kurallarıyla çalış; tab sabit sayıda boşluk değil sonraki tab durağına ilerlemedir

```python
print(repr(b'a\tb'.expandtabs(4)))
# Sonuç: b'a   b'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.54: bytes.expandtabs davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; tab sabit sayıda boşluk değil sonraki tab durağına ilerlemedir

```python
b'ab\tc'.expandtabs(4)
b'abcd\tx'.expandtabs(4)
b'a\nb\tc'.expandtabs(4)
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b'ab  c'`; `b'abcd    x'`; `b'a\nb   c'`.
- [ ] ASCII bayt kurallarıyla çalış; tab sabit sayıda boşluk değil sonraki tab durağına ilerlemedir
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytes.isalnum/README.md)
<!-- learning-task:end -->
