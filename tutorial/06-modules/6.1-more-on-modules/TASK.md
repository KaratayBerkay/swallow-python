# Görev 6.1: İçe aktarmanın adlara ve başlangıca etkisini izle

**Odak:** İlk importta yürütme, modül kapsamı, from/as/* ve reload.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:6](../README.md).

## Tek görev

1. counts.py kopyasına üst düzeyde print("loaded"), public_value = 1 ve _internal = 2 ekle.

2. Yeni oturumda iki kez import et.

3. Ayrı yeni oturumlarda from counts import count_items, import counts as c ve from counts import * deneyerek hangi adların kullanılabildiğini not et.

4. Dosyadaki public_value değerini değiştirip yeniden import ile importlib.reload farkını göster.

## Geçiş ölçütleri

- [ ] Aynı oturumda iki import başlangıç mesajını yalnız bir kez basıyor; reload yeniden yürütüyor.
- [ ] from biçimi işlevi, as biçimi c adını bağlıyor.
- [ ] Yıldızlı aktarım _internal adını getirmiyor; isim gizleme riski somut bir adla açıklanmış.
- [ ] Modülün kendi global adları çağıranın aynı adlı değişkenlerinden ayrılmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
