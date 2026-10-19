### 7.1.4. Old string formatting

The % operator (modulo) can also be used for string formatting. Given `format % values` (where *format* is a string), `%` conversion specifications in *format* are replaced with zero or more elements of *values*. This operation is commonly known as string interpolation. For example:

``` python
>>> import math
>>> print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.
```
> Code: [math_example.py](math_example.py)

More information can be found in the printf-style String Formatting section.

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 7.1.4: Yüzde işaretinin iki rolünü ayır**

**Odak:** Eski % metin biçimlemesi ve sayısal kalan işlemi ayrımı.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:7.1.3](../7.1.3-manual-string-formatting/README.md).

##### Tek görev

1. value = 12.345 için bölümdeki %5.3f biçimini kullanarak fiyat mesajı üret; aynı değeri f-string ile üç ondalıklı gösterip karşılaştır.

2. Ayrı girişte 12 % 5 sonucunu al.

3. Sol taraftaki değerin bu iki kullanımın anlamını nasıl değiştirdiğini açıkla.

##### Geçiş ölçütleri

- [ ] Metin görünümü 12.345; f-string ile aynı hassasiyet.
- [ ] Sayısal kalan 2.
- [ ] % işaretinin sayılarda kalan, format metninde yerleştirme işlemi olduğu açıklanmış; yeni dönüşüm kodları gerekmiyor.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
