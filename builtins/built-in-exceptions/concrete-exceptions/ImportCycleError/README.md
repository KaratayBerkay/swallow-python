## `ImportCycleError`

```
ImportCycleError
```

A subclass of [ImportError](../ImportError/README.md) which is raised when a lazy import fails
because it (directly or indirectly) tries to import itself.

> *Added in version 3.15.*

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.4.8: ImportCycleError teşhisini gerekçelendir**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

Sürüm: Python 3.15 veya üzeri. Daha eski yorumlayıcıda yalnız bu sürüme bağlı kısmı gerekçeli yazılı iz ile çözebilirsin; çalıştırma kanıtını bekleyen olarak kaydet.

#### Tek görev

Verilen olay: Lazy importun dolaylı olarak kendisini yeniden import etmeye çalışması. Beklenen hata türünü veya normal sonucu çıkar. Sistem olayıysa yalnız yazılı teşhis yap; gerçek arıza üretme. Basit veri işlemi ise küçük yerel örnekle doğrula. Bu türün neden uygun olduğunu, yakın ama farklı bir durumdan nasıl ayrıldığını açıkla.

#### Geçiş ölçütleri

- [ ] Python 3.15 ImportCycleError; ImportError alt türüdür.
- [ ] Sadece hata adı değil, tetikleyici koşul ve ilgili yakalama sınırı gerekçelendirilmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../IndexError/README.md)
<!-- learning-task:end -->
