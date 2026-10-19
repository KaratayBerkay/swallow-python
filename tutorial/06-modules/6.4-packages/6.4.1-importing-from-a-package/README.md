### 6.4.1. Importing \* From a Package

Now what happens when the user writes `from sound.effects import *`? Ideally, one would hope that this somehow goes out to the filesystem, finds which submodules are present in the package, and imports them all. This could take a long time and importing sub-modules might have unwanted side-effects that should only happen when the sub-module is explicitly imported.

The only solution is for the package author to provide an explicit index of the package. The `import` statement uses the following convention: if a package's `__init__.py` code defines a list named `__all__`, it is taken to be the list of module names that should be imported when `from package import *` is encountered. It is up to the package author to keep this list up-to-date when a new version of the package is released. Package authors may also decide not to support it, if they don't see a use for importing \* from their package. For example, the file `sound/effects/__init__.py` could contain the following code:

``` python
__all__ = ["echo", "surround", "reverse"]
```
> Code: [all.py](all.py)

This would mean that `from sound.effects import *` would import the three named submodules of the `sound.effects` package.

Be aware that submodules might become shadowed by locally defined names. For example, if you added a `reverse` function to the `sound/effects/__init__.py` file, the `from sound.effects import *` would only import the two submodules `echo` and `surround`, but *not* the `reverse` submodule, because it is shadowed by the locally defined `reverse` function:

``` python
__all__ = [
    "echo",      # refers to the 'echo.py' file
    "surround",  # refers to the 'surround.py' file
    "reverse",   # !!! refers to the 'reverse' function now !!!
]

def reverse(msg: str):  # <-- this name shadows the 'reverse.py' submodule
    return msg[::-1]    #     in the case of a 'from sound.effects import *'
```
> Code: [reverse.py](reverse.py)

If `__all__` is not defined, the statement `from sound.effects import *` does *not* import all submodules from the package `sound.effects` into the current namespace; it only ensures that the package `sound.effects` has been imported (possibly running any initialization code in `__init__.py`) and then imports whatever names are defined in the package. This includes any names defined (and submodules explicitly loaded) by `__init__.py`. It also includes any submodules of the package that were explicitly loaded by previous `import` statements. Consider this code:

``` python
import sound.effects.echo
import sound.effects.surround
from sound.effects import *
```
> Code: [sound.py](sound.py)

In this example, the `echo` and `surround` modules are imported in the current namespace because they are defined in the `sound.effects` package when the `from...import` statement is executed. (This also works when `__all__` is defined.)

Although certain modules are designed to export only names that follow certain patterns when you use `import *`, it is still considered bad practice in production code.

Remember, there is nothing wrong with using `from package import specific_submodule`! In fact, this is the recommended notation unless the importing module needs to use submodules with the same name from different packages.

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 6.4.1: Yıldızlı aktarımın sınırını gör**

**Odak:** `__all__`, kendiliğinden alt modül taramama, önceden yüklenen adlar ve isim gölgeleme.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:6.4](../README.md).

##### Tek görev

1. Kendi lessonpack/tools paketinin kopyasında `__all__` = ["counts"] tanımla; from lessonpack.tools import * sonrasında gelen adı kontrol et.

2. Sonra `__all__` kaldırılmış, başlangıç dosyası boş bir kopyada aynı deneyi yeni oturumda yap; counts açıkça import edildikten sonraki durumu karşılaştır.

3. Üçüncü kopyada counts adlı bir fonksiyon tanımlayıp `__all__` içine counts ekle; modül yerine hangi nesnenin geleceğini izle.

##### Geçiş ölçütleri

- [ ] `__all__` varsa counts adı dışarı aktarılıyor.
- [ ] Boş başlangıç dosyası ve `__all__` yokken diskteki bütün modüller taranıp aktarılmıyor.
- [ ] Önceden yüklenen alt modül paket adı alanında bulunduğu için sonraki * kapsamına girebiliyor.
- [ ] Aynı adlı fonksiyon modülü gölgeleyebiliyor; belirli adı açıkça import etmenin yararı açıklanmış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../6.4.2-intra-package-references/README.md)
<!-- learning-task:end -->
