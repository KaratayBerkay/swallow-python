# Görev b:4.7: Handler tasarımını ağaçtan çıkar

## Önce

[b:4](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

IndexError, ModuleNotFoundError, PermissionError, KeyboardInterrupt ve GeneratorExit için en yakın ortak aileleri ağaçtan bul. Hepsini except Exception ile yakalama iddiasını değerlendir; LookupError ve OSError ile hangi alt kümelerin yakalandığını göster.

## Geçiş ölçütleri

- [ ] İlk üç Exception altında; son ikisi doğrudan BaseException kolundadır.
- [ ] LookupError IndexErrorı, OSError PermissionErrorı yakalar; ModuleNotFoundError ImportError kolundadır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
