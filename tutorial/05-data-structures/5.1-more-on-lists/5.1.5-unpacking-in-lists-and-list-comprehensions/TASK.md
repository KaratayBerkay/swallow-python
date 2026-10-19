# Görev 5.1.5: Açılan öğeyi kapsayıcıdan ayır

**Odak:** Liste içinde * açma, comprehension ile bir seviye açma ve iterable gereksinimi.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:5.1.4](../5.1.4-nested-list-comprehensions/README.md).

**Kaynak/ortam notu:** Comprehension içindeki [`*part` for ...] Python 3.15 gerektirir. Daha eski yorumlayıcıda bu kısmı yazılı iz sürme olarak değerlendir; SyntaxError bilgi eksikliği değildir. [0, `*parts`, 9] eski sürümlerde de kullanılabilir.

## Tek görev

1. parts = [[2, 3], [], [4]] için [0, `*parts`, 9] ile [`*part` for part in parts] sonuçlarını önce yaz, sonra uygun sürümde dene.

2. İlk ifadenin kaç seviye açtığını göster. parts içindeki son öğeyi 4 sayısı yapınca hangi ifade neden çalışır veya hata verir?

3. Son olarak bölümün karışık iterable örneğinde sözlükten anahtarların çıkmasını açıkla.

## Geçiş ölçütleri

- [ ] İlk sonuç [0, [2, 3], [], [4], 9], ikinci sonuç [2, 3, 4].
- [ ] İlk ifade dış listedeki öğeleri, ikinci ifade her part içindeki öğeleri açıyor.
- [ ] Tekil sayı içeren sürümde comprehension iterable olmayan part yüzünden hata veriyor.
- [ ] Boş alt liste öğe eklemiyor; metin karakter, sözlük anahtar sağlıyor.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
