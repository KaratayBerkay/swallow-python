# Görev 8.2: Hata izinden bozulan işlemi bul

**Odak:** Exception türü, mesajı, traceback bağlamı ve parse hatasından ayrım.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:8.1](../8.1-syntax-errors/README.md).

## Tek görev

1. Yeni bir oturumda 6 / 0, tanımlanmamış missing_name + 1 ve "count=" + 3 ifadelerini ayrı ayrı dene.

2. Her biri için türü, mesajın anlattığı bozuk işlemi ve ilgili kaynak satırını not et.

3. Hepsini tek dosyada peş peşe yazınca neden yalnız ilk hatayı görebileceğini açıkla.

## Geçiş ölçütleri

- [ ] Türler ZeroDivisionError, NameError, TypeError.
- [ ] Hata mesajı ezberlenmeden ilgili bölme/ad erişimi/toplama işlemi gösterilmiş.
- [ ] İfadeler sözdizimsel olarak geçerli; sorun çalışma anında.
- [ ] Yakalanmayan hata mevcut yürütmeyi durdurduğu için sonraki satırların kendiliğinden denenmediği açıklanmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
