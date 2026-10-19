# Milestone: Hata bilgisini kaybetmeyen okuyucu yaz

## Önce

Bu klasördeki bütün bölüm görevleri ve alt klasör milestone kontrolleri tamamlanmış olmalı. Sırayı [görev dizininden](../../TASKS.md) kontrol et.

## Tek görev

Metin kayıttan ad ve puan okuyan küçük fonksiyon yaz. Yanlış tür, geçersiz sayı ve eksik alan için farklı hata davranışını seç; çağıran katmanda kendi AlanHatasi türüne `raise ... from asil` ile dönüştür. Birden çok bağımsız kaydın hatasını ExceptionGroup içinde topla; başarılı kayıtları koru.

## Geçiş ölçütleri

- [ ] Dar handlerlar doğru yerde çalışır; SystemExit/KeyboardInterrupt yanlışlıkla yutulmaz.
- [ ] Asıl cause ve alan açıklaması korunur; grup içindeki hatalar türlerine göre ayrılabilir.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md)
