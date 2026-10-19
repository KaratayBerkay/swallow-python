## `getattr()`

```
getattr(object, name, /)
getattr(object, name, default, /)
```

Return the value of the named attribute of *object*.  *name* must be a string.
If the string is the name of one of the object's attributes, the result is the
value of that attribute.  For example, `getattr(x, 'foobar')` is equivalent to
`x.foobar`.  If the named attribute does not exist, *default* is returned if
provided, otherwise [AttributeError](https://docs.python.org/3.15/builtins/exceptions.html#AttributeError) is raised.
*name* need not be a Python identifier (see [setattr()](../setattr/README.md)).

> **Note**
>
> Since [private name mangling](https://docs.python.org/3.15/reference/expressions.html#private-name-mangling) happens at
> compilation time, one must manually mangle a private attribute's
> (attributes with two leading underscores) name in order to retrieve it with
> getattr().

## Çözümlü kısa örnek

Varsayılan değer yalnız eksik nitelikte kullanılır.

```python
class K: pass
o=K(); o.puan=4
print(repr(getattr(o,"puan")))
# Sonuç: 4
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.29: getattr davranışını ayırt et**

#### Önce

[t:9.5](../../../tutorial/09-classes/9.5-inheritance/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; varsayılan değer yalnız eksik nitelikte kullanılır.

```python
class K: pass
o=K(); o.puan=4
getattr(o,"eksik",0)
getattr(o,"eksik")
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `0`; `AttributeError`.
- [ ] Varsayılan değer yalnız eksik nitelikte kullanılır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../globals/README.md)
<!-- learning-task:end -->
