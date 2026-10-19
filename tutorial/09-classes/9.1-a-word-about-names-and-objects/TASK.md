# Görev 9.1: İki adın ortak nesneye etkisini izle

**Odak:** Ad bağlama, alias ve değiştirilebilir nesnenin paylaşılması.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:3.1.3](../../03-an-informal-introduction-to-python/3.1-using-python-as-a-calculator/3.1.3-lists/README.md).
- Ön bilgi: [t:4.8](../../04-more-control-flow-tools/4.8-defining-functions/README.md).

## Tek görev

1. original = [1], alias = original kur.

2. Listeyi parametre alıp append ile değiştiren bir fonksiyon çağır; ardından alias adını [9] listesine yeniden bağla.

3. Her olaydan sonra iki adın hangi nesneyi gösterdiğini çiz.

4. Aynı akışta sayı parametresine yeni değer atamanın çağıranın sayısını neden değiştirmediğini göster.

## Geçiş ölçütleri

- [ ] Fonksiyon içindeki append her iki ad üzerinden görülüyor.
- [ ] alias yeniden bağlanınca original eski listeyi koruyor.
- [ ] Atama yeni nesne kopyalama olarak yorumlanmamış.
- [ ] Fonksiyon parametresinin de bir ad olduğu ve mutation/rebinding farkı açıklanmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
