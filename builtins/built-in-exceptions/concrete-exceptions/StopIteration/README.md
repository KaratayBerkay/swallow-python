## `StopIteration`

```
StopIteration
```

Raised by built-in function [next()](../../../built-in-functions/next/README.md) and an [iterator](https://docs.python.org/3.15/glossary.html#term-iterator)'s
[__next__()](https://docs.python.org/3.15/builtins/stdtypes.html#iterator.__next__) method to signal that there are no further
items produced by the iterator.

### StopIteration.value

The exception object has a single attribute `value`, which is
given as an argument when constructing the exception, and defaults
to [None](https://docs.python.org/3.15/builtins/constants.html#None).

When a [generator](https://docs.python.org/3.15/glossary.html#term-generator) or [coroutine](https://docs.python.org/3.15/glossary.html#term-coroutine) function
returns, a new StopIteration instance is
raised, and the value returned by the function is used as the
`value` parameter to the constructor of the exception.

If a generator code directly or indirectly raises StopIteration,
it is converted into a [RuntimeError](../RuntimeError/README.md) (retaining the
StopIteration as the new exception's cause).

> *Changed in version 3.3:* Added `value` attribute and the ability for generator functions to
> use it to return a value.

> *Changed in version 3.5:* Introduced the RuntimeError transformation via
> `from __future__ import generator_stop`, see [PEP 479](https://peps.python.org/pep-479/).

> *Changed in version 3.7:* Enable [PEP 479](https://peps.python.org/pep-479/) for all code by default: a StopIteration
> error raised in a generator is transformed into a [RuntimeError](../RuntimeError/README.md).

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.4.21: Dönüş değerini tükenme hatasından oku**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Bir generator önce yield 4 sonra return 9 yapsın; sonraki next çağrısında yakalanan StopIteration.value değerini bul. Ayrı generator içinde açıkça raise StopIteration(9) yapmayı karşılaştır.

#### Geçiş ölçütleri

- [ ] Return durumunda value=9 olan StopIteration tüketiciye ulaşır.
- [ ] Generator içinde açık StopIteration, cause alanında asıl hata korunarak RuntimeError durumuna dönüşür.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../StopAsyncIteration/README.md)
<!-- learning-task:end -->
