# Görev b:5.2: Eşzamanlılık iddiasını durum akışıyla sınayalım

## Önce

[b:5](../README.md) ve bu sayfanın açıklama/örnekleri.

Bu görevde verilen durumların yazılı çözümü geçerlidir; ek çalışma ortamı veya harici araç kurulumu gerekmez.

## Tek görev

lst=[1] için A threadi if lst kontrolünü geçiyor; B pop ile öğeyi alıyor; A pop çağırıyor. Akışı çöz. Tek öğe okuma, append/pop(), üyelik/index/count taraması, sort, eleman kaydırmalı pop(0), extend(list) ve extend(özel iterable) garantilerini sınıflandır. Gerçek thread yarışı üretmek yerine verilen sıralamayı yazılı çöz; her garanti için bu sayfadaki koşulu belirt.

## Geçiş ölçütleri

- [ ] A son adımda IndexError alabilir; iki ayrı güvenli çağrı atomik bir check-then-act değildir.
- [ ] Okuma/append/pop() atomik; taramalar eşzamanlı değişiklik görebilir; sort atomik değildir, liste geçici boş görünür.
- [ ] Extend girdi türü ve kaydırmalı işlemlerin lock-free okuyuculara etkisi ayrılmıştır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
