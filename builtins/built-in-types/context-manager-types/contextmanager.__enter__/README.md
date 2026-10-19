## `contextmanager.__enter__`

```
contextmanager.__enter__()
```

Enter the runtime context and return either this object or another object
related to the runtime context. The value returned by this method is bound to
the identifier in the `as` clause of `with` statements using
this context manager.

An example of a context manager that returns itself is a [file object](https://docs.python.org/3.15/glossary.html#term-file-object).
File objects return themselves from __enter__() to allow [open()](../../../built-in-functions/open/README.md) to be
used as the context expression in a `with` statement.

An example of a context manager that returns a related object is the one
returned by [decimal.localcontext()](https://docs.python.org/3.15/library/decimal.html#decimal.localcontext). These managers set the active
decimal context to a copy of the original decimal context and then return the
copy. This allows changes to be made to the current decimal context in the body
of the `with` statement without affecting code outside the
`with` statement.

## Çözümlü kısa örnek

```python
class Yonetici:
    def __enter__(self): return "acik"
    def __exit__(self, *hata): return False

with Yonetici() as durum:
    print(durum)
# acik
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.13.1: Giriş değerini yöneticiden ayır**

#### Önce

[b:2.13](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

__enter__ metodu self yerine "hazir" döndüren context manager yaz. With as değişkeni ve yönetici nesnenin farklı olduğunu göster. __enter__ hata verirse gövde ve __exit__ çalışır mı, akış üzerinden açıkla.

#### Geçiş ölçütleri

- [ ] As değişkeni "hazir" olur; yönetici __exit__ çağrısı için ayrıca tutulur.
- [ ] Enter tamamlanmazsa gövdeye girilmez ve bu yöneticinin exit metodu çağrılmaz.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../contextmanager.__exit__/README.md)
<!-- learning-task:end -->
