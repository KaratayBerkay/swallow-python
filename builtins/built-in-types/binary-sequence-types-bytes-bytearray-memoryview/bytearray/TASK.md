# Görev b:2.10.2: bytearray davranışını ayırt et

## Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

Sürüm: Python 3.15 veya üzeri. Daha eski yorumlayıcıda yalnız bu sürüme bağlı kısmı gerekçeli yazılı iz ile çözebilirsin; çalıştırma kanıtını bekleyen olarak kaydet.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; bytearray uzunluk, değer ve dönüştürme sözleşmelerini ayır

```python
bytearray([65,66])
bytes(bytearray(b"AB"))
bytearray([256])
```

Fromhex ve hex ile veriyi gidiş dönüş dönüştür. Python 3.14+ resize ile küçültmeyi ve sıfır baytlarla büyütmeyi göster. Python 3.15+ take_bytes için b"ABCD" üzerinde 2, -1, None ve sınır dışı n girdilerini yeni nesnelerde dene; dönüş bytes ile kalan bytearrayı kaydet.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `bytearray(b'AB')`; `b'AB'`; `ValueError`.
- [ ] Bytearray uzunluk, değer ve dönüştürme sözleşmelerini ayır
- [ ] Resize küçültmede sonu keser, büyütmede sıfır ekler; take_bytes(2) b"AB" alıp b"CD" bırakır, -1 ilk üç baytı alır, None hepsini alıp boşaltır; sınır dışı IndexError verir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
