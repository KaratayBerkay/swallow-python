# Görev b:2.10.3: Paylaşılan tamponu izle

## Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

Sürüm: Python 3.14 veya üzeri. Daha eski yorumlayıcıda yalnız bu sürüme bağlı kısmı gerekçeli yazılı iz ile çözebilirsin; çalıştırma kanıtını bekleyen olarak kaydet.

## Tek görev

Aynı tampon üzerinde görünüm ve kopyanın yaşamını izle:

1. `data=bytearray(b"ABCD")`, `v=memoryview(data)`, `alt=v[1:3]` ve `salt=v.toreadonly()` kur. `alt` üzerinden bir bayt değiştir; data ve salt sonuçlarını göster.
2. Aynı boyutlu dilim atamasını, farklı boyutlu atamayı ve salt üzerinden yazmayı karşılaştır. `bytes(v)`, `tolist()` ve `hex()` sonuçlarını kaydet.
3. `v.cast("B",shape=[2,2])` ile yeni görünüm al; ndim/shape/strides/itemsize/nbytes/len ilişkisini göster. `obj` kimliğini, c_contiguous/f_contiguous ve suboffsets alanlarının veri değil görünüm metadatası oluşunu kaynakla ilişkilendir.
4. Bütün alt görünümleri bırakmadan data boyutunu değiştirmeyi dene, sonra hepsini release et. Bırakılmış görünüm erişimini, tekrar release çağrısını ve with ile bırakmayı karşılaştır. Hashable bytes görünümü ile writable bytearray görünümünün hash sınırını göster; eşitlikte ham baytların yanında format/shape yorumunun da önemini açıkla.
5. Python 3.14+ count/index için bulunan ve bulunmayan öğeyi ekle. Python 3.12+ sıfır boyutlu görünümde len sınırını yazılı açıkla.

## Geçiş ölçütleri

- [ ] Alt görünüm aynı tamponu paylaşır; readonly görünüm başka ad üzerinden değişikliği görür, yazma denemesi TypeError verir.
- [ ] Farklı boyutlu görünüm ataması ValueError; dış bytearray yeniden boyutlandırılması canlı export varken BufferError verir.
- [ ] Nbytes bayt miktarıdır, len ilk boyut uzunluğudur; dönüştürme kopyası ile cast/slice görünümü ayrılmıştır.
- [ ] Release sonrası erişim ValueError; yeniden release geçerlidir; bütün exportlar bırakıldıktan sonra yeniden boyutlandırma geçerlidir.
- [ ] 3.14 count sayı, index ilk indeks veya ValueError verir; 3.12 sıfır boyutta len TypeError verir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
