### 16.1.3. The Interactive Startup File

When you use Python interactively, it is frequently handy to have some standard commands executed every time the interpreter is started. You can do this by setting an environment variable named `PYTHONSTARTUP` to the name of a file containing your start-up commands. This is similar to the `.profile` feature of the Unix shells.

This file is only read in interactive sessions, not when Python reads commands from a script, and not when `/dev/tty` is given as the explicit source of commands (which otherwise behaves like an interactive session). It is executed in the same namespace where interactive commands are executed, so that objects that it defines or imports can be used without qualification in the interactive session. You can also change the prompts `sys.ps1` and `sys.ps2` in this file.

If you want to read an additional start-up file from the current directory, you can program this in the global start-up file using code like `if os.path.isfile('.pythonrc.py'): exec(open('.pythonrc.py').read())`. If you want to use the startup file in a script, you must do this explicitly in the script:

``` python
import os
filename = os.environ.get('PYTHONSTARTUP')
if filename and os.path.isfile(filename):
    with open(filename) as fobj:
        startup_file = fobj.read()
    exec(startup_file)
```
> Code: [filename.py](filename.py)

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 16.1.3: Başlangıç dosyasının hangi oturumda çalışacağını çıkar**

**Odak:** PYTHONSTARTUP, aynı namespace, etkileşimli/betik farkı ve açık yükleme.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:16.1.2](../16.1.2-executable-python-scripts/README.md).
- Ön bilgi: [t:6.2](../../../06-modules/6.2-standard-modules/README.md).

##### Tek görev

1. Yerel bir startup taslağına marker = "ready" yaz.

2. Değişiklik yapmadan üç çalıştırmanın izini çıkar: PYTHONSTARTUP bu dosyayı gösterirken etkileşimli başlangıç; normal betik çalıştırma; README içindeki açık dosya okuma/exec iskeletini içeren betik. marker hangi durumda kullanılabilir?

3. Dosya yolu tanımlı değilken veya dosya yokken iskeletin ne yaptığını da açıkla.

##### Geçiş ölçütleri

- [ ] Normal etkileşimli başlangıç marker bağını aynı namespace içine ekliyor.
- [ ] Normal betik başlangıç dosyasını kendiliğinden çalıştırmıyor; açık yükleyen betik çalıştırıyor.
- [ ] Dosya tanımsız/yoksa koşullu gövdeye girilmiyor.
- [ ] İstemlerin de bu dosyada değiştirilebildiği ve /dev/tty istisnası belirtilmiş; shell profiline kalıcı ayar yazılmamış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../16.1.4-the-customization-modules/README.md)
<!-- learning-task:end -->
