# Görev b:2.10.74: bytes.splitlines davranışını ayırt et

## Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; sondaki satır sonu ek boş satır üretmez; keepends sonlandırıcıyı korur

```python
b'a\n'.splitlines()
b'a\n\nb'.splitlines(True)
b''.splitlines()
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `[b'a']`; `[b'a\n', b'\n', b'b']`; `[]`.
- [ ] ASCII bayt kurallarıyla çalış; sondaki satır sonu ek boş satır üretmez; keepends sonlandırıcıyı korur
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
