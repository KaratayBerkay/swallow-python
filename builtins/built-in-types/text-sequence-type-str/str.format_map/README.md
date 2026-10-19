## `str.format_map`

```
str.format_map(mapping, /)
```

Similar to `str.format(**mapping)`, except that `mapping` is
used directly and not copied to a [dict](../../mapping-types-dict-frozendict/dict/README.md).  This is useful
if for example `mapping` is a dict subclass:

``` python
>>> class Default(dict):
...     def __missing__(self, key):
...         return key
...
>>> '{name} was born in {country}'.format_map(Default(name='Guido'))
'Guido was born in country'
```
> Code: [example_01.py](example_01.py)

> *Added in version 3.2.*

## Çözümlü kısa örnek

Alanlar verilen mapping üzerinden çözülür

```python
print(repr("{ad}".format_map({"ad":"Ada"})))
# Sonuç: 'Ada'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.12: str.format_map davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; alanlar verilen mapping üzerinden çözülür

```python
"{ad}:{puan}".format_map({"ad":"Ece","puan":8})
"{eksik}".format_map({})
```

Kaynak örnekteki `Default(dict)` sınıfını kullan: `__missing__` bulunmayan alanın adını döndürüyor. `"{ad}:{sehir}".format_map(Default(ad="Ece"))` sonucunu çıkar. Aynı nesneyi önce `dict(...)` ile kopyalayınca eksik alan davranışını karşılaştır.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `'Ece:8'`; `KeyError`.
- [ ] Alanlar verilen mapping üzerinden çözülür

- [ ] Doğrudan mapping kullanımında "Ece:sehir" elde edilir; normal dict kopyasında eksik alan KeyError verir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.index/README.md)
<!-- learning-task:end -->
