### 6.1.1. Executing modules as scripts

When you run a Python module with

``` python
python fibo.py <arguments>
```
> Code: [example_01.py](example_01.py)

the code in the module will be executed, just as if you imported it, but with the `__name__` set to `"__main__"`. That means that by adding this code at the end of your module:

``` python
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```
> Code: [example_02.py](example_02.py)

you can make the file usable as a script as well as an importable module, because the code that parses the command line only runs if the module is executed as the "main" file:

``` console
$ python fibo.py 50
0 1 1 2 3 5 8 13 21 34
```

If the module is imported, the code is not run:

``` python
>>> import fibo
>>>
```
> Code: [fibo.py](fibo.py)

This is often used either to provide a convenient user interface to a module, or for testing purposes (running the module as a script executes a test suite).

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 6.1.1: Dosyanın iki giriş yolunu ayır**

**Odak:** `__name__` == "`__main__`" koruması ve komut satırı argümanları.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:6.1](../README.md).
- Ön bilgi: [t:2.1.1](../../../02-using-the-python-interpreter/2.1-invoking-the-interpreter/2.1.1-argument-passing/README.md).

##### Tek görev

1. counts.py dosyasında count_items işlevini koru; dosyanın sonuna bölümdeki `__main__` korumasıyla sys.argv[1:] öğe sayısını yazdıran kod ekle. python counts.py a b çalıştırması ile yeni REPL içinde import counts ve counts.count_items(["a", "b"]) çağrılarını karşılaştır.

##### Geçiş ölçütleri

- [ ] Dosya olarak çalışınca 2 basıyor; import sırasında komut satırı işlemi çalışmıyor.
- [ ] Açık işlev çağrısı 2 döndürüyor.
- [ ] İki giriş yolunda `__name__` değerleri ve korumanın neden gerekli olduğu açıklanmış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../6.1.2-the-module-search-path/README.md)
<!-- learning-task:end -->
