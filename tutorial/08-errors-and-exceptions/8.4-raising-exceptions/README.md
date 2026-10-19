## 8.4. Raising Exceptions

The `raise` statement allows the programmer to force a specified exception to occur. For example:

``` python
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    raise NameError('HiThere')
NameError: HiThere
```
> Code: [example_01.py](example_01.py)

The sole argument to `raise` indicates the exception to be raised. This must be either an exception instance or an exception class (a class that derives from `BaseException`, such as `Exception` or one of its subclasses). If an exception class is passed, it will be implicitly instantiated by calling its constructor with no arguments:

``` python
raise ValueError  # shorthand for 'raise ValueError()'
```
> Code: [example_02.py](example_02.py)

If you need to determine whether an exception was raised but don't intend to handle it, a simpler form of the `raise` statement allows you to re-raise the exception:

``` python
>>> try:
...     raise NameError('HiThere')
... except NameError:
...     print('An exception flew by!')
...     raise
...
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    raise NameError('HiThere')
NameError: HiThere
```
> Code: [example_03.py](example_03.py)

<!-- learning-task:start -->
### Bölüm görevi

**Görev 8.4: Hatayı üret ve üst çağırana aktar**

**Odak:** raise instance/class ve except içinde çıplak raise ile yeniden yükseltme.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:8.3](../8.3-handling-exceptions/README.md).

#### Tek görev

1. Negatif sayı için ValueError("negative count") yükselten check_count(n) yaz; sıfır ve pozitifte sayıyı döndür.

2. Çağıran bir try/except içinde hatayı görüp "checked" mesajı bastıktan sonra çıplak raise ile yeniden aktar. 2 ve -1 durumlarını ayrı çalıştır; ayrıca raise ValueError ile raise ValueError() farkını bölümün kuralıyla açıkla.

#### Geçiş ölçütleri

- [ ] 2 normal dönüyor; -1 aynı hata türü ve mesajıyla üst çağırana ulaşıyor.
- [ ] checked mesajı hata yolunda yeniden raise öncesinde basılıyor.
- [ ] Çıplak raise yeni hata üretmek yerine mevcut hatayı aktarıyor.
- [ ] Sınıf verilirse argümansız örnek oluşturulduğu açıklanmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../8.5-exception-chaining/README.md)
<!-- learning-task:end -->
