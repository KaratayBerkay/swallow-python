## 6.4. Packages

Packages are a way of structuring Python's module namespace by using "dotted module names". For example, the module name `A.B` designates a submodule named `B` in a package named `A`. Just like the use of modules saves the authors of different modules from having to worry about each other's global variable names, the use of dotted module names saves the authors of multi-module packages like NumPy or Pillow from having to worry about each other's module names.

Suppose you want to design a collection of modules (a "package") for the uniform handling of sound files and sound data. There are many different sound file formats (usually recognized by their extension, for example: `.wav`, `.aiff`, `.au`), so you may need to create and maintain a growing collection of modules for the conversion between the various file formats. There are also many different operations you might want to perform on sound data (such as mixing, adding echo, applying an equalizer function, creating an artificial stereo effect), so in addition you will be writing a never-ending stream of modules to perform these operations. Here's a possible structure for your package (expressed in terms of a hierarchical filesystem):

``` text
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

When importing the package, Python searches through the directories on `sys.path` looking for the package subdirectory.

The `__init__.py` files are required to make Python treat directories containing the file as packages (unless using a namespace package, a relatively advanced feature). This prevents directories with a common name, such as `string`, from unintentionally hiding valid modules that occur later on the module search path. In the simplest case, `__init__.py` can just be an empty file, but it can also execute initialization code for the package or set the `__all__` variable, described later.

Users of the package can import individual modules from the package, for example:

``` python
import sound.effects.echo
```
> Code: [sound.py](sound.py)

This loads the submodule `sound.effects.echo`. It must be referenced with its full name.

``` python
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
```
> Code: [example_01.py](example_01.py)

An alternative way of importing the submodule is:

``` python
from sound.effects import echo
```
> Code: [echo.py](echo.py)

This also loads the submodule `echo`, and makes it available without its package prefix, so it can be used as follows:

``` python
echo.echofilter(input, output, delay=0.7, atten=4)
```
> Code: [example_02.py](example_02.py)

Yet another variation is to import the desired function or variable directly:

``` python
from sound.effects.echo import echofilter
```
> Code: [echofilter.py](echofilter.py)

Again, this loads the submodule `echo`, but this makes its function `echofilter()` directly available:

``` python
echofilter(input, output, delay=0.7, atten=4)
```
> Code: [example_03.py](example_03.py)

Note that when using `from package import item`, the item can be either a submodule (or subpackage) of the package, or some other name defined in the package, like a function, class or variable. The `import` statement first tests whether the item is defined in the package; if not, it assumes it is a module and attempts to load it. If it fails to find it, an `ImportError` exception is raised.

Contrarily, when using syntax like `import item.subitem.subsubitem`, each item except for the last must be a package; the last item can be a module or a package but can't be a class or function or variable defined in the previous item.


<!-- learning-task:start -->
### Bölüm görevi

**Görev 6.4: Paket yolunu çağrı biçimiyle eşleştir**

**Odak:** Paket ağacı, `__init__`.py, noktalı adlar ve üç import biçiminin ad bağlaması.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:6.3](../6.3-the-dir-function/README.md).

#### Tek görev

1. Çalışma klasöründe lessonpack/ ve lessonpack/tools/ paketlerini boş `__init__`.py dosyalarıyla kur. tools/counts.py içinde count_items(items) olsun.

2. Ayrı oturumlarda import lessonpack.tools.counts, from lessonpack.tools import counts, from lessonpack.tools.counts import count_items biçimlerini kullanıp aynı iki öğenin sayısını al.

3. Her çağrıda kullanılabilir adı yaz ve README içindeki sound ağacına eşleştir.

#### Geçiş ölçütleri

- [ ] Üç çağrı da 2 veriyor; tam yol, modül adı ve doğrudan işlev adı doğru kullanılmış.
- [ ] Her ara bileşen paket; son bileşen modül olabiliyor.
- [ ] `__init__`.py regular paket başlatma dosyası olarak tanımlanmış.
- [ ] from package import item ile import package.item arasındaki son öğe kuralları açıklanmış; namespace paket uygulaması istenmemiş.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](6.4.1-importing-from-a-package/README.md)
<!-- learning-task:end -->
### Sections

- [6.4.1. Importing \* From a Package](6.4.1-importing-from-a-package/README.md)
- [6.4.2. Intra-package References](6.4.2-intra-package-references/README.md)

<!-- learning-milestone:start -->
### Klasör milestone görevi

**Milestone: Paketin dışarı açtığı adları tasarla**

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Paket ağacı, mutlak/göreli import ve `__all__` sözleşmesi.

#### Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

#### Tek görev

1. studytools paketinde core/counts.py ve reports/summary.py oluştur; ara paketlerin `__init__`.py dosyaları olsun. counts bir liste uzunluğu işlevi versin; summary bu işlevi göreli importla kullanıp metin değil sayısal özet döndürsün. reports/`__init__`.py için `__all__` ile yalnız summary modülünü dışarı aç.

2. Üç import biçimiyle kullanıcıya hangi adın bağlandığını ayrı oturumlarda göster.

#### Geçiş ölçütleri

- [ ] Göreli import ..core üzerinden doğru hedefe gidiyor.
- [ ] Kullanıcı paketinden çağrı gerçek sayısal sonuç veriyor.
- [ ] `__all__` yalnız belirlenen modülü dışarı açıyor; disk otomatik tarama varsayımı yok.
- [ ] Paket bağlamıyla doğrudan dosya çalıştırması karıştırılmamış; kaynak örneklerdeki boş stub çıktısı gerçek işlev diye sunulmamış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-milestone:end -->
