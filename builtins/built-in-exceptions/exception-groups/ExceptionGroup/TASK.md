# Görev b:4.6.1: Hata ağacını yapısını koruyarak böl

## Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

Sürüm: Python 3.13 veya üzeri. Daha eski yorumlayıcıda yalnız bu sürüme bağlı kısmı gerekçeli yazılı iz ile çözebilirsin; çalıştırma kanıtını bekleyen olarak kaydet.

## Tek görev

İç içe ExceptionGroup içinde iki ValueError ve bir TypeError tut. Subgroup(ValueError), split(ValueError) ve eşleşmeyen subgroup sonucunu göster. Kaynaktaki derive örneğini uyarlayıp alt sınıf türünü, mesajı, notları ve traceback/cause/context bilgilerini bölme sonrasında koru. BaseExceptionGroup içine KeyboardInterrupt koymayı, ExceptionGroup içine koymakla karşılaştır; yalnız Exception içeren BaseExceptionGroup kurucusunun dönüş türünü göster. Callable condition davranışını Python 3.13+ için ayrıca incele.

## Geçiş ölçütleri

- [ ] Eşleşen ve kalan ağaçlar doğru üyeleri ve iç içeliği korur; boş eşleşme None olur.
- [ ] Derive alt sınıfı korur; split metadatayı taşır; özel kurucu gerekiyorsa kaynak örneğindeki __new__ rolü açıklanır.
- [ ] ExceptionGroup KeyboardInterrupt kabul etmez; BaseExceptionGroup kabul eder; yalnız Exception üyeli durumda otomatik ExceptionGroup seçilebilir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
