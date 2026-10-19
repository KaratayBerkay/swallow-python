# Görev 4.9.2: Çağrıdaki değerleri parametrelere bağla

**Odak:** Konumsal/anahtar kelimeli argüman, varsayılan, eksik/tekrar/bilinmeyen argüman ve `*arguments`/`**keywords`.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:4.9.1](../4.9.1-default-argument-values/README.md).

## Tek görev

1. def label(name, color="blue", size=1) imzasına print(name, color, size) gövdesi ver. name değeri "box", color değeri "red", size değeri 2 olacak üç farklı geçerli çağrı yaz.

2. Sonra eksik zorunlu argüman, tekrarlı name, bilinmeyen anahtar ve anahtardan sonra konumsal argüman içeren birer geçersiz çağrıyı ayrı girişlerde dene.

3. README içindeki cheeseshop iskeletine iki ek konumsal ve iki ek anahtarlı değer vererek hangi gruba gittiklerini izle.

## Geçiş ölçütleri

- [ ] Üç geçerli çağrı aynı değerleri doğru parametreye bağlıyor; anahtarların sırası sonucu değiştirmiyor.
- [ ] Geçersiz çağrıların her birinin hangi bağlama kuralını bozduğu açıklanmış.
- [ ] `*arguments` fazladan konumsalları, `**keywords` fazladan anahtarları topluyor.
- [ ] Anahtarlı eklerin yazdırılma sırası çağrıda verilme sırasıyla eşleşiyor.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
