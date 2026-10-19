## 4.6. `pass` Statements

The `pass` statement does nothing. It can be used when a statement is required syntactically but the program requires no action. For example:

``` python
>>> while True:
...     pass  # Busy-wait for keyboard interrupt (Ctrl+C)
...
```
> Code: [example_01.py](example_01.py)

This is commonly used for creating minimal classes:

``` python
>>> class MyEmptyClass:
...     pass
...
```
> Code: [my_empty_class.py](my_empty_class.py)

Another place `pass` can be used is as a place-holder for a function or conditional body when you are working on new code, allowing you to keep thinking at a more abstract level. The `pass` is silently ignored:

``` python
>>> def initlog(*args):
...     pass   # Remember to implement this!
...
```
> Code: [initlog.py](initlog.py)

For this last case, many people use the ellipsis literal `...` instead of `pass`. This use has no special meaning to Python, and is not part of the language definition (you could use any constant expression here), but `...` is used conventionally as a placeholder body as well. See The Ellipsis Object.

<!-- learning-task:start -->
### Bölüm görevi

**Görev 4.6: Boş dalın akışını koru**

**Odak:** pass hiçbir işlem yapmaz; sözdiziminin gövde beklediği yerde yer tutar.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:4.5](../4.5-else-clauses-on-loops/README.md).

#### Tek görev

1. for ile [0, 1, 2] üzerinde dolaş. 1 olduğunda if gövdesine pass koy; her turun sonunda sayıyı yazdır.

2. Aynı deneyi pass yerine continue ve break koyarak ayrı ayrı yap.

3. Bölümdeki boş sınıf ve fonksiyon örneklerinde pass satırının hangi ihtiyacı karşıladığını, sınıf/fonksiyon yapısını genişletmeden açıkla.

#### Geçiş ölçütleri

- [ ] pass ile 0, 1, 2; continue ile 0, 2; break ile yalnızca 0 basılıyor.
- [ ] pass satırının çalışmayı durdurmadığı açıklanmış.
- [ ] Tamamen boş gövdeyle yorum satırından oluşan gövdenin neden yeterli olmadığı açıklanmış.
- [ ] ... kullanımının ayrı bir akış komutu olmadığı belirtilmiş.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../4.7-match-statements/README.md)
<!-- learning-task:end -->
