# Görev 11.1: Görünümü verinin kendisinden ayır

**Odak:** reprlib kısaltma, pprint yerleşimi, textwrap ve locale bağımlı sunum.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:10.12](../../10-brief-tour-of-the-standard-library/10.12-batteries-included/README.md).
- Ön bilgi: [t:7.1.3](../../07-input-and-output/7.1-fancier-output-formatting/7.1.3-manual-string-formatting/README.md).

## Tek görev

1. data = [list(range(8)), list(range(8, 16))] verisini önce repr, sonra reprlib.repr ve pprint.pprint(width=30) ile göster. Kısaltılan öğelerle yalnız satırı değişen öğeleri karşılaştır.

2. "Python makes small data flows easier to inspect and explain." paragrafını textwrap.fill(width=25) ile biçimle. Gösterimlerden sonra data içindeki iki listenin bütün değerlerini ve paragrafın asıl metnini kontrol et.

3. README içindeki locale örneğini çalıştırmak yerine sayı gruplama, para simgesi ve basamak sayısının hangi yerel ayar verilerinden geldiğini yazılı izle.

## Geçiş ölçütleri

- [ ] reprlib gösterimi ... ile kısalıyor; pprint çok satırlı ve girintili gösterimde 0..15 değerlerinin tamamını koruyor.
- [ ] İki kaynak liste hâlâ sekizer öğeli; kısaltma veya satır düzeni veriyi değiştirmemiş.
- [ ] Paragraf satırları en fazla 25 karakter; sözcük sırası ve asıl paragraf metni korunmuş.
- [ ] locale gruplama, currency_symbol ve frac_digits rolleri ayrılmış.
- [ ] Örnekteki Windows locale adının her sistemde bulunacağı varsayılmamış; ortam ayarı değiştirme gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
