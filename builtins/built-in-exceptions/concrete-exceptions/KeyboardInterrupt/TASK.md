# Görev b:4.4.11: KeyboardInterrupt teşhisini gerekçelendir

## Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Verilen olay: Kullanıcı kesme tuşuna basıyor; kod yalnız except Exception kullanıyor. Beklenen hata türünü veya normal sonucu çıkar. Sistem olayıysa yalnız yazılı teşhis yap; gerçek arıza üretme. Basit veri işlemi ise küçük yerel örnekle doğrula. Bu türün neden uygun olduğunu, yakın ama farklı bir durumdan nasıl ayrıldığını açıkla.

## Geçiş ölçütleri

- [ ] KeyboardInterrupt bu handlerı aşar; BaseException kolundadır; keyfi kesintiler tutarsız durum bırakabilir.
- [ ] Sadece hata adı değil, tetikleyici koşul ve ilgili yakalama sınırı gerekçelendirilmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
