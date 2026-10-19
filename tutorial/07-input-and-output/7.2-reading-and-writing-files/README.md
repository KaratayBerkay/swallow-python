## 7.2. Reading and writing files

`open()` returns a file object, and is most commonly used with two positional arguments: `open(filename, mode)`

``` python
>>> f = open('workfile', 'w')
```
> Code: [f.py](f.py)

The first argument is a string containing the filename. The second argument is another string containing a few characters describing the way in which the file will be used. *mode* can be `'r'` when the file will only be read, `'w'` for only writing (an existing file with the same name will be erased), and `'a'` opens the file for appending; any data written to the file is automatically added to the end. `'r+'` opens the file for both reading and writing. The *mode* argument is optional; `'r'` will be assumed if it's omitted.

Normally, files are opened in *text mode*, that means, you read and write strings from and to the file, which are encoded in a specific *encoding*. If *encoding* is not specified, the default is UTF-8 (see `open()`). Appending a `'b'` to the mode opens the file in *binary mode*. Binary mode data is read and written as `bytes` objects. You can not specify *encoding* when opening file in binary mode.

In text mode, the default when reading is to convert platform-specific line endings (`\n` on Unix, `\r\n` on Windows) to just `\n`. When writing in text mode, the default is to convert occurrences of `\n` back to platform-specific line endings. This behind-the-scenes modification to file data is fine for text files, but will corrupt binary data like that in `JPEG` or `EXE` files. Be very careful to use binary mode when reading and writing such files.

It is good practice to use the `with` keyword when dealing with file objects. The advantage is that the file is properly closed after its suite finishes, even if an exception is raised at some point. Using `with` is also much shorter than writing equivalent `try`-`finally` blocks:

``` python
>>> with open('workfile') as f:
...     read_data = f.read()

>>> # We can check that the file has been automatically closed.
>>> f.closed
True
```
> Code: [read_data.py](read_data.py)

If you're not using the `with` keyword, then you should call `f.close()` to close the file and immediately free up any system resources used by it.

> **Warning**
>
> Calling `f.write()` without using the `with` keyword or calling `f.close()` **might** result in the arguments of `f.write()` not being completely written to the disk, even if the program exits successfully.

After a file object is closed, either by a `with` statement or by calling `f.close()`, attempts to use the file object will automatically fail.

``` python
>>> f.close()
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
```
> Code: [example_01.py](example_01.py)


<!-- learning-task:start -->
### Bölüm görevi

**Görev 7.2: Dosya kipinin veriye etkisini seç**

**Odak:** r/w/a/r+, metin/binary, encoding, with/close ve kapanmış dosya.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:7.1](../7.1-fancier-output-formatting/README.md).
- Ön bilgi: [t:6](../../06-modules/README.md).

**Kaynak/ortam notu:** Kaynak 3.15 metni UTF-8 varsayılanından söz ediyor. Yerel 3.11 üzerinde aynı sonucu almak için metin dosyalarında encoding="utf-8" kullan.

#### Tek görev

1. Yalnız kendi çalışma klasöründe note.txt oluştur. open ile w kipinde "first\n" yaz, kapat; a kipinde "second\n" ekle; with ve r ile oku, blok dışında f.closed göster.

2. Aynı işlemi yeniden w ile açmanın önceki içeriğe etkisini ayrı bir kopyada dene.

3. Metin dosyası ile bir resim dosyasını açmak için kip/encoding seçimlerini yazılı karşılaştır; kapanmış dosyadan okumayı ayrı girişte dene.

#### Geçiş ölçütleri

- [ ] Okunan içerik first ve second satırları; a koruyor, w eski içeriği siliyor.
- [ ] with sonrası closed True; kapalı dosyadan okuma ValueError.
- [ ] Metin str, binary bytes ile ilişkilendirilmiş; binary kipte encoding verilmemiş.
- [ ] r varsayılan, r+ iki yönlü; satır sonu dönüşümünün binary dosyaya neden uygun olmadığı açıklanmış.
- [ ] Dosyaya yazma tamamlanması için with/close gereksinimi açıklanmış; UTF-8 açıkça verilmiş.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](7.2.1-methods-of-file-objects/README.md)
<!-- learning-task:end -->
### Sections

- [7.2.1. Methods of file objects](7.2.1-methods-of-file-objects/README.md)
- [7.2.2. Saving structured data with `json`](7.2.2-saving-structured-data-with-json/README.md)

<!-- learning-milestone:start -->
### Klasör milestone görevi

**Milestone: Dosya yaşam döngüsünü veriyle birlikte tamamla**

**Zamanı:** Bu klasörün kendi anlatımı, bütün alt bölümleri ve onların görevleri bittikten sonra.

**Odak:** Kip, imleç, kapanma ve JSON geri yüklemenin birlikte doğrulanması.

#### Önce

[Klasör anlatımı](README.md) ve [sayısal sıradaki alt görevler](../../../TASKS.md) tamamlanmış olmalı. Bu klasörün dışından yalnız daha önce işlenmiş bölüm bilgileri kullanılabilir.

#### Tek görev

1. Kendi klasöründe {"name": "Ece", "scores": [3, 6]} verisini UTF-8 JSON dosyasına yazıp yeni açılışta geri al.

2. Ayrı bir metin raporuna ilk satırı w, ikinciyi a ile yaz; iki readline sonrası EOF değerini göster.

3. Her with bloğu sonrasında closed kontrol et.

4. JSON dosyasını metin olarak okumakla load sonucunu karşılaştır.

#### Geçiş ölçütleri

- [ ] Geri gelen veri aslıyla eşit ve üzerinde liste işlemi yapılabiliyor.
- [ ] w/a seçimi önceki veriyi beklenen biçimde koruyor veya değiştiriyor.
- [ ] İmleç ve EOF kontrolü yeni dosya açılışlarıyla doğru.
- [ ] Kaynaklar kapalı; metin temsil ile sözlük birbirine karıştırılmamış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-milestone:end -->
