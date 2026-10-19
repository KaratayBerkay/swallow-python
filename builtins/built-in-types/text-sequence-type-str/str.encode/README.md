## `str.encode`

```
str.encode(encoding="utf-8", errors="strict")
```

Return the string encoded to [bytes](../../binary-sequence-types-bytes-bytearray-memoryview/bytes/README.md).

*encoding* defaults to `'utf-8'`;
see [Standard Encodings](https://docs.python.org/3.15/library/codecs.html#standard-encodings) for possible values.

*errors* controls how encoding errors are handled.
If `'strict'` (the default), a [UnicodeError](https://docs.python.org/3.15/builtins/exceptions.html#UnicodeError) exception is raised.
Other possible values are `'ignore'`,
`'replace'`, `'xmlcharrefreplace'`, `'backslashreplace'` and any
other name registered via [codecs.register_error()](https://docs.python.org/3.15/library/codecs.html#codecs.register_error).
See [Error Handlers](https://docs.python.org/3.15/library/codecs.html#error-handlers) for details.

For performance reasons, the value of *errors* is not checked for validity
unless an encoding error actually occurs,
[Python Development Mode](https://docs.python.org/3.15/library/devmode.html#devmode) is enabled
or a [debug build](https://docs.python.org/3.15/using/configure.html#debug-build) is used.
For example:

``` python
>>> encoded_str_to_bytes = 'Python'.encode()
>>> type(encoded_str_to_bytes)
<class 'bytes'>
>>> encoded_str_to_bytes
b'Python'
```
> Code: [example_01.py](example_01.py)

> *Changed in version 3.1:* Added support for keyword arguments.

> *Changed in version 3.9:* The value of the *errors* argument is now checked in [Python Development Mode](https://docs.python.org/3.15/library/devmode.html#devmode) and
> in [debug mode](https://docs.python.org/3.15/using/configure.html#debug-build).

## Çözümlü kısa örnek

Kodlama yeni bytes üretir; strict hata, replace veri kaybı anlamına gelir

```python
print(repr("A".encode()))
# Sonuç: b'A'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.8: str.encode davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; kodlama yeni bytes üretir; strict hata, replace veri kaybı anlamına gelir

```python
"İ".encode("utf-8")
"İ".encode("ascii")
"İ".encode("ascii","replace")
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b'\xc4\xb0'`; `UnicodeEncodeError`; `b'?'`.
- [ ] Kodlama yeni bytes üretir; strict hata, replace veri kaybı anlamına gelir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.endswith/README.md)
<!-- learning-task:end -->
