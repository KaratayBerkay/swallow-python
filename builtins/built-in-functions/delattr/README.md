## `delattr()`

```
delattr(object, name, /)
```

This is a relative of [setattr()](../setattr/README.md).  The arguments are an object and a
string.  The string must be the name of one of the object's attributes.  The
function deletes the named attribute, provided the object allows it.  For
example, `delattr(x, 'foobar')` is equivalent to `del x.foobar`.
*name* need not be a Python identifier (see [setattr()](../setattr/README.md)).

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.17: delattr sözleşmesini uygula**

#### Önce

[t:9.5](../../../tutorial/09-classes/9.5-inheritance/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

puan=4 niteliği olan örnekte `delattr(o,"puan")` çağır. Silmeden önce ve sonra hasattr ile kontrol et; ikinci silmeyi ayrı try/except içinde dene.

#### Geçiş ölçütleri

- [ ] Kontroller True ve False olur; ikinci silme AttributeError verir.
- [ ] Delattr nesneyi silmez; belirtilen niteliği kaldırır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../dir/README.md)
<!-- learning-task:end -->
