## 6.1. More on Modules

> **Note**
>
> The `fibo` module used in the examples below is defined in [fibo.py](fibo.py).

A module can contain executable statements as well as function definitions. These statements are intended to initialize the module. They are executed only the *first* time the module name is encountered in an import statement. (In fact function definitions are also 'statements' that are 'executed'; the execution of a module-level function definition adds the function name to the module's global namespace.) (They are also run if the file is executed as a script.)

Each module has its own private namespace, which is used as the global namespace by all functions defined in the module. Thus, the author of a module can use global variables in the module without worrying about accidental clashes with a user's global variables. On the other hand, if you know what you are doing you can touch a module's global variables with the same notation used to refer to its functions, `modname.itemname`.

Modules can import other modules. It is customary but not required to place all `import` statements at the beginning of a module (or script, for that matter). The imported module names, if placed at the top level of a module (outside any functions or classes), are added to the module's global namespace.

There is a variant of the `import` statement that imports names from a module directly into the importing module's namespace. For example:

``` python
>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```
> Code: [fib.py](fib.py)

This does not introduce the module name from which the imports are taken in the local namespace (so in the example, `fibo` is not defined).

There is even a variant to import all names that a module defines:

``` python
>>> from fibo import *
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```
> Code: [example_01.py](example_01.py)

This imports all names except those beginning with an underscore (`_`). In most cases Python programmers do not use this facility since it introduces an unknown set of names into the interpreter, possibly hiding some things you have already defined.

Note that in general the practice of importing `*` from a module or package is frowned upon, since it often causes poorly readable code. However, it is okay to use it to save typing in interactive sessions.

If the module name is followed by `as`, then the name following `as` is bound directly to the imported module.

``` python
>>> import fibo as fib
>>> fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```
> Code: [import_fibo_as_fib.py](import_fibo_as_fib.py)

This is effectively importing the module in the same way that `import fibo` will do, with the only difference of it being available as `fib`.

It can also be used when utilising `from` with similar effects:

``` python
>>> from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```
> Code: [fib_2.py](fib_2.py)

> **Note**
>
> For efficiency reasons, each module is only imported once per interpreter session. Therefore, if you change your modules, you must restart the interpreter -- or, if it's just one module you want to test interactively, use `importlib.reload()`, e.g. `import importlib; importlib.reload(modulename)`.


<!-- learning-task:start -->
### Bölüm görevi

**Görev 6.1: İçe aktarmanın adlara ve başlangıca etkisini izle**

**Odak:** İlk importta yürütme, modül kapsamı, from/as/* ve reload.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:6](../README.md).

#### Tek görev

1. counts.py kopyasına üst düzeyde print("loaded"), public_value = 1 ve _internal = 2 ekle.

2. Yeni oturumda iki kez import et.

3. Ayrı yeni oturumlarda from counts import count_items, import counts as c ve from counts import * deneyerek hangi adların kullanılabildiğini not et.

4. Dosyadaki public_value değerini değiştirip yeniden import ile importlib.reload farkını göster.

#### Geçiş ölçütleri

- [ ] Aynı oturumda iki import başlangıç mesajını yalnız bir kez basıyor; reload yeniden yürütüyor.
- [ ] from biçimi işlevi, as biçimi c adını bağlıyor.
- [ ] Yıldızlı aktarım _internal adını getirmiyor; isim gizleme riski somut bir adla açıklanmış.
- [ ] Modülün kendi global adları çağıranın aynı adlı değişkenlerinden ayrılmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](6.1.1-executing-modules-as-scripts/README.md)
<!-- learning-task:end -->
### Sections

- [6.1.1. Executing modules as scripts](6.1.1-executing-modules-as-scripts/README.md)
- [6.1.2. The Module Search Path](6.1.2-the-module-search-path/README.md)
- [6.1.3. "Compiled" Python files](6.1.3-compiled-python-files/README.md)

<!-- learning-milestone:start -->
### Klasör milestone görevi

**Milestone: Hem içe aktarılan hem çalıştırılan modülü izle**

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Modül başlangıcı, main koruması, ad bağlama, yol ve bytecode cache ilişkisi.

#### Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

#### Tek görev

1. numbers_tool.py içinde listeden toplam döndüren işlev ve yalnız ana çalıştırmada iki sabit sayı için sonuç yazdıran koruma kur.

2. Yeni oturumdan iki import, işlev çağrısı ve doğrudan dosya çalıştırmasını karşılaştır.

3. Aynı adlı başka dosya betik klasöründe olsaydı arama seçimini, kaynak değişseydi yeni süreçte .pyc kontrolünü not et.

#### Geçiş ölçütleri

- [ ] Importta ana rapor basılmıyor, doğrudan betikte basılıyor.
- [ ] İki import aynı modül nesnesine gidiyor; işlev açıkça çağrılabiliyor.
- [ ] İsim bağlama, modül arama ve bytecode cache üç ayrı olay olarak açıklanmış.
- [ ] .pyc çalışma algoritmasını hızlandırma garantisi sayılmamış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../6.2-standard-modules/README.md)
<!-- learning-milestone:end -->
