## `bytes.capitalize`

```
bytes.capitalize()
bytearray.capitalize()
```

Return a copy of the sequence with each byte interpreted as an ASCII
character, and the first byte capitalized and the rest lowercased.
Non-ASCII byte values are passed through unchanged.

> **Note**
>
> The bytearray version of this method does *not* operate in place - it
> always produces a new object, even if no changes were made.

## Çözümlü kısa örnek

ASCII bayt kurallarıyla çalış; yalnız ilk karakter büyür; kalan bölüm küçülür

```python
print(repr(b'ada'.capitalize()))
# Sonuç: b'Ada'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.52: bytes.capitalize davranışını ayırt et**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; ASCII bayt kurallarıyla çalış; yalnız ilk karakter büyür; kalan bölüm küçülür

```python
b'pYTHON 3'.capitalize()
b''.capitalize()
```

Geçerli bir denemeyi eşdeğer bytearray ile tekrarla; sonuç türünü ve özgün bytearrayın korunup korunmadığını göster.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b'Python 3'`; `b''`.
- [ ] ASCII bayt kurallarıyla çalış; yalnız ilk karakter büyür; kalan bölüm küçülür
- [ ] Bytearray karşılığı doğru sonuç türüyle gösterilmiş; yeni binary dizi döndüren yöntem yerinde mutasyon sayılmamıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytes.expandtabs/README.md)
<!-- learning-task:end -->
