## `ConnectionAbortedError`

```
ConnectionAbortedError
```

A subclass of [ConnectionError](../ConnectionError/README.md), raised when a connection attempt
is aborted by the peer.
Corresponds to `errno` [ECONNABORTED](https://docs.python.org/3.15/library/errno.html#errno.ECONNABORTED).

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.4.43: ConnectionAbortedError teşhisini gerekçelendir**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Verilen olay: Bağlantı girişiminin karşı uç tarafından iptal edilmesi. Beklenen hata türünü veya normal sonucu çıkar. Sistem olayıysa yalnız yazılı teşhis yap; gerçek arıza üretme. Basit veri işlemi ise küçük yerel örnekle doğrula. Bu türün neden uygun olduğunu, yakın ama farklı bir durumdan nasıl ayrıldığını açıkla.

#### Geçiş ölçütleri

- [ ] ConnectionAbortedError; reddedilme veya kurulmuş bağlantının resetlenmesiyle aynı olay değildir.
- [ ] Sadece hata adı değil, tetikleyici koşul ve ilgili yakalama sınırı gerekçelendirilmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../ConnectionRefusedError/README.md)
<!-- learning-task:end -->
