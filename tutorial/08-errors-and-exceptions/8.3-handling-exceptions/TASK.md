# Görev 8.3: Yalnız beklediğin hatayı yakala

**Odak:** try/except/else, ilk eşleşen handler, hata argümanları ve alt çağrıdan yayılma.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:8.2](../8.2-exceptions/README.md).
- Ön bilgi: [t:7.2.1](../../07-input-and-output/7.2-reading-and-writing-files/7.2.1-methods-of-file-objects/README.md).

**Kaynak/ortam notu:** Kaynakta except RuntimeError, TypeError, NameError: biçimi var; 3.11 ile gerekiyorsa except (RuntimeError, TypeError, NameError): kullan. Bu bir handler parçasıdır, tek başına çalışacak dosya değildir.

## Tek görev

1. Bir metni int değerine çeviren parse(text) ve onu try/except ValueError/else ile kullanan küçük program yaz. "7", "bad", "0" için başarılı değer ve hata yolunu ayır; başarı mesajı yalnız else içinde olsun.

2. Ayrı denemede parse içinde 1 / 0 üretip ValueError handlerının bunu yakalamadığını göster.

3. README içindeki B/C/D sınıflarını hazır iskelet olarak okuyup handler sırası ters çevrildiğinde sonuçları çıkar; Exception("a", "b") örneğinde args içeriğini açıkla.

## Geçiş ölçütleri

- [ ] Geçerli girdiler başarı yoluna, bad ValueError yoluna gidiyor.
- [ ] Hata olan try satırından sonraki korunan satırlar atlanıyor; alt fonksiyondan gelen hata yakalanabiliyor.
- [ ] ZeroDivisionError ValueError handlerıyla yutulmamış.
- [ ] B/C/D için en özelden sıralama ile tabanın önce olması farklı sonuç veriyor.
- [ ] Exception args iki öğeli tuple; Exception ile BaseException kapsamı ve KeyboardInterrupt ayrımı belirtilmiş.
- [ ] else içindeki hatanın aynı try handlerları tarafından yakalanmayacağı açıklanmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
