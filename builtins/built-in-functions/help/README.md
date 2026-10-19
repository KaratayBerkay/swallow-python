## `help()`

```
help()
help(request)
```

Invoke the built-in help system.  (This function is intended for interactive
use.)  If no argument is given, the interactive help system starts on the
interpreter console.  If the argument is a string, then the string is looked up
as the name of a module, function, class, method, keyword, or documentation
topic, and a help page is printed on the console.  If the argument is any other
kind of object, a help page on the object is generated.

Note that if a slash(/) appears in the parameter list of a function when
invoking help(), it means that the parameters prior to the slash are
positional-only. For more info, see
[the FAQ entry on positional-only parameters](https://docs.python.org/3.15/faq/programming.html#faq-positional-only-arguments).

This function is added to the built-in namespace by the [site](https://docs.python.org/3.15/library/site.html#module-site) module.

> *Changed in version 3.4:* Changes to [pydoc](https://docs.python.org/3.15/library/pydoc.html#module-pydoc) and [inspect](https://docs.python.org/3.15/library/inspect.html#module-inspect) mean that the reported
> signatures for callables are now more comprehensive and consistent.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.33: help sözleşmesini uygula**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

`help(str.split)` ile bu sayfanın imzasını bul. Argümansız yardım sisteminden farkını açıkla; yardım metninden bir doğru çağrı ile bir yanlış argüman çağrısı üret ve dene.

#### Geçiş ölçütleri

- [ ] İmza ve parametre açıklaması bulunmuştur; yardım metninin tamamı ezber çıktısı olarak istenmemiştir.
- [ ] Geçerli çağrı çalışır, yanlış argüman hatası imzayla ilişkilendirilmiştir.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../hex/README.md)
<!-- learning-task:end -->
