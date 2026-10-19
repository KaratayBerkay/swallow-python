## `object()`

```
object()
```

This is the ultimate base class of all other classes. It has methods
that are common to all instances of Python classes. When the constructor
is called, it returns a new featureless object. The constructor does not
accept any arguments.

> **Note**
>
> object instances do *not* have [__dict__](https://docs.python.org/3.15/reference/datamodel.html#object.__dict__)
> attributes, so you can't assign arbitrary attributes to an instance of
> object.

## Çözümlü kısa örnek

Object örneği oluşturmayı ona keyfi veri niteliği eklemekle karıştırma.

```python
print(repr(isinstance(object(),object)))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.49: object davranışını ayırt et**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; object örneği oluşturmayı ona keyfi veri niteliği eklemekle karıştırma.

```python
type(object()) is object
hasattr(object(),"__dict__")
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `False`.
- [ ] Object örneği oluşturmayı ona keyfi veri niteliği eklemekle karıştırma.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../oct/README.md)
<!-- learning-task:end -->
