## 7.1. Fancier output formatting

So far we've encountered two ways of writing values: *expression statements* and the `print()` function. (A third way is using the `write()` method of file objects; the standard output file can be referenced as `sys.stdout`. See the Library Reference for more information on this.)

Often you'll want more control over the formatting of your output than simply printing space-separated values. There are several ways to format output.

- To use formatted string literals, begin a string with `f` or `F` before the opening quotation mark or triple quotation mark. Inside this string, you can write a Python expression between `{` and `}` characters that can refer to variables or literal values.

  ``` python
  >>> year = 2016
  >>> event = 'Referendum'
  >>> f'Results of the {year} {event}'
  'Results of the 2016 Referendum'
  ```

- The `str.format()` method of strings requires more manual effort. You'll still use `{` and `}` to mark where a variable will be substituted and can provide detailed formatting directives, but you'll also need to provide the information to be formatted. In the following code block there are two examples of how to format variables:

  ``` python
  >>> yes_votes = 42_572_654
  >>> total_votes = 85_705_149
  >>> percentage = yes_votes / total_votes
  >>> '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
  ' 42572654 YES votes  49.67%'
  ```

  Notice how the `yes_votes` are padded with spaces and a negative sign only for negative numbers. The example also prints `percentage` multiplied by 100, with 2 decimal places and followed by a percent sign (see Format specification mini-language for details).

- Finally, you can do all the string handling yourself by using string slicing and concatenation operations to create any layout you can imagine. The string type has some methods that perform useful operations for padding strings to a given column width.

When you don't need fancy output but just want a quick display of some variables for debugging purposes, you can convert any value to a string with the `repr()` or `str()` functions.

The `str()` function is meant to return representations of values which are fairly human-readable, while `repr()` is meant to generate representations which can be read by the interpreter (or will force a `SyntaxError` if there is no equivalent syntax). For objects which don't have a particular representation for human consumption, `str()` will return the same value as `repr()`. Many values, such as numbers or structures like lists and dictionaries, have the same representation using either function. Strings, in particular, have two distinct representations.

Some examples:

``` python
>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'
>>> repr(s)
"'Hello, world.'"
>>> str(1/7)
'0.14285714285714285'
>>> x = 10 * 3.25
>>> y = 200 * 200
>>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
>>> print(s)
The value of x is 32.5, and y is 40000...
>>> # The repr() of a string adds string quotes and backslashes:
>>> hello = 'hello, world\n'
>>> hellos = repr(hello)
>>> print(hellos)
'hello, world\n'
>>> # The argument to repr() may be any Python object:
>>> repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"
```
> Code: [s.py](s.py)

The `string` module contains support for a simple templating approach based upon regular expressions, via `string.Template`. This offers yet another way to substitute values into strings, using placeholders like `$x` and replacing them with values from a dictionary. This syntax is easy to use, although it offers much less control for formatting.


<!-- learning-task:start -->
### Bölüm görevi

**Görev 7.1: Aynı verinin üç gösterimini ayır**

**Odak:** print, str/repr, temel f-string ve str.format ile sunum.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:5.5](../../05-data-structures/5.5-dictionaries/README.md).
- Ön bilgi: [t:6](../../06-modules/README.md).

#### Tek görev

1. name = "Ada", count = 3, message = "Ready\nGo" verileriyle aynı "Ada has 3 items" mesajını f-string ve format kullanarak kur. message için print(message), print(str(message)), print(repr(message)) sonuçlarını karşılaştır. 3/8 oranını README içindeki yüzde biçimiyle iki ondalıkla göster; sayısal değer ile biçimlenmiş metni ayrı tut.

#### Geçiş ölçütleri

- [ ] İki mesaj aynı metni üretiyor.
- [ ] İlk iki gösterim iki satır, repr gösterimi tırnak ve kaçış içeren temsil.
- [ ] Yüzde görünümü 37.50%; kaynak oran 0.375 olarak korunmuş.
- [ ] Gösterim biçimlemenin temel veriyi değiştirmediği açıklanmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](7.1.1-formatted-string-literals/README.md)
<!-- learning-task:end -->
### Sections

- [7.1.1. Formatted string literals](7.1.1-formatted-string-literals/README.md)
- [7.1.2. The string format() method](7.1.2-the-string-format-method/README.md)
- [7.1.3. Manual string formatting](7.1.3-manual-string-formatting/README.md)
- [7.1.4. Old string formatting](7.1.4-old-string-formatting/README.md)

<!-- learning-milestone:start -->
### Klasör milestone görevi

**Milestone: Bir raporun verisini ve görünümünü ayrı doğrula**

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** f-string/format/eski % ve manuel hizalamanın aynı veride uygulanması.

#### Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

#### Tek görev

1. name="Ada", count=7, total=12.5 için küçük bir rapor üret.

2. Ana satırda f-string ile genişlik ve iki ondalık kullan; aynı sayısal görünümü format ve eski % yöntemiyle doğrula.

3. Ayrı bir kod alanını zfill ile doldur ve uzun adın kesilmeden alanı aşmasını göster. repr görünümünden boşluk/satır sonlarını kontrol et.

#### Geçiş ölçütleri

- [ ] Üç sayısal görünüm 12.50; alan genişlikleri doğru.
- [ ] Doldurma ve kesme farklı işlem; asıl veriler korunmuş.
- [ ] repr teşhis görünümü normal kullanıcı mesajı sanılmamış.
- [ ] Şablonda hangi alanın hangi değerden geldiği açıklanmış; bir tek çıktıyı sabit metin yazmak yeterli değil.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../7.2-reading-and-writing-files/README.md)
<!-- learning-milestone:end -->
