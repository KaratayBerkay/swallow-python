# Görev b:2.9.29: str.maketrans davranışını ayırt et

## Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

Sürüm: Python 3.15+ frozendict kabulü eski sürümde yalnız gerekçeli yazılı iz ile incelenebilir; temel dict/metin denemelerini çalıştır.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; tablo anahtarları ord olur; eşleştirme, silme ve uzunluk şartını ayır

```python
str.maketrans({"a":"XY","b":None})
str.maketrans("ab","x")
```

Üç argümanlı biçimde `str.maketrans("ab","xy","!")` oluştur; hangi anahtarların hangi değerlere bağlandığını göster. Python 3.15+ aynı tek argümanlı tabloyu frozendict ile oluşturma davranışını yazılı olarak incele.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `{97: 'XY', 98: None}`; `ValueError`.
- [ ] Tablo anahtarları ord olur; eşleştirme, silme ve uzunluk şartını ayır

- [ ] 97->120, 98->121, 33->None eşlemesi vardır; üç argümanlı biçim silme tablosu da üretir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
