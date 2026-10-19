## 10.6. Mathematics

The `math` module gives access to the underlying C library functions for floating-point math:

``` python
>>> import math
>>> math.cos(math.pi / 4)
0.70710678118654757
>>> math.log(1024, 2)
10.0
```
> Code: [math_example.py](math_example.py)

The `random` module provides tools for making random selections:

``` python
>>> import random
>>> random.choice(['apple', 'pear', 'banana'])
'apple'
>>> random.sample(range(100), 10)   # sampling without replacement
[30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
>>> random.random()    # random float from the interval [0.0, 1.0)
0.17970987693706186
>>> random.randrange(6)    # random integer chosen from range(6)
4
```
> Code: [random_example.py](random_example.py)

The `statistics` module calculates basic statistical properties (the mean, median, variance, etc.) of numeric data:

``` python
>>> import statistics
>>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
>>> statistics.mean(data)
1.6071428571428572
>>> statistics.median(data)
1.25
>>> statistics.variance(data)
1.3720238095238095
```
> Code: [data.py](data.py)

The SciPy project \<[https://scipy.org](https://scipy.org)\> has many other modules for numerical computations.

<!-- learning-task:start -->
### Bölüm görevi

**Görev 10.6: Kesin hesapla rastgele seçimin ölçütlerini ayır**

**Odak:** math, random seçim araçları ve statistics mean/median/variance.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:10.5](../10.5-string-pattern-matching/README.md).

#### Tek görev

1. math.log(32, 2) ile 2 tabanındaki hesabı, [1, 2, 3] için mean/median/variance değerlerini hesapla.

2. Ardından üç etiket içinden choice, range(10) içinden 3 öğelik sample, random() ve randrange(4) üret.

3. Rastgele sonuçlarda belirli sayıyı beklemek yerine hangi özelliklerin doğru olması gerektiğini tek tek yaz.

#### Geçiş ölçütleri

- [ ] Logaritma 5.0; mean 2, median 2, örneklem variance 1.
- [ ] choice verilen etiketlerden; sample üç farklı 0..9 öğesi.
- [ ] random sonucu 0 dahil 1 hariç; randrange sonucu 0..3.
- [ ] Tekrar çalıştırınca değer değişmesinin başarısızlık sayılmayacağı; sample için tekrarsızlık ayrımı açıklanmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../10.7-internet-access/README.md)
<!-- learning-task:end -->
