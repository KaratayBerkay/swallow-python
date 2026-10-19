# Görev b:4.4.27: SystemExit teşhisini gerekçelendir

## Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Verilen olay: SystemExit(3), SystemExit(None) ve SystemExit("hata") nesneleri. Beklenen hata türünü veya normal sonucu çıkar. Sistem olayıysa yalnız yazılı teşhis yap; gerçek arıza üretme. Basit veri işlemi ise küçük yerel örnekle doğrula. Bu türün neden uygun olduğunu, yakın ama farklı bir durumdan nasıl ayrıldığını açıkla.

## Geçiş ölçütleri

- [ ] Code alanları sırasıyla 3, None, "hata"; yakalanmazsa çıkış durumları 3, 0, 1; Exception handlerı yakalamaz.
- [ ] Sadece hata adı değil, tetikleyici koşul ve ilgili yakalama sınırı gerekçelendirilmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
