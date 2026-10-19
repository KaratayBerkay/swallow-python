The implementation adds a few special read-only attributes to several object
types, where they are relevant.  Some of these are not reported by the
[dir()](../../built-in-functions/dir/README.md) built-in function.

- [`definition.__name__`](definition.__name__/README.md) — The name of the class, function, method, descriptor, or generator instance.
- [`definition.__qualname__`](definition.__qualname__/README.md) — The qualified name of the class, function, method, descriptor, or generator instance.
- [`definition.__module__`](definition.__module__/README.md) — The name of the module in which a class or function was defined.
- [`definition.__doc__`](definition.__doc__/README.md) — The documentation string of a class or function, or None if undefined.
- [`definition.__type_params__`](definition.__type_params__/README.md) — The type parameters of generic classes, functions, and type aliases.

<!-- learning-task:start -->
## Bölüm görevi

**Görev b:2.16: Metaveri ile nesne durumunu ayır**

### Önce

[b:2](../README.md) ve bu sayfanın açıklama/örnekleri.

### Tek görev

Bir sınıf ve fonksiyon oluşturup __name__, __qualname__, __module__, __doc__ değerlerini bul. Dir çıktısında her özel niteliğin mutlaka listeleneceğini varsaymanın neden hatalı olduğunu açıklayarak uygun nesne üzerinden erişimi göster.

### Geçiş ölçütleri

- [ ] Dört nitelik ad, nitelikli ad, tanımlandığı modül ve belge metni olarak ayrılmıştır.
- [ ] Her özel nitelik her nesnede bulunmaz; dir eksiksiz sözleşme değildir.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](definition.__name__/README.md)
<!-- learning-task:end -->

<!-- learning-milestone:start -->
## Klasör milestone görevi

**Milestone: Tanımın kimliğini raporla**

### Önce

Bu klasördeki bütün bölüm görevleri ve alt klasör milestone kontrolleri tamamlanmış olmalı. Sırayı [görev dizininden](../../../TASKS.md) kontrol et.

Sürüm farkında yalnız yeni özelliği gerekçeli yazılı iz ile inceleyebilirsin; çalıştırma kanıtını bekleyen olarak kaydet.

### Tek görev

Bir sınıf ve iç içe fonksiyon için kısa ad, nitelikli ad, tanımlayan modül ve belgeyi aynı raporda göster. Farklı değişken adına bağlayınca neyin aynı kaldığını açıkla; Python 3.12 tür parametresi metadatasını normal/generic ayrımıyla ekle.

### Geçiş ölçütleri

- [ ] Tanım adı ile referans değişken adı ayrılır.
- [ ] Eksik belge None; özel metadatanın bütün nesnelerde var olduğu varsayılmaz.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../integer-string-conversion-length-limitation/README.md)
<!-- learning-milestone:end -->
