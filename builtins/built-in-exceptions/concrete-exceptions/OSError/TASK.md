# Görev b:4.4.15: Sistem hatasının alanlarını koru

## Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

`e=OSError(2,"yok","ornek.txt")` nesnesini oluştur. Tür, errno, strerror, filename ve args değerlerini kaydet. Mesajı eşleştirerek karar vermek yerine hata türü/alanlarını kullanmanın neden daha doğru olduğunu açıkla; verilmemiş filename2 ve platforma özgü winerror alanlarını genelleme.

## Geçiş ölçütleri

- [ ] Bu kurucu FileNotFoundError alt türünü verir; errno=2, filename="ornek.txt", args=(2,"yok").
- [ ] Dosya adı mesajdan ayrı alandır; platforma özel alanlar her ortamda bulunmak zorunda değildir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
