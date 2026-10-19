# Görev b:2.9: text-sequence-type-str davranışını ayırt et

## Önce

[b:2](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; unicode karakteriyle bayt dizisi aynı nesne değildir

```python
len("İ")
"a" "b"
"ab"[0:9]
```

Aynı çalışmaya `%` biçimlendirmeyle ad ve puan yerleştirmeyi, `%%` ile literal yüzdeyi, yanlış sayıda alan verilmesi hatasını ekle. Metin içine yerleştirmeyle özgün Unicode metni değiştirmeyi ayır.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `1`; `'ab'`; `'ab'`.
- [ ] Unicode karakteriyle bayt dizisi aynı nesne değildir
- [ ] Biçimlendirme yeni str verir; literal yüzde kaçışı ve argüman sayısı uyuşmazlığı açıklanır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
