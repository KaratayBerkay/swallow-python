# Görev b:5.1: Eşzamanlılık iddiasını durum akışıyla sınayalım

## Önce

[b:5](../README.md) ve bu sayfanın açıklama/örnekleri.

Bu görevde verilen durumların yazılı çözümü geçerlidir; ek çalışma ortamı veya harici araç kurulumu gerekmez.

## Tek görev

A işlemine iki threadde çağrı yapılması hiçbir durumda desteklenmiyor; B yalnız dış kilitle aynı nesnede kullanılabiliyor; C ayrı nesnelerde güvenli; D aynı nesnede güvenli; E tek anda olmuş gibi gözüküyor. Beş seviyeye eşleştir. İki ayrı memoryview aynı tamponu paylaşınca "ayrı nesne" gerekçesini de değerlendir. Gerçek thread yarışı üretmek yerine verilen sıralamayı yazılı çöz; her garanti için bu sayfadaki koşulu belirt.

## Geçiş ölçütleri

- [ ] Sıra incompatible, compatible, safe on distinct objects, safe on shared objects, atomic.
- [ ] Ayrı nesne kimliği paylaşılan alt durum olmadığını kanıtlamaz.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
