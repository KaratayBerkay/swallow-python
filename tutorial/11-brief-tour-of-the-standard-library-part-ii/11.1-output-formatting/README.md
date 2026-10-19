## 11.1. Output formatting

The `reprlib` module provides a version of `repr()` customized for abbreviated displays of large or deeply nested containers:

``` python
>>> import reprlib
>>> reprlib.repr(set('supercalifragilisticexpialidocious'))
"{'a', 'c', 'd', 'e', 'f', 'g', ...}"
```
> Code: [reprlib_example.py](reprlib_example.py)

The `pprint` module offers more sophisticated control over printing both built-in and user defined objects in a way that is readable by the interpreter. When the result is longer than one line, the "pretty printer" adds line breaks and indentation to more clearly reveal data structure:

``` python
>>> import pprint
>>> t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
...     'yellow'], 'blue']]]
...
>>> pprint.pprint(t, width=30)
[[[['black', 'cyan'],
   'white',
   ['green', 'red']],
  [['magenta', 'yellow'],
   'blue']]]
```
> Code: [t.py](t.py)

The `textwrap` module formats paragraphs of text to fit a given screen width:

``` python
>>> import textwrap
>>> doc = """The wrap() method is just like fill() except that it returns
... a list of strings instead of one big string with newlines to separate
... the wrapped lines."""
...
>>> print(textwrap.fill(doc, width=40))
The wrap() method is just like fill()
except that it returns a list of strings
instead of one big string with newlines
to separate the wrapped lines.
```
> Code: [doc.py](doc.py)

The `locale` module accesses a database of culture specific data formats. The grouping attribute of locale's format function provides a direct way of formatting numbers with group separators:

``` python
>>> import locale
>>> locale.setlocale(locale.LC_ALL, 'English_United States.1252')
'English_United States.1252'
>>> conv = locale.localeconv()          # get a mapping of conventions
>>> x = 1234567.8
>>> locale.format_string("%d", x, grouping=True)
'1,234,567'
>>> locale.format_string("%s%.*f", (conv['currency_symbol'],
...                      conv['frac_digits'], x), grouping=True)
'$1,234,567.80'
```
> Code: [conv.py](conv.py)

<!-- learning-task:start -->
### Bölüm görevi

**Görev 11.1: Görünümü verinin kendisinden ayır**

**Odak:** reprlib kısaltma, pprint yerleşimi, textwrap ve locale bağımlı sunum.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:10.12](../../10-brief-tour-of-the-standard-library/10.12-batteries-included/README.md).
- Ön bilgi: [t:7.1.3](../../07-input-and-output/7.1-fancier-output-formatting/7.1.3-manual-string-formatting/README.md).

#### Tek görev

1. data = [list(range(8)), list(range(8, 16))] verisini önce repr, sonra reprlib.repr ve pprint.pprint(width=30) ile göster. Kısaltılan öğelerle yalnız satırı değişen öğeleri karşılaştır.

2. "Python makes small data flows easier to inspect and explain." paragrafını textwrap.fill(width=25) ile biçimle. Gösterimlerden sonra data içindeki iki listenin bütün değerlerini ve paragrafın asıl metnini kontrol et.

3. README içindeki locale örneğini çalıştırmak yerine sayı gruplama, para simgesi ve basamak sayısının hangi yerel ayar verilerinden geldiğini yazılı izle.

#### Geçiş ölçütleri

- [ ] reprlib gösterimi ... ile kısalıyor; pprint çok satırlı ve girintili gösterimde 0..15 değerlerinin tamamını koruyor.
- [ ] İki kaynak liste hâlâ sekizer öğeli; kısaltma veya satır düzeni veriyi değiştirmemiş.
- [ ] Paragraf satırları en fazla 25 karakter; sözcük sırası ve asıl paragraf metni korunmuş.
- [ ] locale gruplama, currency_symbol ve frac_digits rolleri ayrılmış.
- [ ] Örnekteki Windows locale adının her sistemde bulunacağı varsayılmamış; ortam ayarı değiştirme gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../11.2-templating/README.md)
<!-- learning-task:end -->
