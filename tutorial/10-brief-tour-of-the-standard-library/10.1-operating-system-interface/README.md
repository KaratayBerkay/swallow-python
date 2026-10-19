## 10.1. Operating system interface

The `os` module provides dozens of functions for interacting with the operating system:

``` python
>>> import os
>>> os.getcwd()      # Return the current working directory
'C:\\Python315'
>>> os.chdir('/server/accesslogs')   # Change current working directory
>>> os.system('mkdir today')   # Run the command mkdir in the system shell
0
```
> Code: [os_example.py](os_example.py)

Be sure to use the `import os` style instead of `from os import *`. This will keep `os.open()` from shadowing the built-in `open()` function which operates much differently.

The built-in `dir()` and `help()` functions are useful as interactive aids for working with large modules like `os`:

``` python
>>> import os
>>> dir(os)
<returns a list of all module functions>
>>> help(os)
<returns an extensive manual page created from the module's docstrings>
```
> Code: [os_2.py](os_2.py)

For daily file and directory management tasks, the `shutil` module provides a higher-level interface that is easier to use:

``` python
>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
'archive.db'
>>> shutil.move('/build/executables', 'installdir')
'installdir'
```
> Code: [shutil_example.py](shutil_example.py)

<!-- learning-task:start -->
### Bölüm görevi

**Görev 10.1: Dosya işlemini doğru arayüzle eşleştir**

**Odak:** os ile çalışma dizini, nitelikli import, help/dir ve shutil copy/move.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:7.2](../../07-input-and-output/7.2-reading-and-writing-files/README.md).
- Ön bilgi: [t:6.3](../../06-modules/6.3-the-dir-function/README.md).

#### Tek görev

1. Kendi geçici çalışma klasöründe source.txt ve dest alt klasörünü hazırla. os.getcwd ile konumu kaydet; shutil.copyfile ile source.txt dosyasını copy.txt olarak kopyala, ardından shutil.move ile copy.txt dosyasını dest içine taşı.

2. Sonuçları open ile okuyarak karşılaştır. os.chdir örneğinin sonraki göreli dosya adlarını nasıl etkilediğini ve os.system("mkdir today") satırının ne yaptığını yazılı izle. help(os) ile dir(os) amaçlarını ayır.

#### Geçiş ölçütleri

- [ ] Asıl source.txt korunuyor; taşınan kopya dest içinde aynı içeriğe sahip.
- [ ] Kopyalama ile taşıma farkı yalnız mesajdan değil dosyaların son yerlerinden gösterilmiş.
- [ ] Çalışma dizini değişimi göreli dosya aramasını etkiliyor; shell komutu Python ifadesi sanılmamış.
- [ ] import os biçiminin os.open ile built-in open karışmasını önlediği açıklanmış; sistem dizinlerine yazılmamış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../10.2-file-wildcards/README.md)
<!-- learning-task:end -->
