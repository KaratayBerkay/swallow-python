# Görev 4.7: Desen yönlendiricisinin karar tablosunu çıkar

**Odak:** İlk eşleşme, literal/OR/wildcard, yakalama, sequence/mapping/class desenleri, guard, as ve noktalı sabit.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:4.6](../4.6-pass-statements/README.md).
- Ön bilgi: [t:3.1.3](../../03-an-informal-introduction-to-python/3.1-using-python-as-a-calculator/3.1.3-lists/README.md).

## Tek görev

1. README içindeki yönlendirme örneklerini temel alarak tek bir karar tablosu hazırla.

2. Sütunlar: girdi, ilk seçilen case, bağlanan adlar, çıktı.

3. Durumlar: HTTP 401/403/999 için literal ve |; (0, 0), [0, 5], (3, 4), "ab" için koordinat desenleri; [1, 2, 3] için [x, y, `*rest`]; ek anahtarlı ve eksik anahtarlı sözlük için mapping deseni.

4. Sonra verilen Point sınıfını hazır iskelet olarak kullanarak origin, tek nokta, iki Y ekseni noktası ve eşit/eşit olmayan koordinat guard durumlarını tabloya ekle.

5. README içindeki as ve Color.RED örneklerinde hangi adların yakalandığını işaretle.

6. Yeni sınıf veya enum yazman gerekmiyor.

## Geçiş ölçütleri

- [ ] Tabloda yalnızca ilk uygun case seçiliyor; wildcard varsayılan, OR deseni alternatif olarak yorumlanmış.
- [ ] Liste ve tuple koordinatları eşleşiyor; metin sequence deseniyle eşleşmiyor; `*rest` kalan öğeleri alıyor.
- [ ] Mapping ek anahtarları kabul ediyor, gerekli anahtar yoksa eşleşmiyor; `**rest` ile `**_` ayrımı açıklanmış.
- [ ] Point desenlerinde x=/y= etiketleri ile yakalanan adlar ayrılmış; `__match_args__` sırası doğru okunmuş.
- [ ] Guard yakalamadan sonra sınanıyor; yanlışsa sonraki case deneniyor; as hem alt nesneyi hem alanlarını bağlayabiliyor.
- [ ] Color.RED noktalı sabit, bağımsız ad yakalama olarak ayrılmış; True/False/None karşılaştırmasının kimlik kuralı belirtilmiş.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
