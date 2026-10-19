## 10.11. Quality control

One approach for developing high quality software is to write tests for each function as it is developed and to run those tests frequently during the development process.

The `doctest` module provides a tool for scanning a module and validating tests embedded in a program's docstrings. Test construction is as simple as cutting-and-pasting a typical call along with its results into the docstring. This improves the documentation by providing the user with an example and it allows the doctest module to make sure the code remains true to the documentation:

``` python
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests
```
> Code: [average.py](average.py)

The `unittest` module is not as effortless as the `doctest` module, but it allows a more comprehensive set of tests to be maintained in a separate file:

``` python
import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()  # Calling from the command line invokes all tests
```
> Code: [test_average.py](test_average.py)

<!-- learning-task:start -->
### Bölüm görevi

**Görev 10.11: Davranış bozulunca testin yakaladığını göster**

**Odak:** doctest ve unittest, normal sonuç, istisna ve başarısız testin tanı değeri.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:10.10](../10.10-performance-measurement/README.md).
- Ön bilgi: [t:9.5](../../09-classes/9.5-inheritance/README.md).

#### Tek görev

1. README içindeki average işlevi için [2, 4] sonucunu gösteren docstring testi yazıp doctest.testmod ile çalıştır.

2. Ayrı test dosyasında unittest ile aynı normal sonucu ve boş listede ZeroDivisionError beklentisini sınat.

3. Sonra average kopyasının paydasına yanlışlıkla +1 ekleyerek hem doctest hem unittestin bunu yakaladığını göster; doğru sürüme geri dön.

#### Geçiş ölçütleri

- [ ] Doğru sürümde doctest ve unittest geçiyor.
- [ ] Bozuk sürümde normal sonuç testleri gerçekten başarısız oluyor; yalnız çalıştırılmış olmaları başarı sayılmamış.
- [ ] Boş liste davranışı assertRaises ile kontrol edilmiş.
- [ ] Beklenen sonuç koddan kopyalanmadan bağımsız hesaplanmış; son sürüm tekrar geçiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../10.12-batteries-included/README.md)
<!-- learning-task:end -->
