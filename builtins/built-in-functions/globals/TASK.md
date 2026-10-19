# Görev b:3.30: globals sözleşmesini uygula

## Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Modül düzeyinde `puan=3` tanımla. `def oku(): return globals()["puan"]` yaz. Globals sözlüğündeki puan değerini 8 yapıp fonksiyonu yeniden çağır; sözlüğün bir kopya mı canlı namespace mi olduğunu kanıtla.

## Geçiş ölçütleri

- [ ] Sonuç önce 3 sonra 8 olur; globals modülün canlı sözlüğüdür.
- [ ] Fonksiyonun tanımlandığı modülün global alanı kullanılır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
