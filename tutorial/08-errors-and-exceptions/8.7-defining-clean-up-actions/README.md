## 8.7. Defining Clean-up Actions

The `try` statement has another optional clause which is intended to define clean-up actions that must be executed under all circumstances. For example:

``` python
>>> try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
...
Goodbye, world!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    raise KeyboardInterrupt
KeyboardInterrupt
```
> Code: [example_01.py](example_01.py)

If a `finally` clause is present, the `finally` clause will execute as the last task before the `try` statement completes. The `finally` clause runs whether or not the `try` statement produces an exception. The following points discuss more complex cases when an exception occurs:

- If an exception occurs during execution of the `try` clause, the exception may be handled by an `except` clause. If the exception is not handled by an `except` clause, the exception is re-raised after the `finally` clause has been executed.

- An exception could occur during execution of an `except` or `else` clause. Again, the exception is re-raised after the `finally` clause has been executed.

- If the `finally` clause executes a `break`, `continue` or `return` statement, exceptions are not re-raised. This can be confusing and is therefore discouraged. From version 3.14 the compiler emits a `SyntaxWarning` for it (see [**PEP 765**](https://peps.python.org/pep-0765/)).

- If the `try` statement reaches a `break`, `continue` or `return` statement, the `finally` clause will execute just prior to the `break`, `continue` or `return` statement's execution.

- If a `finally` clause includes a `return` statement, the returned value will be the one from the `finally` clause's `return` statement, not the value from the `try` clause's `return` statement. This can be confusing and is therefore discouraged. From version 3.14 the compiler emits a `SyntaxWarning` for it (see [**PEP 765**](https://peps.python.org/pep-0765/)).

For example:

``` python
>>> def bool_return():
...     try:
...         return True
...     finally:
...         return False
...
>>> bool_return()
False
```
> Code: [bool_return.py](bool_return.py)

A more complicated example:

``` python
>>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")
...
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    divide("2", "1")
    ~~~~~~^^^^^^^^^^
  File "<stdin>", line 3, in divide
    result = x / y
             ~~^~~
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```
> Code: [divide.py](divide.py)

As you can see, the `finally` clause is executed in any event. The `TypeError` raised by dividing two strings is not handled by the `except` clause and therefore re-raised after the `finally` clause has been executed.

In real world applications, the `finally` clause is useful for releasing external resources (such as files or network connections), regardless of whether the use of the resource was successful.

<!-- learning-task:start -->
### Bölüm görevi

**Görev 8.7: Temizliği bütün çıkış yollarında izle**

**Odak:** finally ile normal/hatalı çıkış, return ve hata bastırma riski.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:8.5](../8.5-exception-chaining/README.md).

#### Tek görev

1. README içindeki divide örneğinin kopyasında her bölüme farklı kısa bir işaret koy. (6, 2), (6, 0) ve ("6", "2") için try/except/else/finally sırasını önce çıkar, sonra çalıştır.

2. Ayrı bir fonksiyonda try içinden 1 döndür; finally yalnız mesaj bassın.

3. Sonra finally içine return 2 ekle ve dönen değer ile bir hata durumuna etkisini karşılaştır.

#### Geçiş ölçütleri

- [ ] Normal yol else ve finally; sıfır yolunda except ve finally; tip hatasında finally sonrası yayılma.
- [ ] finally temizliği hatayı kendiliğinden çözmüyor.
- [ ] Yalnız mesajlı finally dönüş 1 değerini koruyor; return 2 eklenince sonuç 2.
- [ ] finally içindeki return hatayı da bastırabilir; bu yüzden temizliğe kontrol akışı ekleme riski açıklanmış.
- [ ] 3.14+ SyntaxWarning farkı bölümdeki sürüm notuyla ayrılmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../8.8-predefined-clean-up-actions/README.md)
<!-- learning-task:end -->
