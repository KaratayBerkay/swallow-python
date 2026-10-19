# Görev b:2.7.11: sequence.index davranışını ayırt et

## Önce

[b:2.7](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; i̇lk eşleşmenin özgün indeksini, arama sınırını ve yokluk hatasını ayır

```python
[1,2,1].index(1,1)
[1,2].index(9)
```

Aynı değeri aramayı tuple ve range üzerinde de dene. Index için başlangıç/bitiş argümanlarının bütün sequence türlerinde desteklendiğini varsayma; desteklenmeyen çağrıyı kaynak notuyla ilişkilendir.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `2`; `ValueError`.
- [ ] İlk eşleşmenin özgün indeksini, arama sınırını ve yokluk hatasını ayır

- [ ] List/tuple/range üzerindeki ortak sonuç sözleşmesi ile isteğe bağlı parametre desteği ayrı incelenmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
