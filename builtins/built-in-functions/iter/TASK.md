# Görev b:3.40: iter sözleşmesini uygula

## Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

`it=iter([4,6])` için `iter(it) is it` kontrolünü ve tüketim sırasını göster. Ayrı olarak 4,6,"SON",8 döndüren hazır çağrılabilir bir fonksiyon verildiğini varsay; `iter(f,"SON")` hangi öğeleri verir?

## Geçiş ölçütleri

- [ ] İlk iterator kendisini döndürür; 4 ve 6 sonrasında tükenir.
- [ ] İki argümanlı biçim 4 ve 6 verir, sentinel öğesini vermez; sonraki 8 için f çağrılmaz.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
