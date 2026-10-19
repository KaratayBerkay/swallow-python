# Görev 8.4: Hatayı üret ve üst çağırana aktar

**Odak:** raise instance/class ve except içinde çıplak raise ile yeniden yükseltme.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:8.3](../8.3-handling-exceptions/README.md).

## Tek görev

1. Negatif sayı için ValueError("negative count") yükselten check_count(n) yaz; sıfır ve pozitifte sayıyı döndür.

2. Çağıran bir try/except içinde hatayı görüp "checked" mesajı bastıktan sonra çıplak raise ile yeniden aktar. 2 ve -1 durumlarını ayrı çalıştır; ayrıca raise ValueError ile raise ValueError() farkını bölümün kuralıyla açıkla.

## Geçiş ölçütleri

- [ ] 2 normal dönüyor; -1 aynı hata türü ve mesajıyla üst çağırana ulaşıyor.
- [ ] checked mesajı hata yolunda yeniden raise öncesinde basılıyor.
- [ ] Çıplak raise yeni hata üretmek yerine mevcut hatayı aktarıyor.
- [ ] Sınıf verilirse argümansız örnek oluşturulduğu açıklanmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
