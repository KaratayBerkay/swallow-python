## `ascii()`

```
ascii(object, /)
```

As [repr()](../repr/README.md), return a string containing a printable representation of an
object, but escape the non-ASCII characters in the string returned by
[repr()](../repr/README.md) using `\x`, `\u`, or `\U` escapes.  This generates a string
similar to that returned by [repr()](../repr/README.md) in Python 2.

## Çözümlü kısa örnek

ASCII kaçışlı temsil ile gerçek Unicode metni ayır.

```python
print(repr(ascii("Ada")))
# Sonuç: "'Ada'"
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.6: ascii davranışını ayırt et**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII kaçışlı temsil ile gerçek Unicode metni ayır.

```python
ascii("İpek")
ascii("a\nb")
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `"'\\u0130pek'"`; `"'a\\nb'"`.
- [ ] ASCII kaçışlı temsil ile gerçek Unicode metni ayır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bin/README.md)
<!-- learning-task:end -->
