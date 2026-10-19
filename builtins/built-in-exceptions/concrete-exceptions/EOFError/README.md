## `EOFError`

```
EOFError
```

Raised when the [input()](../../../built-in-functions/input/README.md) function hits an end-of-file condition (EOF)
without reading any data. (Note: the [io.TextIOBase.read()](https://docs.python.org/3.15/library/io.html#io.TextIOBase.read) and
[io.IOBase.readline()](https://docs.python.org/3.15/library/io.html#io.IOBase.readline) methods return an empty string when they hit EOF.)

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.4.3: EOFError teşhisini gerekçelendir**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Verilen olay: Input hiçbir veri okumadan EOF alıyor; başka denemede yalnız boş satır okunuyor. Beklenen hata türünü veya normal sonucu çıkar. Sistem olayıysa yalnız yazılı teşhis yap; gerçek arıza üretme. Basit veri işlemi ise küçük yerel örnekle doğrula. Bu türün neden uygun olduğunu, yakın ama farklı bir durumdan nasıl ayrıldığını açıkla.

#### Geçiş ölçütleri

- [ ] EOF ilkinde EOFError; boş satırda boş str döner, EOFError değildir.
- [ ] Sadece hata adı değil, tetikleyici koşul ve ilgili yakalama sınırı gerekçelendirilmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../FloatingPointError/README.md)
<!-- learning-task:end -->
