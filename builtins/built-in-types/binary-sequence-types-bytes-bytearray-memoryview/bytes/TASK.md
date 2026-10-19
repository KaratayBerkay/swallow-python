# Görev b:2.10.1: bytes davranışını ayırt et

## Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII literal, hex dönüşüm ve değişmezliği bağla

```python
bytes.fromhex("41 42")
b"AB".hex()
b"AB"=="AB"
```

Fromhex ile boşluk içeren hex metni ve hatalı tek hex basamağını dene. Hex için ayırıcı ve bytes_per_sep seçeneğini kullan. Binary `%` biçimlendirmede ASCII sayıyla %b girdisini göster; Unicode metni doğrudan binary alana vermenin sınırını açıkla.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b'AB'`; `'4142'`; `False`.
- [ ] ASCII literal, hex dönüşüm ve değişmezliği bağla
- [ ] Hatalı hex ValueError; biçimlendirme sonucu bytes; bytes ile str kendiliğinden birbirine dönüşmez.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
