# Görev 9.2: Bir adı nerede aradığını ve nereye yazdığını ayır

**Odak:** Namespace, LEGB, yerel/global/nonlocal bağlama ve fonksiyonun tanımlandığı modül.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:9.1](../9.1-a-word-about-names-and-objects/README.md).
- Ön bilgi: [t:6.1](../../06-modules/6.1-more-on-modules/README.md).

## Tek görev

1. Modül düzeyinde label = "module" kur. outer içinde label = "outer"; içindeki read yalnız label okusun, change_local yeni yerel label atasın, change_outer nonlocal ile outer değerini, change_module global ile modül değerini değiştirsin.

2. Çağrılar arasına print ekleyip her okuma/yazmanın hangi namespace kullandığını not et.

3. Fonksiyon başka modülden çağrılsaydı global hedefin neresi olacağını açıkla.

## Geçiş ölçütleri

- [ ] Normal okuma en yakın çevreleyen label değerini buluyor.
- [ ] Normal atama yalnız iç fonksiyona, nonlocal outer alanına, global tanımın modülüne yazıyor.
- [ ] Yerel/çevreleyen/global/builtins arama sırası belirtilmiş.
- [ ] Ad alanının oluşturulma anı ile kapsamın kaynak kod konumu ayrılmış.
- [ ] del ve import/def işlemlerinin de ad bağlamasına etkisi açıklanmış; sınıf kapsamı ayrıntıları istenmemiş.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
