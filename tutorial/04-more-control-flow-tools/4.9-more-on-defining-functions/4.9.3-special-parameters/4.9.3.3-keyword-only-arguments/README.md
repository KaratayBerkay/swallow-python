#### 4.9.3.3. Keyword-Only Arguments

To mark parameters as *keyword-only*, indicating the parameters must be passed by keyword argument, place an `*` in the arguments list just before the first *keyword-only* parameter.

<!-- learning-task:start -->
##### Bölüm görevi

**Görev 4.9.3.3: Anlamlı seçeneği anahtarla zorunlu kıl**

**Odak:** * sonrasındaki parametrenin yalnız anahtarla verilmesi.

###### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:4.9.3.2](../4.9.3.2-positional-only-parameters/README.md).

###### Tek görev

1. def label(name, *, color) gövdesinden name + ":" + color döndür. label("box", color="red"), label(name="box", color="red") ve label("box", "red") çağrılarını karşılaştır.

###### Geçiş ölçütleri

- [ ] İlk iki çağrı box:red döndürüyor; üçüncü çağrı kabul edilmiyor.
- [ ] * işaretinin name parametresini konumsal olmaya zorlamadığı açıklanmış.
- [ ] color değerinin neden açık isimle verilmesi gerektiği imzadan gösterilmiş.

[Değerlendirme yöntemi](../../../../../DEGERLENDIRME.md) · [Sıra](../../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../4.9.3.4-function-examples/README.md)
<!-- learning-task:end -->
