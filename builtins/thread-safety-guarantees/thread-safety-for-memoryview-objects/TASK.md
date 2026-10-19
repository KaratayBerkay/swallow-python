# Görev b:5.6: Eşzamanlılık iddiasını durum akışıyla sınayalım

## Önce

[b:5](../README.md) ve bu sayfanın açıklama/örnekleri.

Bu görevde verilen durumların yazılı çözümü geçerlidir; ek çalışma ortamı veya harici araç kurulumu gerekmez.

## Tek görev

Aynı bytearray tamponunun iki görünümü var; biri toreadonly ile elde edilmiş. B yazarken A salt okunur görünümden okuyor. Durumu immutable bytes tamponuyla karşılaştır. Bir görünümün release edilmesiyle diğerinin yaşamını ve yeniden boyutlandırma engelini ayır. Gerçek thread yarışı üretmek yerine verilen sıralamayı yazılı çöz; her garanti için bu sayfadaki koşulu belirt.

## Geçiş ölçütleri

- [ ] Readonly erişim kaynağı dondurmaz; aynı mutable bölgeye eşzamanlı okuma/yazma dış eşgüdüm gerektirir.
- [ ] Bytes üzerinden eşzamanlı okumalar güvenlidir; view metadatası güvenliği tampon verisinin güvenliği değildir.
- [ ] Bütün exportlar bırakılmadan tampon yeniden boyutlandırma engeli kalkmış sayılmaz.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
