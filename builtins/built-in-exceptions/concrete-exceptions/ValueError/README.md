## `ValueError`

```
ValueError
```

Raised when an operation or function receives an argument that has the
right type but an inappropriate value, and the situation is not described by a
more precise exception such as [IndexError](../IndexError/README.md).

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.4.34: ValueError teşhisini gerekçelendir**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Verilen olay: int("abc") ve [1][5] denemeleri. Beklenen hata türünü veya normal sonucu çıkar. Sistem olayıysa yalnız yazılı teşhis yap; gerçek arıza üretme. Basit veri işlemi ise küçük yerel örnekle doğrula. Bu türün neden uygun olduğunu, yakın ama farklı bir durumdan nasıl ayrıldığını açıkla.

#### Geçiş ölçütleri

- [ ] İlki doğru str türündeki geçersiz değer için ValueError, ikincisi daha özel IndexError olur.
- [ ] Sadece hata adı değil, tetikleyici koşul ve ilgili yakalama sınırı gerekçelendirilmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../ZeroDivisionError/README.md)
<!-- learning-task:end -->
