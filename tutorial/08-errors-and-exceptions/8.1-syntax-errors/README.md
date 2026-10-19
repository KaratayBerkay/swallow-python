## 8.1. Syntax Errors

Syntax errors, also known as parsing errors, are perhaps the most common kind of complaint you get while you are still learning Python:

``` python
>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
               ^^^^^
SyntaxError: invalid syntax
```
> Code: [example_01.py](example_01.py)

The parser repeats the offending line and displays little arrows pointing at the place where the error was detected. Note that this is not always the place that needs to be fixed. In the example, the error is detected at the function `print()`, since a colon (`':'`) is missing just before it.

The file name (`<stdin>` in our example) and line number are printed so you know where to look in case the input came from a file.

<!-- learning-task:start -->
### Bölüm görevi

**Görev 8.1: Okun işaret ettiği yerden asıl hataya git**

**Odak:** SyntaxError içindeki dosya/satır/ok bilgisi ile eksik sözdizimini bulma.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:7.2.2](../../07-input-and-output/7.2-reading-and-writing-files/7.2.2-saving-structured-data-with-json/README.md).

#### Tek görev

1. README içindeki while True print örneğinin kopyasında True yerine False kullan.

2. Önce hatayı çalıştırarak gör; dosya adı, satır ve okun gösterdiği yeri kaydet.

3. Yalnız gereken sözdizimini düzeltip yeniden çalıştır.

4. Koşul False olduğundan son sürümün neden çıktı üretmediğini açıkla.

#### Geçiş ölçütleri

- [ ] Ok print yakınında olsa da düzeltme öncesine : eklenmiş.
- [ ] İlk çalıştırma SyntaxError, ikinci çalıştırma sonlanıyor ve hello basmıyor.
- [ ] Hatanın bulunduğu yer ile düzeltilecek yerin her zaman aynı olmadığı açıklanmış; sonsuz döngü başlatılmamış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../8.2-exceptions/README.md)
<!-- learning-task:end -->
