## 6.2. Standard Modules

Python comes with a library of standard modules, described in a separate document, the Python Library Reference ("Library Reference" hereafter). Some modules are built into the interpreter; these provide access to operations that are not part of the core of the language but are nevertheless built in, either for efficiency or to provide access to operating system primitives such as system calls. The set of such modules is a configuration option which also depends on the underlying platform. For example, the `winreg` module is only provided on Windows systems. One particular module deserves some attention: `sys`, which is built into every Python interpreter. The variables `sys.ps1` and `sys.ps2` define the strings used as primary and secondary prompts:

``` python
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>
```
> Code: [sys_example.py](sys_example.py)

These two variables are only defined if the interpreter is in interactive mode.

The variable `sys.path` is a list of strings that determines the interpreter's search path for modules. It is initialized to a default path taken from the environment variable `PYTHONPATH`, or from a built-in default if `PYTHONPATH` is not set. You can modify it using standard list operations:

``` python
>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')
```
> Code: [sys_2.py](sys_2.py)

<!-- learning-task:start -->
### Bölüm görevi

**Görev 6.2: Yorumlayıcının standart modülünü kullan**

**Odak:** Standart/built-in modül, platform farkı, sys.ps1/ps2 ve sys.path listesi.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:6.1.2](../6.1-more-on-modules/6.1.2-the-module-search-path/README.md).

#### Tek görev

1. Yeni bir REPL oturumunda sys.ps1 ve sys.ps2 değerlerini not et; birincil istemi "study> " yapıp tekrar eski haline getir.

2. Aynı adlara bir betikten erişmenin neden aynı varsayıma dayanamayacağını açıkla. sys.path listesinin kopyasına "/lesson/modules" ekleyip modül arama yolunun metinlerden oluştuğunu göster. winreg örneğini platforma göre sınıflandır.

#### Geçiş ölçütleri

- [ ] İstem değişikliği yalnız açık oturumda uygulanmış ve geri alınmış.
- [ ] ps1/ps2 etkileşimli oturum niteliği; betikte bulunması varsayılmamış.
- [ ] Yol ekleme liste işlemi olarak açıklanmış; kurulum ayarı değiştirilmemiş.
- [ ] Standart kütüphanede olmak her platformda aynı modülün bulunacağı anlamına gelmiyor; sys built-in olarak ayrılmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../6.3-the-dir-function/README.md)
<!-- learning-task:end -->
