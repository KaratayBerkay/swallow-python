## `PendingDeprecationWarning`

```
PendingDeprecationWarning
```

Base class for warnings about features which are obsolete and
expected to be deprecated in the future, but are not deprecated
at the moment.

This class is rarely used as emitting a warning about a possible
upcoming deprecation is unusual, and [DeprecationWarning](../DeprecationWarning/README.md)
is preferred for already active deprecations.

Ignored by the default warning filters. Enabling the `Python
Development Mode <devmode>` shows this warning.

The deprecation policy is described in [PEP 387](https://peps.python.org/pep-387/).

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.5.4: PendingDeprecationWarning kategorisini seç**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Verilen olay: Henüz deprecated olmamış ama ileride olması beklenen özellik. Kategori seçimini gerekçelendir; bunu doğrudan programı durduran hata ile karıştırma. Bu sayfada varsayılan görünürlük bilgisi varsa, uyarının görülmemesinin hiç üretilmediğini kanıtlayıp kanıtlamadığını açıkla.

#### Geçiş ölçütleri

- [ ] PendingDeprecationWarning uygun kategori olarak kaynakta tarif edilen hedef/kapsama bağlanmıştır.
- [ ] Yalnız burada belirtilen filtre bilgisi kullanılmıştır; belirtilmeyen varsayılan davranış ezberden uydurulmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../SyntaxWarning/README.md)
<!-- learning-task:end -->
