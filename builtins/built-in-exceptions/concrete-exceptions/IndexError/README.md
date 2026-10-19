## `IndexError`

```
IndexError
```

Raised when a sequence subscript is out of range.  (Slice indices are
silently truncated to fall in the allowed range; if an index is not an
integer, [TypeError](../TypeError/README.md) is raised.)

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.4.9: IndexError teşhisini gerekçelendir**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Verilen olay: s=[4] için s[3], s[:3] ve s["x"] denemeleri. Beklenen hata türünü veya normal sonucu çıkar. Sistem olayıysa yalnız yazılı teşhis yap; gerçek arıza üretme. Basit veri işlemi ise küçük yerel örnekle doğrula. Bu türün neden uygun olduğunu, yakın ama farklı bir durumdan nasıl ayrıldığını açıkla.

#### Geçiş ölçütleri

- [ ] IndexError, [4], TypeError; indeks taşmasıyla kesilen dilim ayrılır.
- [ ] Sadece hata adı değil, tetikleyici koşul ve ilgili yakalama sınırı gerekçelendirilmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../KeyError/README.md)
<!-- learning-task:end -->
