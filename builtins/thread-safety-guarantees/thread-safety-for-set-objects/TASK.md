# Görev b:5.4: Eşzamanlılık iddiasını durum akışıyla sınayalım

## Önce

[b:5](../README.md) ve bu sayfanın açıklama/örnekleri.

Bu görevde verilen durumların yazılı çözümü geçerlidir; ek çalışma ortamı veya harici araç kurulumu gerekmez.

## Tek görev

s={1} için A üyelik kontrolünü geçiyor; B remove(1) yapıyor; A remove(1) yapıyor. Sonucu, discard seçeneğiyle karşılaştır. Len, membership, copy, operatörler ve iterable alan yöntemlerde iki tarafın kilitlenme koşullarını ayır. Gerçek thread yarışı üretmek yerine verilen sıralamayı yazılı çöz; her garanti için bu sayfadaki koşulu belirt.

## Geçiş ölçütleri

- [ ] İkinci remove KeyError verebilir; discard eksik üyede hata vermez, bütün algoritmaya atomiklik kazandırmaz.
- [ ] Len atomik, üyelik eşzamanlı değişimi görebilir; yöntem/operatör ve argüman türü garantileri farklıdır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
