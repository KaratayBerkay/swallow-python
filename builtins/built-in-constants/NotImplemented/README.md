## `NotImplemented`

```
NotImplemented
```

A special value which should be returned by the binary special methods
(e.g. [__eq__()](https://docs.python.org/3.15/reference/datamodel.html#object.__eq__), [__lt__()](https://docs.python.org/3.15/reference/datamodel.html#object.__lt__), [__add__()](https://docs.python.org/3.15/reference/datamodel.html#object.__add__), [__rsub__()](https://docs.python.org/3.15/reference/datamodel.html#object.__rsub__),
etc.) to indicate that the operation is not implemented with respect to
the other type; may be returned by the in-place binary special methods
(e.g. [__imul__()](https://docs.python.org/3.15/reference/datamodel.html#object.__imul__), [__iand__()](https://docs.python.org/3.15/reference/datamodel.html#object.__iand__), etc.) for the same purpose.
It should not be evaluated in a boolean context.
NotImplemented is the sole instance of the [types.NotImplementedType](https://docs.python.org/3.15/library/types.html#types.NotImplementedType) type.

> **Note**
>
> When a binary (or in-place) method returns NotImplemented the
> interpreter will try the reflected operation on the other type (or some
> other fallback, depending on the operator).  If all attempts return
> NotImplemented, the interpreter will raise an appropriate exception.
> Incorrectly returning NotImplemented will result in a misleading
> error message or the NotImplemented value being returned to Python code.
>
> See [Implementing the arithmetic operations](https://docs.python.org/3.15/library/numbers.html#implementing-the-arithmetic-operations) for examples.

> **Caution**
>
> NotImplemented and [NotImplementedError](https://docs.python.org/3.15/builtins/exceptions.html#NotImplementedError) are not
> interchangeable. This constant should only be used as described
> above; see [NotImplementedError](https://docs.python.org/3.15/builtins/exceptions.html#NotImplementedError) for details on correct usage
> of the exception.

> *Changed in version 3.9:* Evaluating NotImplemented in a boolean context was deprecated.

> *Changed in version 3.14:* Evaluating NotImplemented in a boolean context now raises a [TypeError](https://docs.python.org/3.15/builtins/exceptions.html#TypeError).
> It previously evaluated to [True](../True/README.md) and emitted a [DeprecationWarning](https://docs.python.org/3.15/builtins/exceptions.html#DeprecationWarning)
> since Python 3.9.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:1.4: Operatörün geri dönüş yolunu izle**

#### Önce

[b:1](../README.md) ve bu sayfanın açıklama/örnekleri.

Sürüm: Python 3.14 veya üzeri. Daha eski yorumlayıcıda yalnız bu sürüme bağlı kısmı gerekçeli yazılı iz ile çözebilirsin; çalıştırma kanıtını bekleyen olarak kaydet.

#### Tek görev

Sol nesnenin __add__ metodu NotImplemented, sağ nesnenin __radd__ metodu 9 döndürüyor. `sol + sag` akışını yazılı izle. İki metot da NotImplemented döndürürse ne olur? Sabiti raise etmek, NotImplementedError yükseltmek ve bool bağlamına sokmakla karşılaştır.

#### Geçiş ölçütleri

- [ ] Yansıyan işlem denenir ve 9 döner; iki taraf desteklemezse TypeError olur.
- [ ] NotImplemented bir exception değildir; raise etmek TypeError verir; NotImplementedError ayrı hata türüdür.
- [ ] Python 3.14+ bool(NotImplemented) TypeError verir; eski sürüm davranışı yeni sürüm beklentisi yerine sayılmaz.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../Ellipsis/README.md)
<!-- learning-task:end -->
