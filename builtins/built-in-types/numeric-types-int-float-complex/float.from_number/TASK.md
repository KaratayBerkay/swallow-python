# Görev b:2.4.7: float.from_number sınırını göster

## Önce

[b:2.4](../README.md) ve bu sayfanın açıklama/örnekleri.

Sürüm: Python 3.14 veya üzeri. Daha eski yorumlayıcıda yalnız bu sürüme bağlı kısmı gerekçeli yazılı iz ile çözebilirsin; çalıştırma kanıtını bekleyen olarak kaydet.

## Tek görev

`float.from_number(7)`, `float.from_number("7")` ve yalnız __index__ döndüren hazır nesne için çağrı akışını çıkar. __float__ da varsa önceliği belirt.

## Geçiş ölçütleri

- [ ] 7.0, TypeError; __float__ varsa önce o, yoksa __index__ kullanılır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
