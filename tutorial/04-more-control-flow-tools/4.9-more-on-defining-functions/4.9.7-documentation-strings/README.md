### 4.9.7. Documentation Strings

Here are some conventions about the content and formatting of documentation strings.

The first line should always be a short, concise summary of the object's purpose. For brevity, it should not explicitly state the object's name or type, since these are available by other means (except if the name happens to be a verb describing a function's operation). This line should begin with a capital letter and end with a period.

If there are more lines in the documentation string, the second line should be blank, visually separating the summary from the rest of the description. The following lines should be one or more paragraphs describing the object's calling conventions, its side effects, etc.

The Python parser strips indentation from multi-line string literals when they serve as module, class, or function docstrings.

Here is an example of a multi-line docstring:

``` python
>>> def my_function():
...     """Do nothing, but document it.
...
...     No, really, it doesn't do anything:
...
...         >>> my_function()
...         >>>
...     """
...     pass
...
>>> print(my_function.__doc__)
Do nothing, but document it.

No, really, it doesn't do anything:

    >>> my_function()
    >>>
```
> Code: [my_function.py](my_function.py)

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 4.9.7: Davranışı anlatan docstring yaz**

**Odak:** Özet satırı, boş ayırıcı satır, çağrı koşulları ve `__doc__`.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:4.8](../../4.8-defining-functions/README.md).

##### Tek görev

1. İki metni bir ayraçla birleştirip döndüren label(left, right, sep=":") fonksiyonuna çok satırlı İngilizce docstring yaz.

2. İlk satır kısa özet, devamı varsayılan ayraç ve dönüş davranışı olsun. print(`label.__doc__`) ile açıklamayı, label("a", "b") ile davranışı kontrol et.

3. Yorum satırı ile docstring yerini karşılaştır.

##### Geçiş ölçütleri

- [ ] İlk satır büyük harfle başlayan ve noktayla biten kısa davranış özeti.
- [ ] İkinci satır boş; devamı parametre ve dönüşü anlatıyor.
- [ ] Docstring fonksiyonun ilk ifadesi ve `__doc__` ile erişilebilir.
- [ ] Açıklama gerçek a:b davranışıyla tutarlı; # yorumu docstring yerine sayılmamış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../4.9.8-function-annotations/README.md)
<!-- learning-task:end -->
