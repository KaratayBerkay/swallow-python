## `ConnectionError`

```
ConnectionError
```

A base class for connection-related issues.

Subclasses are [BrokenPipeError](../BrokenPipeError/README.md), [ConnectionAbortedError](../ConnectionAbortedError/README.md),
[ConnectionRefusedError](../ConnectionRefusedError/README.md) and [ConnectionResetError](../ConnectionResetError/README.md).

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.4.41: ConnectionError teşhisini gerekçelendir**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Verilen olay: BrokenPipeError, ConnectionRefusedError ve KeyError örnekleri. Beklenen hata türünü veya normal sonucu çıkar. Sistem olayıysa yalnız yazılı teşhis yap; gerçek arıza üretme. Basit veri işlemi ise küçük yerel örnekle doğrula. Bu türün neden uygun olduğunu, yakın ama farklı bir durumdan nasıl ayrıldığını açıkla.

#### Geçiş ölçütleri

- [ ] İlk ikisi ConnectionError ile yakalanır; KeyError yakalanmaz.
- [ ] Sadece hata adı değil, tetikleyici koşul ve ilgili yakalama sınırı gerekçelendirilmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../BrokenPipeError/README.md)
<!-- learning-task:end -->
