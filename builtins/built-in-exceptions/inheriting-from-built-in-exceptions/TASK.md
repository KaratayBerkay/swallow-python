# Görev b:4.2: Tek hata sorumluluğu tasarla

## Önce

[b:4](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

ValueError alt sınıfı bir AlanHatasi yaz; geçersiz yaş değeri için yükselt ve hem kendi türü hem ValueError ile ayrı denemelerde yakala. İki built-in exceptiondan aynı anda kalıtım almak yerine tek kol seçimini açıklayarak args bilgisini koru.

## Geçiş ölçütleri

- [ ] Özel tür bir Exception alt türüdür; iki yakalama da kalıtım gereği çalışır.
- [ ] Tek built-in kalıtım kolu seçilir; olası bellek düzeni ve sürüm uyumu çatışmaları gerekçelendirilir.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
