# Görev b:5: Garanti kapsamını sınırla

## Önce

[t:11.4](../../tutorial/11-brief-tour-of-the-standard-library-part-ii/11.4-multi-threading/README.md) ve bu sayfanın açıklama/örnekleri.

Bu görevde verilen durumların yazılı çözümü geçerlidir; ek çalışma ortamı veya harici araç kurulumu gerekmez.

## Tek görev

GIL açık Python, GIL kapalı free-threaded Python ve farklı Python implementasyonu için bu sayfadaki garantilerin kapsamını yaz. "Her built-in kullanımı artık tek adımda güvenlidir" iddiasının neden sayfadan çıkmadığını açıkla.

## Geçiş ölçütleri

- [ ] Garantiler free-threaded/GIL kapalı bağlamda okunur; başka çalışma koşullarına koşulsuz taşınmaz.
- [ ] Tek işlem garantisi bütün kullanıcı algoritmasının atomik olduğu anlamına gelmez.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md)
