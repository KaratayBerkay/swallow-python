# Görev 15: Gösterimi gerçek sayı değeriyle karıştırma

**Odak:** Binary yaklaşım, gösterim yuvarlaması, isclose, tam geri kurma ve toplama hassasiyeti.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:11.8](../11-brief-tour-of-the-standard-library-part-ii/11.8-decimal-floating-point-arithmetic/README.md).
- Ön bilgi: [t:9.10](../09-classes/9.10-generator-expressions/README.md).

**Kaynak/ortam notu:** Kaynak yeni Python sürümündeki sum iyileştirmelerini anlatıyor. Python 3.11 üzerinde sum([0.1] * 10) == 1.0 yanlış çıkabilir; sonucu sürümüyle değerlendir.

## Tek görev

1. Tek bir sayı inceleme notu hazırla. 0.1 + 0.1 + 0.1 ile 0.3 için ==, math.isclose ve format(..., ".2f") sonuçlarını karşılaştır; round ile her girdiyi önceden yuvarlamanın neden aynı sorunu çözmediğini dene. x=0.1 için as_integer_ratio ve hex/fromhex ile değeri geri kur.

2. Ardından on adet 0.1 için açık toplama, sum ve math.fsum sonuçlarını mevcut Python sürümüyle birlikte kaydet.

3. README içindeki büyük değerlerin birbirini götürdüğü arr örneğini, gerekli math/Fraction importlarını ekleyerek aynı ölçütle incele.

## Geçiş ölçütleri

- [ ] Doğrudan eşitlik yanlış, isclose doğru; aynı görünen iki biçimlenmiş metnin altında farklı değerler bulunabiliyor.
- [ ] Ön yuvarlama temsil sorununu ortadan kaldırmıyor.
- [ ] Kesirden ve hex metninden geri kurulan float, ilk float ile tam eşit; gerçek 1/10 ile eşit olduğu iddia edilmemiş.
- [ ] sum davranışının 3.11 ve 3.12+ arasında farklılaşabileceği belirtilmiş; math.fsum ile açık toplama ayrılmış.
- [ ] arr için hangi yöntemin kayıp basamakları daha iyi koruduğu gözlemle açıklanmış; sürüme bağlı son basamaklar ezber ölçütü yapılmamış.
- [ ] Decimal metin girdisi ile Fraction tam kesir amaçları, gösterim biçimlemeyle karıştırılmamış.

[Değerlendirme yöntemi](../../DEGERLENDIRME.md) · [Sıra](../../TASKS.md)
