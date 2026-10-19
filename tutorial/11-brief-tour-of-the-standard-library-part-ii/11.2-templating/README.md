## 11.2. Templating

The `string` module includes a versatile `Template` class with a simplified syntax suitable for editing by end-users. This allows users to customize their applications without having to alter the application.

The format uses placeholder names formed by `$` with valid Python identifiers (alphanumeric characters and underscores). Surrounding the placeholder with braces allows it to be followed by more alphanumeric letters with no intervening spaces. Writing `$$` creates a single escaped `$`:

``` python
>>> from string import Template
>>> t = Template('${village}folk send $$10 to $cause.')
>>> t.substitute(village='Nottingham', cause='the ditch fund')
'Nottinghamfolk send $10 to the ditch fund.'
```
> Code: [t.py](t.py)

The `substitute()` method raises a `KeyError` when a placeholder is not supplied in a dictionary or a keyword argument. For mail-merge style applications, user supplied data may be incomplete and the `safe_substitute()` method may be more appropriate --- it will leave placeholders unchanged if data is missing:

``` python
>>> t = Template('Return the $item to $owner.')
>>> d = dict(item='unladen swallow')
>>> t.substitute(d)
Traceback (most recent call last):
  ...
KeyError: 'owner'
>>> t.safe_substitute(d)
'Return the unladen swallow to $owner.'
```
> Code: [t_2.py](t_2.py)

Template subclasses can specify a custom delimiter. For example, a batch renaming utility for a photo browser may elect to use percent signs for placeholders such as the current date, image sequence number, or file format:

``` python
>>> import time, os.path
>>> photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
>>> class BatchRename(Template):
...     delimiter = '%'
...
>>> fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f

>>> t = BatchRename(fmt)
>>> date = time.strftime('%d%b%y')
>>> for i, filename in enumerate(photofiles):
...     base, ext = os.path.splitext(filename)
...     newname = t.substitute(d=date, n=i, f=ext)
...     print('{0} --> {1}'.format(filename, newname))

img_1074.jpg --> Ashley_0.jpg
img_1076.jpg --> Ashley_1.jpg
img_1077.jpg --> Ashley_2.jpg
```
> Code: [batch_rename.py](batch_rename.py)

Another application for templating is separating program logic from the details of multiple output formats. This makes it possible to substitute custom templates for XML files, plain text reports, and HTML web reports.

<!-- learning-task:start -->
### Bölüm görevi

**Görev 11.2: Eksik alanı tamamlamadan şablonu koru**

**Odak:** Template $/{}/$$, substitute/safe_substitute ve özel delimiter.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:11.1](../11.1-output-formatting/README.md).
- Ön bilgi: [t:9.5](../../09-classes/9.5-inheritance/README.md).

#### Tek görev

1. Template("${name}box costs $$5 for $owner.") oluştur. name="Study", owner="Ada" ile doldur; owner eksikken substitute ile safe_substitute sonuçlarını ayrı dene.

2. Sonra bölümdeki BatchRename iskeletindeki delimiter = "%" yaklaşımını kullanarak "%n%f" şablonunu n=2, f=".jpg" ile doldur.

3. Yalnız yeni dosya adını üret, dosya yeniden adlandırma işlemi gerekmiyor.

#### Geçiş ölçütleri

- [ ] Tam sonuç Studybox costs $5 for Ada.
- [ ] Eksik owner substitute için KeyError, safe_substitute için $owner olarak kalıyor.
- [ ] ${name} bitişi, isimden sonra box ekine izin veriyor; $$ tek $ üretiyor.
- [ ] Özel ayraç sonucu 2.jpg; şablonun veriyle doldurulması program mantığından ayrılmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../11.3-working-with-binary-data-record-layouts/README.md)
<!-- learning-task:end -->
