## 8.10. Enriching Exceptions with Notes

When an exception is created in order to be raised, it is usually initialized with information that describes the error that has occurred. There are cases where it is useful to add information after the exception was caught. For this purpose, exceptions have a method `add_note(note)` that accepts a string and adds it to the exception's notes list. The standard traceback rendering includes all notes, in the order they were added, after the exception.

``` python
>>> try:
...     raise TypeError('bad type')
... except Exception as e:
...     e.add_note('Add some information')
...     e.add_note('Add some more information')
...     raise
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    raise TypeError('bad type')
TypeError: bad type
Add some information
Add some more information
>>>
```
> Code: [example_01.py](example_01.py)

For example, when collecting exceptions into an exception group, we may want to add context information for the individual errors. In the following each exception in the group has a note indicating when this error has occurred.

``` python
>>> def f():
...     raise OSError('operation failed')
...
>>> excs = []
>>> for i in range(3):
...     try:
...         f()
...     except Exception as e:
...         e.add_note(f'Happened in Iteration {i+1}')
...         excs.append(e)
...
>>> raise ExceptionGroup('We have some problems', excs)
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 1, in <module>
  |     raise ExceptionGroup('We have some problems', excs)
  | ExceptionGroup: We have some problems (3 sub-exceptions)
  +-+---------------- 1 ----------------
    | Traceback (most recent call last):
    |   File "<stdin>", line 3, in <module>
    |     f()
    |     ~^^
    |   File "<stdin>", line 2, in f
    |     raise OSError('operation failed')
    | OSError: operation failed
    | Happened in Iteration 1
    +---------------- 2 ----------------
    | Traceback (most recent call last):
    |   File "<stdin>", line 3, in <module>
    |     f()
    |     ~^^
    |   File "<stdin>", line 2, in f
    |     raise OSError('operation failed')
    | OSError: operation failed
    | Happened in Iteration 2
    +---------------- 3 ----------------
    | Traceback (most recent call last):
    |   File "<stdin>", line 3, in <module>
    |     f()
    |     ~^^
    |   File "<stdin>", line 2, in f
    |     raise OSError('operation failed')
    | OSError: operation failed
    | Happened in Iteration 3
    +------------------------------------
>>>
```
> Code: [f.py](f.py)

<!-- learning-task:start -->
### Bölüm görevi

**Görev 8.10: Hatanın kimliğini koruyup bağlam ekle**

**Odak:** add_note, eklenme sırası, yeniden yükseltme ve grup içindeki yerel bağlam.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:8.9](../8.9-raising-and-handling-multiple-unrelated-exceptions/README.md).

#### Tek görev

1. İki farklı sayı dönüşümünde oluşan ValueError hatalarını listeye topla.

2. Her hataya önce hangi girdiye ait olduğunu, sonra "count import" işlemini belirten iki not ekle.

3. Sonunda ExceptionGroup ile yükselt.

4. Hata türü/mesajı ile notların konum ve sırasını incele; tek hata için çıplak raise ile aynı notların korunmasını ayrıca göster.

#### Geçiş ölçütleri

- [ ] Her alt hatanın kendi girdi notu var; notlar yanlış hataya taşınmamış.
- [ ] İki not eklenme sırasıyla hata mesajından sonra görünüyor.
- [ ] Asıl ValueError türü ve mesajı korunuyor.
- [ ] Not ekleme ile yeni exception oluşturarak hata çevirme arasındaki fark açıklanmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
