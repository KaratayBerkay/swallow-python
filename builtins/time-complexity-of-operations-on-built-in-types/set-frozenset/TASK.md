# Görev b:6.4: Maliyeti işlemden türet

## Önce

[b:6](../README.md) ve bu sayfanın açıklama/örnekleri.

Bu görevde verilen durumların yazılı çözümü geçerlidir; ek çalışma ortamı veya harici araç kurulumu gerekmez.

## Tek görev

n ve m üyeli iki kümede union, intersection, difference, difference_update maliyetlerini karşılaştır. Diğer operand set yerine genel iterable olursa dipnotların etkisini ekle; frozenset kopyasını ayrı göster. Süre ölçümünü geçiş kanıtı olarak kullanma; tablo ve dipnotla gerekçelendir.

## Geçiş ölçütleri

- [ ] Union O(n+m), intersection O(min(n,m)), difference O(n), difference_update O(min(n,m)) olağan varsayımlarla verilir.
- [ ] Genel iterable ve hash çakışması koşulları sonucu değiştirir; frozenset copy O(1), mutable set copy O(n).

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
