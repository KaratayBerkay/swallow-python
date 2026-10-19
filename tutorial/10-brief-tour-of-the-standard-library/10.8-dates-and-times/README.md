## 10.8. Dates and times

The `datetime` module supplies classes for manipulating dates and times in both simple and complex ways. While date and time arithmetic is supported, the focus of the implementation is on efficient member extraction for output formatting and manipulation. The module also supports objects that are timezone aware.

``` python
>>> # dates are easily constructed and formatted
>>> import datetime as dt
>>> now = dt.date.today()
>>> now
datetime.date(2003, 12, 2)
>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

>>> # dates support calendar arithmetic
>>> birthday = dt.date(1964, 7, 31)
>>> age = now - birthday
>>> age.days
14368
```
> Code: [now.py](now.py)

<!-- learning-task:start -->
### Bölüm görevi

**Görev 10.8: Tarih farkını sabit girdilerle doğrula**

**Odak:** date oluşturma, today, strftime ve çıkarma sonucunun days niteliği.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:10.7](../10.7-internet-access/README.md).

#### Tek görev

1. dt.date ile 2024-02-28 ve 2024-03-01 tarihlerini oluştur; farkın days değerini bul.

2. Son tarihi "%m-%d-%y" ve "%d %b %Y" biçimlerinde göster. today() çağrısını ayrı yapıp neden bugünün tarihine sabit bir beklenen değer yazılamayacağını açıkla.

#### Geçiş ölçütleri

- [ ] Fark 2 gün; artık gün tarih aritmetiğiyle hesaba katılmış.
- [ ] Sayısal görünüm 03-01-24; ikinci görünüm aynı tarihi ifade ediyor.
- [ ] %b yerel ayara göre farklı metin üretebilir; sistem locale ayarı değiştirilmemiş.
- [ ] Çıkarma sonucu ile biçimlenen str birbirinden ayrılmış; timezone API tasarımı gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../10.9-data-compression/README.md)
<!-- learning-task:end -->
