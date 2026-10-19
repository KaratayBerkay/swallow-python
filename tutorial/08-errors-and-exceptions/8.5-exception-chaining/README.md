## 8.5. Exception Chaining

If an unhandled exception occurs inside an `except` section, it will have the exception being handled attached to it and included in the error message:

``` python
>>> try:
...     open("database.sqlite")
... except OSError:
...     raise RuntimeError("unable to handle error")
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    open("database.sqlite")
    ~~~~^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'database.sqlite'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
    raise RuntimeError("unable to handle error")
RuntimeError: unable to handle error
```
> Code: [example_01.py](example_01.py)

To indicate that an exception is a direct consequence of another, the `raise` statement allows an optional `from` clause:

``` python
# exc must be exception instance or None.
raise RuntimeError from exc
```
> Code: [example_02.py](example_02.py)

This can be useful when you are transforming exceptions. For example:

``` python
>>> def func():
...     raise ConnectionError
...
>>> try:
...     func()
... except ConnectionError as exc:
...     raise RuntimeError('Failed to open database') from exc
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    func()
    ~~~~^^
  File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
    raise RuntimeError('Failed to open database') from exc
RuntimeError: Failed to open database
```
> Code: [func.py](func.py)

It also allows disabling automatic exception chaining using the `from None` idiom:

``` python
>>> try:
...     open('database.sqlite')
... except OSError:
...     raise RuntimeError from None
...
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
    raise RuntimeError from None
RuntimeError
```
> Code: [example_03.py](example_03.py)

For more information about chaining mechanics, see Built-in Exceptions.

<!-- learning-task:start -->
### Bölüm görevi

**Görev 8.5: Hata çevirisinin nedenini görünür kıl**

**Odak:** Örtük zincir, from exc ile açık neden ve from None ile zinciri göstermeme.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:8.4](../8.4-raising-exceptions/README.md).

#### Tek görev

1. int("bad") hatasını yakalayıp RuntimeError("invalid count") üreten üç ayrı sürüm yaz: doğrudan raise, raise ... from exc ve raise ... from None.

2. Her birini ayrı çalıştır ve traceback içinde görünen hata bölümleriyle aralarındaki ilişkiyi karşılaştır.

#### Geçiş ölçütleri

- [ ] Üç sürümün son hatası RuntimeError.
- [ ] Doğrudan raise örtük bağlamı, from exc açık nedeni gösteriyor.
- [ ] from None çıktıda önceki bağlam zincirini göstermiyor; önceki işlemin gerçekleşmediği sanılmamış.
- [ ] Hata çevirisinin hangi düşük seviye işlemi hangi uygulama hatasına bağladığı açıklanmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../8.6-user-defined-exceptions/README.md)
<!-- learning-task:end -->
