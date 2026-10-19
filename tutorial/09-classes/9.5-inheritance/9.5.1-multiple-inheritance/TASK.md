# Görev 9.5.1: Elmas hiyerarşide arama sırasını çıkar

**Odak:** Çoklu kalıtım, soldan sağa öncelik, ortak atanın tek kez sıralanması ve monotonic düzen.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:9.5](../README.md).

## Tek görev

1. A sınıfında label = "A"; B(A) içinde yeni nitelik yok; C(A) içinde label = "C"; D(B, C) olsun.

2. D().label değerinin B üzerinden doğrudan A seçilerek bulunup bulunamayacağını bölümdeki ortak atanın tek kez ve alt sınıflardan sonra sıralanması kuralıyla açıkla, sonra dene.

3. B içine label = "B" eklenince sonucu yeniden çıkar.

4. Bu adımda cooperative super zinciri yazman gerekmiyor.

## Geçiş ölçütleri

- [ ] İlk sonuç C; B üzerinde değer yokken ortak A, C önüne yanlışlıkla alınmamış.
- [ ] İkinci sonuç B; D taban sırası B sonra C olarak etkili.
- [ ] Ortak A iki kez aranacak biçimde sıralanmamış; B/C öncelikleri korunmuş.
- [ ] Basit depth-first sezgisinin elmas durumda yeterli olmadığı somut örnekle açıklanmış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
