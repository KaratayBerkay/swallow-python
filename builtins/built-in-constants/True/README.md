## `True`

```
True
```

The true value of the [bool](../../built-in-functions/bool/README.md) type. Assignments to `True`
are illegal and raise a [SyntaxError](https://docs.python.org/3.15/builtins/exceptions.html#SyntaxError).

## Çözümlü kısa örnek

True tekil bool değeridir; değişken adıyla sabitin kendisi ayrıdır

```python
print(repr(True is True))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:1.2: True davranışını ayırt et**

#### Önce

[b:1](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; true tekil bool değeridir; değişken adıyla sabitin kendisi ayrıdır

```python
type(True) is bool
(lambda durum: durum is True)(True)
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `True`.
- [ ] True tekil bool değeridir; değişken adıyla sabitin kendisi ayrıdır

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../None/README.md)
<!-- learning-task:end -->
