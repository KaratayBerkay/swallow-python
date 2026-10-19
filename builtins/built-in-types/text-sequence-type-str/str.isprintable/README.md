## `str.isprintable`

```
str.isprintable()
```

Return `True` if all characters in the string are printable, `False` if it
contains at least one non-printable character.

Here "printable" means the character is suitable for [repr()](../../../built-in-functions/repr/README.md) to use in
its output; "non-printable" means that [repr()](../../../built-in-functions/repr/README.md) on built-in types will
hex-escape the character.  It has no bearing on the handling of strings
written to [sys.stdout](https://docs.python.org/3.15/library/sys.html#sys.stdout) or [sys.stderr](https://docs.python.org/3.15/library/sys.html#sys.stderr).

The printable characters are those which in the Unicode character database
(see [unicodedata](https://docs.python.org/3.15/library/unicodedata.html#module-unicodedata)) have a general category in group Letter, Mark,
Number, Punctuation, or Symbol (L, M, N, P, or S); plus the ASCII space 0x20.
Nonprintable characters are those in group Separator or Other (Z or C),
except the ASCII space.

For example:

``` python
>>> ''.isprintable(), ' '.isprintable()
(True, True)
>>> '\t'.isprintable(), '\n'.isprintable()
(False, False)
```
> Code: [example_01.py](example_01.py)

See also `isspace()`.

## Çözümlü kısa örnek

Boş metin ile satır sonu içeren metnin sonucu farklıdır

```python
print(repr("abc".isprintable()))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.22: str.isprintable davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; boş metin ile satır sonu içeren metnin sonucu farklıdır

```python
"".isprintable()
"a\nb".isprintable()
" ".isprintable()
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `False`; `True`.
- [ ] Boş metin ile satır sonu içeren metnin sonucu farklıdır

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.isspace/README.md)
<!-- learning-task:end -->
