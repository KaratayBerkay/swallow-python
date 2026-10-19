## `hasattr()`

```
hasattr(object, name, /)
```

The arguments are an object and a string.  The result is `True` if the
string is the name of one of the object's attributes, `False` if not. (This
is implemented by calling `getattr(object, name)` and seeing whether it
raises an [AttributeError](https://docs.python.org/3.15/builtins/exceptions.html#AttributeError) or not.)

## Çözümlü kısa örnek

Hasattr yalnız AttributeError durumunu False yapar; diğer hatayı yutmaz.

```python
class K: puan = 4
o = K()
print(hasattr(o, "puan"))
# True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.31: hasattr davranışını ayırt et**

#### Önce

[t:9.5](../../../tutorial/09-classes/9.5-inheritance/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

`class K: puan=4` ve `o=K()` için `hasattr(o,"puan")` ve `hasattr(o,"eksik")` sonuçlarını çalıştır. Ayrı bir hazır nesnenin nitelik okumasının AttributeError yerine ValueError yükselttiği verilmiş olsun; hasattr sonucunu yazılı çıkar. Bu nesnenin özel erişim mekanizmasını yazman gerekmiyor.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `False`; `ValueError`.
- [ ] Hasattr yalnız AttributeError durumunu False yapar; diğer hatayı yutmaz.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../hash/README.md)
<!-- learning-task:end -->
