### 4.9.8. Function Annotations

Function annotations are completely optional metadata information about the types used by user-defined functions (see [**PEP 3107**](https://peps.python.org/pep-3107/) and [**PEP 484**](https://peps.python.org/pep-0484/) for more information).

Annotations are stored in the `__annotations__` attribute of the function as a dictionary and have no effect on any other part of the function. Parameter annotations are defined by a colon after the parameter name, followed by an expression evaluating to the value of the annotation. Return annotations are defined by a literal `->`, followed by an expression, between the parameter list and the colon denoting the end of the `def` statement. The following example has a required argument, an optional argument, and the return value annotated:

``` python
>>> def f(ham: str, eggs: str = 'eggs') -> str:
...     print("Annotations:", f.__annotations__)
...     print("Arguments:", ham, eggs)
...     return ham + ' and ' + eggs
...
>>> f('spam')
Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
Arguments: spam eggs
'spam and eggs'
```
> Code: [f.py](f.py)

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 4.9.8: Tür açıklamasını çalışma zamanı denetiminden ayır**

**Odak:** Parametre ve dönüş annotation sözdizimi, varsayılan ve `__annotations__` metaverisi.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:4.9.7](../4.9.7-documentation-strings/README.md).

##### Tek görev

1. left: str ve right: str = "!" parametreleriyle iki değeri + kullanarak döndüren, dönüşü str olarak açıklanmış combine yaz. `__annotations__` içeriğini incele; combine("Hi") ve combine(2, 3) çağrılarını dene.

2. Sonuç ile açıklanan tür uyuşmadığında yorumlayıcının ne yaptığını anlat.

##### Geçiş ölçütleri

- [ ] İlk sonuç Hi!, ikinci sonuç 5; annotation kendiliğinden tür hatası üretmiyor.
- [ ] Parametreler : ile, dönüş -> ile açıklanmış; varsayılan doğru yerde.
- [ ] `__annotations__` içinde left, right, return adları mevcut; anahtar sırası veya repr adresi ezberlenmemiş.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
