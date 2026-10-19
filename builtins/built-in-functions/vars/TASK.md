# Görev b:3.71: vars davranışını ayırt et

## Önce

[t:9.5](../../../tutorial/09-classes/9.5-inheritance/README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; nesnenin __dict__ eşlemesiyle nitelik erişimini bağla.

```python
class K: pass
o=K(); o.puan=4
vars(o) is o.__dict__
vars(3)
```

Sınıf nesnesinin `vars(K)` sonucuna anahtar atamayı örneğin `vars(o)` sonucuna atamayla karşılaştır; bu farkı kaynakta belirtilen salt okunur eşlemeye bağla.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `TypeError`.
- [ ] Nesnenin __dict__ eşlemesiyle nitelik erişimini bağla.

- [ ] Örneğin dict alanı güncellenebilir; sınıfın mappingproxy alanına doğrudan atama TypeError verir.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
