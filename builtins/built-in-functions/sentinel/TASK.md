# Görev b:3.62: sentinel sözleşmesini uygula

## Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

Sürüm: Python 3.15 veya üzeri. Daha eski yorumlayıcıda yalnız bu sürüme bağlı kısmı gerekçeli yazılı iz ile çözebilirsin; çalıştırma kanıtını bekleyen olarak kaydet.

## Tek görev

`EKSIK=sentinel("EKSIK")` ile varsayılanı None olabilen bir fonksiyonda verilmemiş argümanı ayır. Aynı adla ikinci sentinel oluştur; is karşılaştırmasını, bool sonucunu ve repr özelleştirmesini dene.

## Geçiş ölçütleri

- [ ] Verilmemiş argüman, açık None ve açık 0 üç ayrı durumdur.
- [ ] Aynı adlı iki çağrı farklı nesnelerdir; sentinel truthy olur; denetim is ile yapılır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
