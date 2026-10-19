# Görev 8.6: Alan hatasını doğru exception ailesine yerleştir

**Odak:** Exception alt sınıfı, anlamlı Error adı ve basit özel hata.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:8.4](../8.4-raising-exceptions/README.md).
- Ön bilgi: [t:8.3](../8.3-handling-exceptions/README.md).

## Tek görev

1. Bir görev sayacında negatif değer için NegativeCountError adlı özel hata gerektiğini düşün.

2. Yeni sınıf yazmak yerine tasarım notunda adını, hangi sınıftan türeyeceğini, hangi hatalarda kullanılacağını ve except NegativeCountError ile except Exception handlerlarının kapsam ilişkisini yaz.

3. Sınıf yazım sözdizimi bu kısa bölümde örneklenmediği için uygulama beklenmiyor.

## Geçiş ölçütleri

- [ ] Negatif görev sayısı alan hatasıyla ilişkilendirilmiş; taban Exception.
- [ ] Error son eki ve sade hata tasarımı gerekçeli.
- [ ] Özel handler yalnız ilgili aileyi, Exception daha genel aileyi yakalıyor; handler sırası doğru.
- [ ] Dosya bulunamaması gibi ilgisiz bir hatanın bu isimle yeniden etiketlenmemesi açıklanmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
