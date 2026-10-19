# Görev 4.9.7: Davranışı anlatan docstring yaz

**Odak:** Özet satırı, boş ayırıcı satır, çağrı koşulları ve `__doc__`.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:4.8](../../4.8-defining-functions/README.md).

## Tek görev

1. İki metni bir ayraçla birleştirip döndüren label(left, right, sep=":") fonksiyonuna çok satırlı İngilizce docstring yaz.

2. İlk satır kısa özet, devamı varsayılan ayraç ve dönüş davranışı olsun. print(`label.__doc__`) ile açıklamayı, label("a", "b") ile davranışı kontrol et.

3. Yorum satırı ile docstring yerini karşılaştır.

## Geçiş ölçütleri

- [ ] İlk satır büyük harfle başlayan ve noktayla biten kısa davranış özeti.
- [ ] İkinci satır boş; devamı parametre ve dönüşü anlatıyor.
- [ ] Docstring fonksiyonun ilk ifadesi ve `__doc__` ile erişilebilir.
- [ ] Açıklama gerçek a:b davranışıyla tutarlı; # yorumu docstring yerine sayılmamış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
