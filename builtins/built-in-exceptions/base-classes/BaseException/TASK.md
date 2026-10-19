# Görev b:4.3.1: Hata nesnesini veri kaybetmeden taşı

## Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

`e=ValueError("alan",7)` oluştur; args, str(e), __traceback__ ve add_note ile eklenen __notes__ alanını incele. Bir try/except içinde yakalanmış hatanın tracebackini başka bir hata nesnesine with_traceback ile bağla; dönen nesnenin kimliğini göster. add_note için metin dışı girdiyi dene.

## Geçiş ölçütleri

- [ ] Args ("alan",7), notlar ayrı listede; hata yükseltilmeden traceback None olabilir.
- [ ] With_traceback aynı hata nesnesini döndürür; traceback ile mesaj ayrı bilgilerdir.
- [ ] Add_note metin dışı girdide TypeError verir; hata notu ilk args değerlerini değiştirmez.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
