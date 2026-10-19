## 5.7. Package Relative Imports

Relative imports use leading dots. A single leading dot indicates a relative import, starting with the current package. Two or more leading dots indicate a relative import to the parent(s) of the current package, one level per dot after the first. For example, given the following package layout:

``` python
package/
    __init__.py
    subpackage1/
        __init__.py
        moduleX.py
        moduleY.py
    subpackage2/
        __init__.py
        moduleZ.py
    moduleA.py
```
> Code: [example_01.py](example_01.py)

In either `subpackage1/moduleX.py` or `subpackage1/__init__.py`, the following are valid relative imports:

``` python
from .moduleY import spam
from .moduleY import spam as ham
from . import moduleY
from ..subpackage1 import moduleY
from ..subpackage2.moduleZ import eggs
from ..moduleA import foo
```
> Code: [spam.py](spam.py)

Absolute imports may use either the `import <>` or `from <> import <>` syntax, but relative imports may only use the second form; the reason for this is that:

``` python
import XXX.YYY.ZZZ
```
> Code: [xxx.py](xxx.py)

should expose `XXX.YYY.ZZZ` as a usable expression, but .moduleY is not a valid expression.

<!-- learning-task:start -->
### Bölüm görevi

**Görev 5.7: Göreli importu mutlak ada çöz**

**Odak:** Nokta sayısı, package bağlamı, alias ve göreli import için from gerekliliği.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.6](../5.6-replacing-the-standard-import-system/README.md).
- Ön bilgi: [t:6.4.2](../../../tutorial/06-modules/6.4-packages/6.4.2-intra-package-references/README.md).

#### Tek görev

1. README içindeki package.subpackage1.moduleX konumundan .moduleY, ..subpackage2.moduleZ ve ..moduleA yollarını mutlak importlara çevir. spam as ham aktarımında kaynak nesne ile yerel adı ayır.

2. Aynı göreli ifadenin subpackage1/`__init__`.py içinde neden aynı hedefi bulduğunu açıkla. import .moduleY biçiminin neden geçerli olmadığını yaz.

#### Geçiş ölçütleri

- [ ] Hedefler package.subpackage1.moduleY, package.subpackage2.moduleZ, package.moduleA.
- [ ] Bir nokta mevcut paket, her ek nokta bir üst paket.
- [ ] Alias yerel adı değiştiriyor, kaynağı değiştirmiyor.
- [ ] Göreli import from biçiminde; başlangıç noktası dosya sisteminin çalışma dizini değil paket bağlamı.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../5.8-special-considerations-for-main/README.md)
<!-- learning-task:end -->
