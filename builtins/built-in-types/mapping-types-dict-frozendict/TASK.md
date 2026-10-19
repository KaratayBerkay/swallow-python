# Görev b:2.12: Anahtarları ve canlı sözlük görünümlerini izle

## Önce

[b:2](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Bir sözlüğün anahtarlarını ve ondan alınan görünümleri aynı çalışma içinde incele. Her adımın sonucunu çalıştırmadan önce çıkar, sonra doğrula.

1. `list({"b":2,"a":1})` ve `{[1]:2}` denemelerini ayrı yap. Kaynaktaki `1`, `1.0`, `True` eşitliğinin aynı anahtarı nasıl etkilediğini açıkla.
2. `d={"Ada":7,"Ece":9}` kur; keys, values ve items görünümlerini sakla. Uzunluklarını, sıralı dolaşımlarını, ters dolaşımlarını ve üyelik testlerini karşılaştır. Ardından `d["Can"]=5` ve `del d["Ada"]` uygula; saklanan görünümlerde neyin değiştiğini göster.
3. Güncel keys görünümü ile `["Can","Deniz"]` arasında kesişim yap. Güncel items görünümünü `{("Ece",9)}` ile kesiştir. Values görünümüne aynı küme işlemini uygulamayı ayrı dene. `{"Ada":[7]}.items()` görünümünü `[]` ile birleştirmeyi de dene; değerlerin hashable olmasının neden önemli olduğunu açıkla.
4. Saklanan values görünümünün `mapping` alanını `proxy` adına bağla. Proxy üzerinden atama denemesini, asıl d üzerinde Ece değerini 10 yapmayla karşılaştır. Son olarak canlı görünüm üzerinde dolaşırken anahtar ekleme veya silmenin kaynakta neden güvenilir sayılmadığını yazılı açıkla; her değişikliğin mutlaka aynı hatayı vereceğini varsayma.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `['b', 'a']`; `TypeError`.
- [ ] Eşit sayısal anahtarlar tek girdiyi paylaşır; görünümler doğru sırayı, üyelik anlamını ve değişiklik sonrası Ece/Can girdilerini gösterir. Items görünümünde üye `(anahtar, değer)` çiftidir.
- [ ] Keys kesişimi `{"Can"}`, items kesişimi `{("Ece",9)}` olur. Görünüm operatörleri uygun iterable kabul eder; values küme benzeri değildir, hashlenemeyen item değeri de küme sonucuna konamaz. Son iki geçersiz deneme TypeError verir.
- [ ] Proxy üzerinden yazma TypeError verir; d üzerinden değişiklik proxyye yansır. Salt okunur proxy, bağımsız veya dondurulmuş bir snapshot sayılmamış.
- [ ] Görünüm üzerinde dolaşırken anahtar ekleme/silme hata veya eksik dolaşım üretebilir; güvenli bir tam dolaşım garantisi verilmemiş.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
