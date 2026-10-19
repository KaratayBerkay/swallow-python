### 2.2.1. Source Code Encoding

By default, Python source files are treated as encoded in UTF-8. In that encoding, characters of most languages in the world can be used simultaneously in string literals, identifiers and comments --- although the standard library only uses ASCII characters for identifiers, a convention that any portable code should follow. To display all these characters properly, your editor must recognize that the file is UTF-8, and it must use a font that supports all the characters in the file.

To declare an encoding other than the default one, a special comment line should be added as the *first* line of the file. The syntax is as follows:

``` python
# -*- coding: encoding -*-
```
> Code: [example_01.py](example_01.py)

where *encoding* is one of the valid `codecs` supported by Python.

For example, to declare that Windows-1252 encoding is to be used, the first line of your source code file should be:

``` python
# -*- coding: cp1252 -*-
```
> Code: [example_02.py](example_02.py)

One exception to the *first line* rule is when the source code starts with a UNIX "shebang" line. In this case, the encoding declaration should be added as the second line of the file. For example:

``` python
#!/usr/bin/env python3
# -*- coding: cp1252 -*-
```
> Code: [example_03.py](example_03.py)

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 2.2.1: Kaynak dosyasının kodlamasını seç**

**Odak:** Varsayılan UTF-8, kodlama bildiriminin konumu ve editör ile dosya kodlamasının uyumu.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:2.1](../../2.1-invoking-the-interpreter/README.md).

##### Tek görev

1. Üç küçük kaynak dosyası taslağı hazırla: UTF-8 yorum içeren varsayılan dosya; cp1252 olarak kaydedileceği belirtilen dosya; ilk satırı bölümdeki shebang olan cp1252 dosyası.

2. İçerik olarak yalnızca yorum kullanabilirsin.

3. Her taslak için gerçek kayıt kodlamasını, bildirimin gerekip gerekmediğini ve varsa satır numarasını yaz.

4. Gerçek cp1252 dosyası üretmek yerine taslak yeterli.

##### Geçiş ölçütleri

- [ ] UTF-8 dosya için ayrıca kodlama bildirimi gerekmiyor.
- [ ] cp1252 bildirimi normal dosyada ilk, shebang bulunan dosyada ikinci satırda.
- [ ] Bildirimdeki encoding sözcüğü yer tutucu olarak bırakılmamış.
- [ ] Bildirim eklemenin dosyanın gerçek baytlarını dönüştürmediği; editör kodlaması ve karakteri gösterebilen yazı tipinin ayrı olduğu açıklanmış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
