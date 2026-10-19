# Görev b:5.5: Eşzamanlılık iddiasını durum akışıyla sınayalım

## Önce

[b:5](../README.md) ve bu sayfanın açıklama/örnekleri.

Bu görevde verilen durumların yazılı çözümü geçerlidir; ek çalışma ortamı veya harici araç kurulumu gerekmez.

## Tek görev

ba içinde 65 varken A üyelik kontrolünü geçiyor; B bu değeri kaldırıyor; A remove(65) yapıyor. Akışı çöz. Len, tek indeks/dilim, copy, eşitlik/birleştirme ve iterasyon için garanti düzeyini ayır; kopya üzerinden iterasyon çözümünün sınırını açıkla. Gerçek thread yarışı üretmek yerine verilen sıralamayı yazılı çöz; her garanti için bu sayfadaki koşulu belirt.

## Geçiş ölçütleri

- [ ] A ValueError alabilir; check-then-act atomik değildir.
- [ ] Len atomik; eşitlik/birleştirme kilitsiz ara durum görebilir; copy üzerinde iterasyon özgün ba değişiminden ayrılır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
