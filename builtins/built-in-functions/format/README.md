## `format()`

```
format(value, format_spec="", /)
```

Convert a *value* to a "formatted" representation, as controlled by
*format_spec*.  The interpretation of *format_spec* will depend on the type
of the *value* argument; however, there is a standard formatting syntax that
is used by most built-in types: [Format specification mini-language](https://docs.python.org/3.15/library/string.html#formatspec).

The default *format_spec* is an empty string which usually gives the same
effect as calling `str(value)`.

A call to `format(value, format_spec)` is translated to
`type(value).__format__(value, format_spec)` which bypasses the instance
dictionary when searching for the value's [__format__()](https://docs.python.org/3.15/reference/datamodel.html#object.__format__) method.
A [TypeError](https://docs.python.org/3.15/builtins/exceptions.html#TypeError) exception is raised if the method search reaches
`object` and the *format_spec* is non-empty, or if either the
*format_spec* or the return value are not strings.

> *Changed in version 3.4:* `object().__format__(format_spec)` raises [TypeError](https://docs.python.org/3.15/builtins/exceptions.html#TypeError)
> if *format_spec* is not an empty string.

## Çözümlü kısa örnek

Alan genişliği alt sınırdır; biçimlenen sonuç yeni metindir.

```python
print(repr(format(2.5,".1f")))
# Sonuç: '2.5'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.26: format davranışını ayırt et**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; alan genişliği alt sınırdır; biçimlenen sonuç yeni metindir.

```python
format(7,"04d")
format(12.345,".2f")
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `'0007'`; `'12.35'`.
- [ ] Alan genişliği alt sınırdır; biçimlenen sonuç yeni metindir.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../frozenset/README.md)
<!-- learning-task:end -->
