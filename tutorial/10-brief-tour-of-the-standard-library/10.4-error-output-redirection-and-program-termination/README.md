## 10.4. Error output redirection and program termination

The `sys` module also has attributes for *stdin*, *stdout*, and *stderr*. The latter is useful for emitting warnings and error messages to make them visible even when *stdout* has been redirected:

``` python
>>> sys.stderr.write('Warning, log file not found starting a new one\n')
Warning, log file not found starting a new one
```
> Code: [example_01.py](example_01.py)

The most direct way to terminate a script is to use `sys.exit()`.

<!-- learning-task:start -->
### Bölüm görevi

**Görev 10.4: Hata mesajıyla normal çıktıyı ayır**

**Odak:** stdout/stderr ayrımı ve sys.exit ile yürütmeyi bitirme.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:10.3](../10.3-command-line-arguments/README.md).
- Ön bilgi: [t:8.4](../../08-errors-and-exceptions/8.4-raising-exceptions/README.md).

#### Tek görev

1. Küçük betikte print ile "starting" yaz; sys.stderr.write ile "missing data\n" yaz; sys.exit() çağır; arkasına print("unreachable") koy.

2. Terminalde dene ve her mesajın akışını not et.

3. Normal çıktı bir dosyaya yönlendirilmiş olsaydı hangi mesajın dosyaya, hangisinin stderr akışına gideceğini açıkla. Shell yönlendirme komutu yazman gerekmiyor.

#### Geçiş ölçütleri

- [ ] starting stdout, missing data stderr üzerinden; unreachable basılmıyor.
- [ ] sys.exit sonrasına normal yürütmeyle geçilmiyor.
- [ ] Hata mesajının sıradan printten ayrı akışa yazılmasının amacı açıklanmış.
- [ ] stdout yönlendirilse stderr görünürlüğünün ayrı kaldığı kavramsal olarak gösterilmiş; yeni shell yönlendirme sözdizimi gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../10.5-string-pattern-matching/README.md)
<!-- learning-task:end -->
