## 10.10. Performance measurement

Some Python users develop a deep interest in knowing the relative performance of different approaches to the same problem. Python provides a measurement tool that answers those questions immediately.

For example, it may be tempting to use the tuple packing and unpacking feature instead of the traditional approach to swapping arguments. The `timeit` module quickly demonstrates a modest performance advantage:

``` python
>>> from timeit import Timer
>>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
0.57535828626024577
>>> Timer('a,b = b,a', 'a=1; b=2').timeit()
0.54962537085770791
```
> Code: [timer.py](timer.py)

In contrast to `timeit`'s fine level of granularity, the `profile` and `pstats` modules provide tools for identifying time critical sections in larger blocks of code.

<!-- learning-task:start -->
### Bölüm görevi

**Görev 10.10: Hızı ölçerken sonucu garanti etme**

**Odak:** Timer kurulum/ölçüm ayrımı, aynı işin iki uygulaması ve ölçüm yorumu.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:10.9](../10.9-data-compression/README.md).

#### Tek görev

1. İki değişkeni geçici değişkenle ve tuple atamasıyla yer değiştiren iki kısa kodu önce normal çalıştırarak aynı davranışı verdiklerini göster.

2. Sonra bölümdeki Timer iskeletinde aynı başlangıç değerleriyle iki yaklaşımı ölç.

3. Çıkan süreleri kaydet; hangisinin hızlı çıkacağını başarı şartı yapmadan ölçümün ne anlattığını açıkla.

#### Geçiş ölçütleri

- [ ] İki kod parçası aynı başlangıçta aynı değişimi yapıyor.
- [ ] Başlangıç hazırlığı setup, ölçülen iş statement alanında.
- [ ] Süreler makineye/oturuma bağlı gözlem olarak raporlanmış; örnekteki sayılar beklenmemiş.
- [ ] timeit küçük parça, profile/pstats daha büyük kodda zaman harcayan yerleri bulma amacıyla ayrılmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../10.11-quality-control/README.md)
<!-- learning-task:end -->
