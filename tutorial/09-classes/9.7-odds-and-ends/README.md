## 9.7. Odds and Ends

Sometimes it is useful to have a data type similar to the Pascal "record" or C "struct", bundling together a few named data items. The idiomatic approach is to use `dataclasses` for this purpose:

``` python
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    dept: str
    salary: int
```
> Code: [employee.py](employee.py)

``` python
>>> john = Employee('john', 'computer lab', 1000)
>>> john.dept
'computer lab'
>>> john.salary
1000
```
> Code: [john.py](john.py)

A piece of Python code that expects a particular abstract data type can often be passed a class that emulates the methods of that data type instead. For instance, if you have a function that formats some data from a file object, you can define a class with methods `read()` and `readline()` that get the data from a string buffer instead, and pass it as an argument.

Instance method objects have attributes, too: `m.__self__` is the instance object with the method `m()`, and `m.__func__` is the function object corresponding to the method.

<!-- learning-task:start -->
### Bölüm görevi

**Görev 9.7: Kayıt nesnesiyle metot bağını göster**

**Odak:** Veri kaydı için verilen dataclass iskeleti, beklenen metotları sağlayabilme ve metot nitelikleri.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:9.6](../9.6-private-variables/README.md).
- Ön bilgi: [t:4.9.8](../../04-more-control-flow-tools/4.9-more-on-defining-functions/4.9.8-function-annotations/README.md).

#### Tek görev

1. README içindeki Employee dataclass tanımını hazır iskelet olarak kullan; iki çalışan oluşturup birinin dept değerini değiştir ve diğerinin korunduğunu göster.

2. Sonra kendi Notebook örneğindeki m = notebook.add_note için `m.__self__` ve `m.__func__` değerlerini, nesne ve sınıf işleviyle karşılaştır.

3. Son notunda read/readline bekleyen bir tüketiciye aynı metotları sağlayan başka nesnenin neden verilebildiğini açıkla.

4. Decorator mekanizmasını uygulaman gerekmiyor.

#### Geçiş ölçütleri

- [ ] Çalışanların verileri ayrı; iskeletteki alanlar doğru argümanlarla doldurulmuş.
- [ ] `m.__self__` ilgili notebook, `m.__func__` Notebook.add_note işlevi.
- [ ] Veri kaydıyla davranış beklentisini karşılama ayrı ihtiyaçlar olarak açıklanmış.
- [ ] dataclass iç çalışma mekanizması veya daha önce öğretilmeyen bir seçenek kullanılmamış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../9.8-iterators/README.md)
<!-- learning-task:end -->
