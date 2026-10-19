## `callable()`

```
callable(object, /)
```

Return [True](https://docs.python.org/3.15/builtins/constants.html#True) if the *object* argument appears callable,
[False](https://docs.python.org/3.15/builtins/constants.html#False) if not.  If this returns `True`, it is still possible that a
call fails, but if it is `False`, calling *object* will never succeed.
Note that classes are callable (calling a class returns a new instance);
instances are callable if their class has a [__call__()](https://docs.python.org/3.15/reference/datamodel.html#object.__call__) method.

> *Added in version 3.2:* This function was first removed in Python 3.0 and then brought back
> in Python 3.2.

## Çözümlü kısa örnek

Çağrılabilir olma, her argümanla başarılı çağrı garantisi değildir.

```python
print(repr(callable(len)))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.12: callable davranışını ayırt et**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; çağrılabilir olma, her argümanla başarılı çağrı garantisi değildir.

```python
callable(7)
callable(lambda x:x)
(lambda x:x)()
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `False`; `True`; `TypeError`.
- [ ] Çağrılabilir olma, her argümanla başarılı çağrı garantisi değildir.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../chr/README.md)
<!-- learning-task:end -->
