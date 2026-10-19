## `False`

```
False
```

The false value of the [bool](../../built-in-functions/bool/README.md) type. Assignments to `False`
are illegal and raise a [SyntaxError](https://docs.python.org/3.15/builtins/exceptions.html#SyntaxError).

## Çözümlü kısa örnek

False tekil bool değeridir; değişken adıyla sabitin kendisi ayrıdır

```python
print(repr(False is False))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:1.1: False davranışını ayırt et**

#### Önce

[b:1](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; false tekil bool değeridir; değişken adıyla sabitin kendisi ayrıdır

```python
type(False) is bool
(lambda durum: durum is False)(False)
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `True`.
- [ ] False tekil bool değeridir; değişken adıyla sabitin kendisi ayrıdır

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../True/README.md)
<!-- learning-task:end -->
