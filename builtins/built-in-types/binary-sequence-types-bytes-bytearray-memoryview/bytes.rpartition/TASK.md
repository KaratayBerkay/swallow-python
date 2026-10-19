# Görev b:2.10.30: bytes.rpartition davranışını ayırt et

## Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; sağdaki ayırıcı seçilir; bulunamazsa özgün metin son parçadır

```python
b'a=b=c'.rpartition(b'=')
b'abc'.rpartition(b'=')
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `(b'a=b', b'=', b'c')`; `(b'', b'', b'abc')`.
- [ ] ASCII bayt kurallarıyla çalış; sağdaki ayırıcı seçilir; bulunamazsa özgün metin son parçadır
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
