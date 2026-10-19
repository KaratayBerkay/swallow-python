## `UnicodeDecodeError`

```
UnicodeDecodeError
```

Raised when a Unicode-related error occurs during decoding.  It is a subclass of
[UnicodeError](../UnicodeError/README.md).

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.4.32: UnicodeDecodeError teşhisini gerekçelendir**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Verilen olay: Geçersiz baytların strict kod çözücüye verilmesi. Beklenen hata türünü veya normal sonucu çıkar. Sistem olayıysa yalnız yazılı teşhis yap; gerçek arıza üretme. Basit veri işlemi ise küçük yerel örnekle doğrula. Bu türün neden uygun olduğunu, yakın ama farklı bir durumdan nasıl ayrıldığını açıkla.

#### Geçiş ölçütleri

- [ ] UnicodeDecodeError; yön bytes -> str, UnicodeError ve ValueError kolundadır.
- [ ] Sadece hata adı değil, tetikleyici koşul ve ilgili yakalama sınırı gerekçelendirilmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../UnicodeTranslateError/README.md)
<!-- learning-task:end -->
