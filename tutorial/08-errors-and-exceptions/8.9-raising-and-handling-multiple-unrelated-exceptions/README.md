## 8.9. Raising and Handling Multiple Unrelated Exceptions

There are situations where it is necessary to report several exceptions that have occurred. This is often the case in concurrency frameworks, when several tasks may have failed in parallel, but there are also other use cases where it is desirable to continue execution and collect multiple errors rather than raise the first exception.

The builtin `ExceptionGroup` wraps a list of exception instances so that they can be raised together. It is an exception itself, so it can be caught like any other exception.

``` python
>>> def f():
...     excs = [OSError('error 1'), SystemError('error 2')]
...     raise ExceptionGroup('there were problems', excs)
...
>>> f()
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 1, in <module>
  |     f()
  |     ~^^
  |   File "<stdin>", line 3, in f
  |     raise ExceptionGroup('there were problems', excs)
  | ExceptionGroup: there were problems (2 sub-exceptions)
  +-+---------------- 1 ----------------
    | OSError: error 1
    +---------------- 2 ----------------
    | SystemError: error 2
    +------------------------------------
>>> try:
...     f()
... except Exception as e:
...     print(f'caught {type(e)}: {e}')
...
caught <class 'ExceptionGroup'>: there were problems (2 sub-exceptions)
>>>
```
> Code: [f.py](f.py)

By using `except*` instead of `except`, we can selectively handle only the exceptions in the group that match a certain type. In the following example, which shows a nested exception group, each `except*` clause extracts from the group exceptions of a certain type while letting all other exceptions propagate to other clauses and eventually to be reraised.

``` python
>>> def f():
...     raise ExceptionGroup(
...         "group1",
...         [
...             OSError(1),
...             SystemError(2),
...             ExceptionGroup(
...                 "group2",
...                 [
...                     OSError(3),
...                     RecursionError(4)
...                 ]
...             )
...         ]
...     )
...
>>> try:
...     f()
... except* OSError as e:
...     print("There were OSErrors")
... except* SystemError as e:
...     print("There were SystemErrors")
...
There were OSErrors
There were SystemErrors
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 2, in <module>
  |     f()
  |     ~^^
  |   File "<stdin>", line 2, in f
  |     raise ExceptionGroup(
  |     ...<12 lines>...
  |     )
  | ExceptionGroup: group1 (1 sub-exception)
  +-+---------------- 1 ----------------
    | ExceptionGroup: group2 (1 sub-exception)
    +-+---------------- 1 ----------------
      | RecursionError: 4
      +------------------------------------
>>>
```
> Code: [f_2.py](f_2.py)

Note that the exceptions nested in an exception group must be instances, not types. This is because in practice the exceptions would typically be ones that have already been raised and caught by the program, along the following pattern:

``` python
>>> excs = []
... for test in tests:
...     try:
...         test.run()
...     except Exception as e:
...         excs.append(e)
...
>>> if excs:
...    raise ExceptionGroup("Test Failures", excs)
...
```
> Code: [excs.py](excs.py)

<!-- learning-task:start -->
### Bölüm görevi

**Görev 8.9: Toplu hatadan yalnız seçilen türleri işle**

**Odak:** ExceptionGroup, iç içe gruplar, except* ve işlenmeyen alt hataların yayılması.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:8.8](../8.8-predefined-clean-up-actions/README.md).

#### Tek görev

1. Bir grupta ValueError("a"), TypeError("b") ve içinde ValueError("c") ile OSError("d") bulunan alt grup oluştur.

2. İlk çalıştırmada except* ValueError, ikinci çalıştırmada ayrıca except* TypeError kullan.

3. Hangi hata yapraklarının işlendiğini ve hangilerinin kalan traceback içinde yer aldığını önceden çıkar.

4. Ayrı bir denemede except Exception ile grubun tamamını yakalamayı karşılaştır.

#### Geçiş ölçütleri

- [ ] İlk denemede a ve c işleniyor; b ve d yayılıyor.
- [ ] İkinci denemede b de işleniyor; d kalıyor.
- [ ] İç içe grup ilişkileri düz ve ilişkisiz hata listesi sanılmamış.
- [ ] except Exception tek grup nesnesini yakalıyor; except* alt türleri seçiyor.
- [ ] Grupta sınıflar yerine hata örnekleri bulunuyor; eşzamanlı yürütme altyapısı gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../8.10-enriching-exceptions-with-notes/README.md)
<!-- learning-task:end -->
