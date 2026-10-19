# Görev 5.4: İki grubun ortak ve farklı üyelerini bul

**Odak:** Tekrarsız ve sırasız set, üyelik, fark/birleşim/kesişim/simetrik fark ve comprehension.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:5.3](../5.3-tuples-and-sequences/README.md).
- Ön bilgi: [t:5.1.5](../5.1-more-on-lists/5.1.5-unpacking-in-lists-and-list-comprehensions/README.md).

**Kaynak/ortam notu:** Son unpacking comprehension Python 3.15 gerektirir; diğer işlemler Python 3.11 ile uygulanabilir. Son kısım eski yorumlayıcıda yazılı iz sürmedir.

## Tek görev

1. a = set("banana"), b = set("band") için ortak, yalnız a içinde, iki gruptan herhangi birinde ve yalnız birinde olan harfleri hesapla. a içinden n harfini dışlayan set comprehension yaz.

2. Boş set ile {} farkını belirt.

3. Son olarak [{"a", "b"}, {"b", "c"}] için bölümde gösterilen unpacking comprehension sonucunu yazılı olarak çıkar.

## Geçiş ölçütleri

- [ ] Kesişim {a, b, n}; a-b boş; birleşim {a, b, n, d}; simetrik fark {d}, öğe sırası önemsenmemiş.
- [ ] Filtre sonucu {a, b}; n üyeliği ile d üyeliği doğru.
- [ ] Boş set set() ile kurulmuş, {} sözlük olarak ayrılmış.
- [ ] Açılan gruplar tekrarsız {a, b, c} üretir; metin sırası üzerinden set sırası çıkarılmamış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
