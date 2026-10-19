# Görev b:2.15: Çağrı ve depolama nesnelerini ayır

## Önce

[b:2](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Bir modül, Python fonksiyonu, örneğe bağlı yöntem ve sınıf için ad çözümleme/çağrı akışını tek tabloyla göster. `nesne.yontem(x)` ile fonksiyona nesneyi açık vermeyi karşılaştır. Fonksiyon kodu, global namespace, sınıf namespace ve örnek namespace sorumluluklarını ayır. None, NotImplemented ve Ellipsis türlerini de yalnız uygun rollerine yerleştir.

## Geçiş ölçütleri

- [ ] Bağlı yöntemde örnek örtük ilk argümandır; modül erişimi modül namespace üzerinden yürür.
- [ ] Kod nesnesi tek başına global bağlam taşıyan fonksiyon değildir; sınıf ve örnek alanları ayrıdır.
- [ ] Özel tekil nesneler fonksiyon veya container yerine konmamıştır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
