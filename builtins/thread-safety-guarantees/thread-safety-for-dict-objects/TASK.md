# Görev b:5.3: Eşzamanlılık iddiasını durum akışıyla sınayalım

## Önce

[b:5](../README.md) ve bu sayfanın açıklama/örnekleri.

Bu görevde verilen durumların yazılı çözümü geçerlidir; ek çalışma ortamı veya harici araç kurulumu gerekmez.

## Tek görev

d["n"]=0 için A ve B aynı 0 değerini okuyup sonra birer kez +1 sonucunu yazıyor. Son değeri çöz. Get/üyelik/len, tek yazma, copy, update(dict), update(özel iterable) ve kullanıcı __eq__ çağrılarının kilit sınırlarını karşılaştır. Gerçek thread yarışı üretmek yerine verilen sıralamayı yazılı çöz; her garanti için bu sayfadaki koşulu belirt.

## Geçiş ölçütleri

- [ ] Son değer 1 olabilir; iki artışın 2 olacağı garantisi yoktur.
- [ ] Atomik okuma ile kilitli yazma ayrı garantilerdir; update girdisinin türü karşı tarafın kilitlenmesini değiştirir.
- [ ] Özel karşılaştırma Python kodu çalıştırabilir; view oluşturma viewün sonsuza dek snapshot olması demek değildir.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
