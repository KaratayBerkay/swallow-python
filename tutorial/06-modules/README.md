# 6. Modules

If you quit from the Python interpreter and enter it again, the definitions you have made (functions and variables) are lost. Therefore, if you want to write a somewhat longer program, you are better off using a text editor to prepare the input for the interpreter and running it with that file as input instead. This is known as creating a *script*. As your program gets longer, you may want to split it into several files for easier maintenance. You may also want to use a handy function that you've written in several programs without copying its definition into each program.

To support this, Python has a way to put definitions in a file and use them in a script or in an interactive instance of the interpreter. Such a file is called a *module*; definitions from a module can be *imported* into other modules or into the *main* module (the collection of variables that you have access to in a script executed at the top level and in calculator mode).

A module is a file containing Python definitions and statements. The file name is the module name with the suffix `.py` appended. Within a module, the module's name (as a string) is available as the value of the global variable `__name__`. For instance, use your favorite text editor to create a file called `fibo.py` in the current directory with the following contents:

``` python
# Fibonacci numbers module

def fib(n):
    """Write Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    """Return Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```
> Code: [fibo.py](fibo.py)

Now enter the Python interpreter and import this module with the following command:

``` python
>>> import fibo
```
> Code: [import_fibo.py](import_fibo.py)

This does not add the names of the functions defined in `fibo` directly to the current namespace (see Python Scopes and Namespaces for more details); it only adds the module name `fibo` there. Using the module name you can access the functions:

``` python
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'
```
> Code: [example_01.py](example_01.py)

If you intend to use a function often you can assign it to a local name:

``` python
>>> fib = fibo.fib
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```
> Code: [fib_2.py](fib_2.py)


<!-- learning-task:start -->
## Bölüm görevi

**Görev 6: İşlevi başka dosyadan kullan**

**Odak:** Modül dosyası, import ile ad bağlama, modül niteliği ve `__name__`.

### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:4.8](../04-more-control-flow-tools/4.8-defining-functions/README.md).

### Tek görev

1. Ayrı bir çalışma klasöründe counts.py içine count_items(items) işlevini yaz; len(items) döndürsün.

2. Aynı klasörden başlattığın REPL içinde import counts ile işlevi çağır, `counts.__name__` değerini göster ve f = counts.count_items ile ikinci ad üzerinden çağır.

3. Python oturumu yeniden başlayınca nelerin kaybolduğunu, dosyanın neden kaldığını açıkla.

### Geçiş ölçütleri

- [ ] counts.count_items([3, 5]) ve f([3, 5]) sonuçları 2.
- [ ] import counts, count_items adını tek başına yerel alana eklemiyor.
- [ ] `counts.__name__` counts metni; dosya adı .py son ekiyle ilişkili.
- [ ] Yeni oturumda tekrar import gerektiği açıklanmış; sonraki bölümdeki from/as teknikleri gerekmiyor.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md) · [Sıra](../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](6.1-more-on-modules/README.md)
<!-- learning-task:end -->
## Sections

- [6.1. More on Modules](6.1-more-on-modules/README.md)
- [6.2. Standard Modules](6.2-standard-modules/README.md)
- [6.3. The `dir()` Function](6.3-the-dir-function/README.md)
- [6.4. Packages](6.4-packages/README.md)

<!-- learning-milestone:start -->
## Klasör milestone görevi

**Milestone: Tekrar kullanılabilir hesap paketini teslim et**

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Modül/paket sınırları, kontrollü başlangıç, public adlar ve keşif.

### Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

### Tek görev

1. studycalc paketinde operations.py içinde total(values), driver.py içinde yalnız ana girişte örnek veriyle sonuç yazdıran kod olsun. `__init__`.py üzerinden total adını açıkça sun.

2. Ayrı REPLde import studycalc, from studycalc import total ve bir alias çağrısı yap; dir ile erişilebilir adları kontrol et. driver için paket bağlamında -m başlatma planı yaz.

3. Bir ad gölgeleme hatasını oluşturmak yerine hangi dosya adından kaçınacağını açıklayan teşhis notu ekle.

### Geçiş ölçütleri

- [ ] Paket işlevi ve doğrudan alınan işlev aynı veride aynı sonucu veriyor.
- [ ] Normal importta driver raporu çalışmıyor.
- [ ] Public adlar bilinçli dışarı açılmış; tüm adları * ile yayma varsayımı yok.
- [ ] Arama yolu ve yeniden import/reload farkı açıklanmış.
- [ ] Başka klasörden çalıştırma gereksinimi paket dosyalarının yanında olmakla karıştırılmamış; daha önce işlenmeyen paket kurulumu gerekmiyor.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md) · [Sıra](../../TASKS.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../07-input-and-output/7.1-fancier-output-formatting/README.md)
<!-- learning-milestone:end -->
