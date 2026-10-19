## 4.1. `if` Statements

Perhaps the most well-known statement type is the `if` statement. For example:

``` python
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x < 0:
...     x = 0
...     print('Negative changed to zero')
... elif x == 0:
...     print('Zero')
... elif x == 1:
...     print('Single')
... else:
...     print('More')
...
More
```
> Code: [x.py](x.py)

There can be zero or more `elif` parts, and the `else` part is optional. The keyword '`elif`' is short for 'else if', and is useful to avoid excessive indentation. An `if` ... `elif` ... `elif` ... sequence is a substitute for the `switch` or `case` statements found in other languages.

If you're comparing the same value to several constants, or checking for specific types or attributes, you may also find the `match` statement useful. For more details see match Statements.

<!-- learning-task:start -->
### Bölüm görevi

**Görev 4.1: Tek bir koşul dalı seç**

**Odak:** if/elif/else, ilk doğru dal, karşılaştırma ve kullanıcı girdisinin int dönüşümü.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:3.2](../../03-an-informal-introduction-to-python/3.2-first-steps-towards-programming/README.md).

#### Tek görev

1. Bir sayı alan program yaz: negatifse "negative", sıfırsa "zero", 1 ise "single", diğer durumlarda "many" yazsın. -2, 0, 1 ve 4 girdilerini dene.

2. Ardından ilk koşulu x <= 0 yapınca 0 için hangi dalın çalıştığını açıklayıp ilk haline dön.

#### Geçiş ölçütleri

- [ ] Dört giriş sırasıyla negative, zero, single, many üretiyor.
- [ ] Her girişte yalnızca bir dal çalışıyor; <= değişikliği sonrası zero dalının neden seçilmediği açıklanmış.
- [ ] else ve elif bulunmasının hangi durumlarda gerekli olduğu kendi akışın üzerinden açıklanmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../4.2-for-statements/README.md)
<!-- learning-task:end -->
