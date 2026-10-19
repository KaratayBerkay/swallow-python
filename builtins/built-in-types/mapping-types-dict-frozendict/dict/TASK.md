# Görev b:2.12.2: Canlı kayıt haritasını yönet

## Önce

[b:2.12](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Bir kayıt haritasını aynı çalışma içinde aşağıdaki akışla yönet. Her adımda dönen değerleri, anahtar sırasını ve saklanan eski nesnelerin gördüğü durumu kaydet.

1. `d={"a":[1],"b":[2]}` kur; keys/items/values görünümleri ve shallow copy sakla. a iç listesini yerinde değiştir.
2. Eksik c anahtarını get ile oku, setdefault ile ekle. Update ile b değerini değiştir; `|` ile yeni sözlük üret, `|=` ile d güncelle. İki birleşimde sağ tarafın önceliğini göster.
3. c anahtarı için pop, son eklenen öğe için popitem uygula. Boş sözlükte popitem ve eksik anahtarda defaultsuz pop hatalarını yakala. `d.values()` ile yeniden oluşturulan başka bir values görünümünün eşitliğini de dene.
4. Ayrı sözlükte fromkeys ile iki anahtara aynı boş liste ver; birini değiştir. Sonra comprehension ile bağımsız listeler oluşturarak farkı kanıtla.

## Geçiş ölçütleri

- [ ] Görünümler canlıdır; copy yeni dış sözlüktür ama a iç listesi paylaşılır; values görünümleri için içerik eşitliği varsayılmamıştır.
- [ ] Get eksik anahtarı eklemez, setdefault ekler; update None döndürür; sağ taraf çakışmada kazanır.
- [ ] Yeni | sonucu d ile aynı nesne değildir; |= d üzerinde çalışır; yeniden atama mevcut anahtar sırasını değiştirmez.
- [ ] Pop değer, popitem son eklenen (key,value) çifti döndürür; boş ve eksik durumlar KeyError verir.
- [ ] Fromkeys iki anahtarda aynı listeyi paylaşır; bağımsız listeler için comprehension kullanılır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
