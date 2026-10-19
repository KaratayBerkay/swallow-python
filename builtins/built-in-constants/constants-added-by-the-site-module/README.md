The [site](https://docs.python.org/3.15/library/site.html#module-site) module (which is imported automatically during startup, except
if the [-S](https://docs.python.org/3.15/using/cmdline.html#cmdoption-S) command-line option is given) adds several constants to the
built-in namespace.  They are useful for the interactive interpreter shell and
should not be used in programs.


<!-- learning-task:start -->
### Bölüm görevi

**Görev b:1.7: Etkileşimli yardımcıların sınırını belirle**

#### Önce

[b:1](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Normal başlatılan interpreter ile -S kullanılarak site yüklenmeden başlatılan interpreterı karşılaştır. quit, help, license adlarının bulunmasına güvenen bir uygulamanın varsayımını ve neden bu yardımcıların etkileşimli kullanım için olduğunu açıkla.

#### Geçiş ölçütleri

- [ ] Normal site kurulumu yardımcı adları ekler; -S ile otomatik eklenmelerine güvenilmez.
- [ ] Uygulama davranışı bu etkileşimli nesnelerin varlığına bağlanmamıştır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](quit/README.md)
<!-- learning-task:end -->
## Entries

- [`quit()`](quit/README.md)
- [`help`](help/README.md)
- [`copyright`](copyright/README.md)
- [`license`](license/README.md)
- [`exit()`](exit/README.md)
- [`credits`](credits/README.md)

<!-- learning-milestone:start -->
### Klasör milestone görevi

**Milestone: Etkileşimli oturumu tanı**

#### Önce

Bu klasördeki bütün bölüm görevleri ve alt klasör milestone kontrolleri tamamlanmış olmalı. Sırayı [görev dizininden](../../../TASKS.md) kontrol et.

#### Tek görev

Tek yazılı oturumda help ile bir nesnenin belgesine ulaşmayı, license ile tam metni görmeyi, credits/copyright farkını ve quit(2) ile çıkışı göster. -S ile başlayan oturumda hangi varsayımın bozulduğunu belirt.

#### Geçiş ölçütleri

- [ ] Yazdırma ile çağrı davranışları ayrılmış; çıkış SystemExit(code=2) olarak açıklanmıştır.
- [ ] Site yardımcılarının otomatik eklenmediği durumda uygulama bunlara bağımlı değildir.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-milestone:end -->
