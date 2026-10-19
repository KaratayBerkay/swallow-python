### 5.2.1. Regular packages

Python defines two types of packages, regular packages and namespace packages. Regular packages are traditional packages as they existed in Python 3.2 and earlier. A regular package is typically implemented as a directory containing an `__init__.py` file. When a regular package is imported, this `__init__.py` file is implicitly executed, and the objects it defines are bound to names in the package's namespace. The `__init__.py` file can contain the same Python code that any other module can contain, and Python will add some additional attributes to the module when it is imported.

For example, the following file system layout defines a top level `parent` package with three subpackages:

``` python
parent/
    __init__.py
    one/
        __init__.py
    two/
        __init__.py
    three/
        __init__.py
```
> Code: [example_01.py](example_01.py)

Importing `parent.one` will implicitly execute `parent/__init__.py` and `parent/one/__init__.py`. Subsequent imports of `parent.two` or `parent.three` will execute `parent/two/__init__.py` and `parent/three/__init__.py` respectively.

A subdirectory inside a regular package that does not contain an `__init__.py` file is treated as an implicit namespace package (a "namespace subpackage") rooted in that parent. See [**PEP 420**](https://peps.python.org/pep-0420/) for the underlying specification.

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 5.2.1: Paket başlatıcılarının yürütme sırasını çıkar**

**Odak:** Regular paket `__init__` yürütmesi, ebeveyn içe aktarımı ve ayrı alt paketler.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.2](../README.md).

##### Tek görev

1. Bölümdeki parent/one/two/three ağacının çalışma kopyasında her `__init__`.py içine kendi adını yazdıran tek satır ekle.

2. Aynı oturumda parent.one, parent.two ve tekrar parent.one içe aktar.

3. Mesaj sırasını ve her başlatıcının kaç kez çalışacağını önce çıkar, sonra gözlemle.

##### Geçiş ölçütleri

- [ ] İlk import parent sonra parent.one başlatıcılarını yürütüyor.
- [ ] İkinci import yalnız parent.two başlatıcısını ilk kez yürütüyor.
- [ ] Tekrar parent.one yeni başlangıç yürütmesi yapmıyor.
- [ ] three açıkça istenmediği için çalışmıyor; alt klasörde `__init__` yokluğu otomatik regular paket sayılmamış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../5.2.2-namespace-packages/README.md)
<!-- learning-task:end -->
