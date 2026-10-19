# Görev b:4: Yakalama sınırını uygulamayla kanıtla

## Önce

[t:8.3](../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

ValueError alt sınıfı bir VeriHatasi oluştur. İki handler sırasını karşılaştır: önce ValueError sonra VeriHatasi; önce VeriHatasi sonra ValueError. Aynı isimde fakat farklı sınıf nesneleri olan iki hatanın birbirini yakalamadığını göster.

## Geçiş ölçütleri

- [ ] Alt tür önce yazılırsa özel handler çalışır; üst tür önce yazılırsa alt türü de o yakalar.
- [ ] Adların eşit olması exception sınıflarını eşdeğer yapmaz; kalıtım ilişkisi gerekir.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md)
