## `OverflowError`

```
OverflowError
```

Raised when the result of an arithmetic operation is too large to be
represented.  This cannot occur for integers (which would rather raise
[MemoryError](../MemoryError/README.md) than give up).  However, for historical reasons,
OverflowError is sometimes raised for integers that are outside a required
range.   Because of the lack of standardization of floating-point exception
handling in C, most floating-point operations are not checked.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.4.16: OverflowError teşhisini gerekçelendir**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Verilen olay: 256 değerini signed=False ile yalnız bir bayta dönüştürme. Beklenen hata türünü veya normal sonucu çıkar. Sistem olayıysa yalnız yazılı teşhis yap; gerçek arıza üretme. Basit veri işlemi ise küçük yerel örnekle doğrula. Bu türün neden uygun olduğunu, yakın ama farklı bir durumdan nasıl ayrıldığını açıkla.

#### Geçiş ölçütleri

- [ ] OverflowError; sınırsız int toplaması her büyük sonuçta otomatik taşma vermez.
- [ ] Sadece hata adı değil, tetikleyici koşul ve ilgili yakalama sınırı gerekçelendirilmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../PythonFinalizationError/README.md)
<!-- learning-task:end -->
