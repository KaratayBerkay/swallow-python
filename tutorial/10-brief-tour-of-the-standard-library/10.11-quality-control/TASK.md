# Görev 10.11: Davranış bozulunca testin yakaladığını göster

**Odak:** doctest ve unittest, normal sonuç, istisna ve başarısız testin tanı değeri.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:10.10](../10.10-performance-measurement/README.md).
- Ön bilgi: [t:9.5](../../09-classes/9.5-inheritance/README.md).

## Tek görev

1. README içindeki average işlevi için [2, 4] sonucunu gösteren docstring testi yazıp doctest.testmod ile çalıştır.

2. Ayrı test dosyasında unittest ile aynı normal sonucu ve boş listede ZeroDivisionError beklentisini sınat.

3. Sonra average kopyasının paydasına yanlışlıkla +1 ekleyerek hem doctest hem unittestin bunu yakaladığını göster; doğru sürüme geri dön.

## Geçiş ölçütleri

- [ ] Doğru sürümde doctest ve unittest geçiyor.
- [ ] Bozuk sürümde normal sonuç testleri gerçekten başarısız oluyor; yalnız çalıştırılmış olmaları başarı sayılmamış.
- [ ] Boş liste davranışı assertRaises ile kontrol edilmiş.
- [ ] Beklenen sonuç koddan kopyalanmadan bağımsız hesaplanmış; son sürüm tekrar geçiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
