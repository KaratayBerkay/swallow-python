Three attributes on exception objects provide information about the context in
which the exception was raised:

### BaseException.__context__, BaseException.__cause__, BaseException.__suppress_context__

When raising a new exception while another exception
is already being handled, the new exception's
`__context__` attribute is automatically set to the handled
exception.  An exception may be handled when an `except` or
`finally` clause, or a `with` statement, is used.

This implicit exception context can be
supplemented with an explicit cause by using `from` with
`raise`:

``` python
raise new_exc from original_exc
```

The expression following `from` must be an exception or `None`. It
will be set as `__cause__` on the raised exception. Setting
`__cause__` also implicitly sets the `__suppress_context__`
attribute to `True`, so that using `raise new_exc from None`
effectively replaces the old exception with the new one for display
purposes (e.g. converting [KeyError](../concrete-exceptions/KeyError/README.md) to [AttributeError](../concrete-exceptions/AttributeError/README.md)), while
leaving the old exception available in `__context__` for introspection
when debugging.

The default traceback display code shows these chained exceptions in
addition to the traceback for the exception itself. An explicitly chained
exception in `__cause__` is always shown when present. An implicitly
chained exception in `__context__` is shown only if `__cause__`
is [None](https://docs.python.org/3.15/builtins/constants.html#None) and `__suppress_context__` is false.

In either case, the exception itself is always shown after any chained
exceptions so that the final line of the traceback always shows the last
exception that was raised.

<!-- learning-task:start -->
#### Bölüm görevi

**Görev b:4.1: Hata zincirini üç biçimde karşılaştır**

##### Önce

[b:4](../README.md) ve bu sayfanın açıklama/örnekleri.

##### Tek görev

KeyError yakalandığında ValueError üreten üç küçük fonksiyon yaz: yalın raise, `from asil`, `from None`. Dışarıda hataları yakalayıp context/cause/suppress_context alanlarını göster; tracebackte hangi zincirin görünür olduğunu açıkla.

##### Geçiş ölçütleri

- [ ] Yalın raise context tutar; açık from cause ve suppress_context=True ayarlar.
- [ ] From None görüntüde eski hatayı gizler ama __context__ içinden silmez.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../inheriting-from-built-in-exceptions/README.md)
<!-- learning-task:end -->
