#### 4.9.3.5. Recap

The use case will determine which parameters to use in the function definition:

``` python
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
```
> Code: [f.py](f.py)

As guidance:

- Use positional-only if you want the name of the parameters to not be available to the user. This is useful when parameter names have no real meaning, if you want to enforce the order of the arguments when the function is called or if you need to take some positional parameters and arbitrary keywords.

- Use keyword-only when names have meaning and the function definition is more understandable by being explicit with names or you want to prevent users relying on the position of the argument being passed.

- For an API, use positional-only to prevent breaking API changes if the parameter's name is modified in the future.

<!-- learning-task:start -->
##### Bölüm görevi

**Görev 4.9.3.5: Çağrı sözleşmesine uygun imzayı seç**

**Odak:** Parametre türü seçiminin okunabilirlik ve ad değişikliği ile ilişkisi.

###### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:4.9.3.4](../4.9.3.4-function-examples/README.md).

###### Tek görev

1. Bir kayıt işlevi için şu sözleşmeyi yalnız imzayla ifade et: kayıt nesnesi yalnız konumla, etiket hem konumla hem anahtarla, görünürlük yalnız anahtarla verilecek.

2. Bir geçerli çağrı yaz.

3. Kayıt parametresinin adını değiştirmekle etiket parametresinin adını değiştirmenin mevcut çağrılara etkisini açıkla.

###### Geçiş ölçütleri

- [ ] / ilk parametreden, * etiket parametresinden sonra.
- [ ] Örnek çağrı sözleşmeye uyuyor.
- [ ] Konumsal parametre adının değişmesinin çağıranları etkilememesi; anahtar kullanılan parametre adının değişmesinin etkisi doğru açıklanmış.

[Değerlendirme yöntemi](../../../../../DEGERLENDIRME.md) · [Sıra](../../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
