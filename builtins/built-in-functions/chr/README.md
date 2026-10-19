## `chr()`

```
chr(codepoint, /)
```

Return the string representing a character with the specified Unicode code point.
For example, `chr(97)` returns the string `'a'`, while
`chr(8364)` returns the string `'€'`. This is the inverse of [ord()](../ord/README.md).

The valid range for the argument is from 0 through 1,114,111 (0x10FFFF in
base 16).  [ValueError](https://docs.python.org/3.15/builtins/exceptions.html#ValueError) will be raised if it is outside that range.

## Çözümlü kısa örnek

Bir kod noktasından tek karakter üretme ile sınır hatasını ayır.

```python
print(repr(chr(65)))
# Sonuç: 'A'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.13: chr davranışını ayırt et**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; bir kod noktasından tek karakter üretme ile sınır hatasını ayır.

```python
chr(0x130)
chr(0x110000)
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `'İ'`; `ValueError`.
- [ ] Bir kod noktasından tek karakter üretme ile sınır hatasını ayır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../classmethod/README.md)
<!-- learning-task:end -->
