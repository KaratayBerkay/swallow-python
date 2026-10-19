# Görev b:6.3: Maliyeti işlemden türet

## Önce

[b:6](../README.md) ve bu sayfanın açıklama/örnekleri.

Bu görevde verilen durumların yazılı çözümü geçerlidir; ek çalışma ortamı veya harici araç kurulumu gerekmez.

## Tek görev

N anahtarlı sözlükte get, len, copy ve k çiftle update maliyetlerini yaz. Bütün hashler çakışıyorsa get varsayımını değiştir; çoğu üye silinmiş büyük iç tabloyu ve frozendict.copy istisnasını değerlendir. Süre ölçümünü geçiş kanıtı olarak kullanma; tablo ve dipnotla gerekçelendir.

## Geçiş ölçütleri

- [ ] Get ortalama O(1), çakışmada O(N); len O(1), dict copy O(N), update ortalama amortized O(k).
- [ ] Hash/eşitlik O(1) varsayımı belirtilir; eski tablo kapasitesi tarama/kopya maliyetini etkileyebilir; frozendict copy O(1).

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
