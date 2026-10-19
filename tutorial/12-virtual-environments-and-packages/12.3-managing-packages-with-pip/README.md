## 12.3. Managing Packages with pip

You can install, upgrade, and remove packages using a program called **pip**. By default `pip` will install packages from the [Python Package Index](https://pypi.org). You can browse the Python Package Index by going to it in your web browser.

`pip` has a number of subcommands: "install", "uninstall", "freeze", etc. (Consult the Installing Python modules guide for complete documentation for `pip`.)

You can install the latest version of a package by specifying a package's name:

``` console
(tutorial-env) $ python -m pip install novas
Collecting novas
  Downloading novas-3.1.1.3.tar.gz (136kB)
Installing collected packages: novas
  Running setup.py install for novas
Successfully installed novas-3.1.1.3
```

You can also install a specific version of a package by giving the package name followed by `==` and the version number:

``` console
(tutorial-env) $ python -m pip install requests==2.6.0
Collecting requests==2.6.0
  Using cached requests-2.6.0-py2.py3-none-any.whl
Installing collected packages: requests
Successfully installed requests-2.6.0
```

If you re-run this command, `pip` will notice that the requested version is already installed and do nothing. You can supply a different version number to get that version, or you can run `python -m pip install --upgrade` to upgrade the package to the latest version:

``` console
(tutorial-env) $ python -m pip install --upgrade requests
Collecting requests
Installing collected packages: requests
  Found existing installation: requests 2.6.0
    Uninstalling requests-2.6.0:
      Successfully uninstalled requests-2.6.0
Successfully installed requests-2.7.0
```

`python -m pip uninstall` followed by one or more package names will remove the packages from the virtual environment.

`python -m pip show` will display information about a particular package:

``` console
(tutorial-env) $ python -m pip show requests
---
Metadata-Version: 2.0
Name: requests
Version: 2.7.0
Summary: Python HTTP for Humans.
Home-page: http://python-requests.org
Author: Kenneth Reitz
Author-email: me@kennethreitz.com
License: Apache 2.0
Location: /Users/akuchling/envs/tutorial-env/lib/python3.4/site-packages
Requires:
```

`python -m pip list` will display all of the packages installed in the virtual environment:

``` console
(tutorial-env) $ python -m pip list
novas (3.1.1.3)
numpy (1.9.2)
pip (7.0.3)
requests (2.7.0)
setuptools (16.0)
```

`python -m pip freeze` will produce a similar list of the installed packages, but the output uses the format that `python -m pip install` expects. A common convention is to put this list in a `requirements.txt` file:

``` console
(tutorial-env) $ python -m pip freeze > requirements.txt
(tutorial-env) $ cat requirements.txt
novas==3.1.1.3
numpy==1.9.2
requests==2.7.0
```

The `requirements.txt` can then be committed to version control and shipped as part of an application. Users can then install all the necessary packages with `install -r`:

``` console
(tutorial-env) $ python -m pip install -r requirements.txt
Collecting novas==3.1.1.3 (from -r requirements.txt (line 1))
  ...
Collecting numpy==1.9.2 (from -r requirements.txt (line 2))
  ...
Collecting requests==2.7.0 (from -r requirements.txt (line 3))
  ...
Installing collected packages: novas, numpy, requests
  Running setup.py install for novas
Successfully installed novas-3.1.1.3 numpy-1.9.2 requests-2.7.0
```

`pip` has many more options. Consult the Installing Python modules guide for complete documentation for `pip`. When you've written a package and want to make it available on the Python Package Index, consult the [Python packaging user guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/).

<!-- learning-task:start -->
### Bölüm görevi

**Görev 12.3: Paket değişiminin planını ve kanıtını yaz**

**Odak:** pip install/pin/upgrade/uninstall, show/list/freeze ve requirements ile yeniden kurma.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:12.2](../12.2-creating-virtual-environments/README.md).

#### Tek görev

1. Ağ veya kurulum çalıştırmadan, docs içindeki paket adlarını kullanarak bir komut planı hazırla: requests için tam sürüm kur; aynı sürümü yeniden iste; en yeni sürüme yükselt; show/list ile gözle; freeze çıktısını requirements.txt olarak sakla; ikinci ortamda bu dosyadan kur; ilk ortamdan requests kaldır.

2. Her komutun beklenen etkisini ve etkisiz kalabileceği durumu yaz. requirements taslağı için docs içindeki örnek verileri kullan; güncel sürüm olduklarını iddia etme.

#### Geçiş ölçütleri

- [ ] Tam sürüm == ile; yükseltme --upgrade ile; dosyadan kurma -r ile.
- [ ] Aynı sürüm zaten varsa yeniden isteğin değişiklik gerektirmeyebileceği açıklanmış.
- [ ] show paket bilgisi, list kurulu paket görünümü, freeze yeniden kurulabilir sürüm satırları olarak ayrılmış.
- [ ] uninstall yalnız seçilen ortama yönelik; yorumlayıcı seçimi python -m pip üzerinden.
- [ ] Eski örnek sürümler güncel öneri veya gerçekten kurulmuş paket gibi sunulmamış; paket yayımlama yok.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
