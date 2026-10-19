# Görev 4.9.4: Değişken sayıda parçayı birleştir

**Odak:** `*args` ile kalan konumsalları toplama ve sonrasındaki yalnız anahtarlı parametre.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:4.9.3.5](../4.9.3-special-parameters/4.9.3.5-recap/README.md).

## Tek görev

1. Bölümdeki concat örneğinden yola çıkarak join_parts(prefix, `*parts`, sep="/") yaz. prefix ile başla; ardından parts öğelerini döngüyle, aralara sep koyarak ekle.

2. Sıfır, bir ve üç ek parça ile; hem varsayılan hem özel ayraçla çağır.

3. Sonuna konumsal verilen ":" değerinin neden sep değil bir parça olduğunu göster.

## Geçiş ölçütleri

- [ ] join_parts("root") root; join_parts("root", "a", "b") root/a/b.
- [ ] sep=":" ile root:a:b elde ediliyor.
- [ ] parts bir tuple içinde toplanıyor, prefix bu grubun dışında kalıyor.
- [ ] sep yalnız anahtarla değiştirilebiliyor; konumsal ":" parts içine gidiyor.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
