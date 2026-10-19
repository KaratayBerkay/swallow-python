# Görev b:2.6.7: generator.close durum geçişini kanıtla

## Önce

[b:2.6](../README.md) ve bu sayfanın açıklama/örnekleri.

Sürüm: Python 3.13 veya üzeri. Daha eski yorumlayıcıda yalnız bu sürüme bağlı kısmı gerekçeli yazılı iz ile çözebilirsin; çalıştırma kanıtını bekleyen olarak kaydet.

## Tek görev

Yield noktasında durdurulmuş üç generator düşün: A GeneratorExit ile normal sonlanıyor; B GeneratorExit yakalayıp yeni bir değer yield ediyor; C yakalayıp return 7 yapıyor. Close sonuçlarını ve tekrar close çağrısını izle. Sonuçları çağrı -> durulan nokta -> sonraki durum tablosuyla göster.

## Geçiş ölçütleri

- [ ] A None, B RuntimeError; C Python 3.13+ için 7 döndürür; kapalı generator close None olur.
- [ ] Çağrı ve tüketim/ilerleme anı birbirinden ayrılmıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
