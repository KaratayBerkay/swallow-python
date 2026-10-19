# Görev b:2.4: numeric-types-int-float-complex davranışını ayırt et

## Önce

[b:2](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; bölme, taban bölmesi, kalan ve complex parçasını ayır

```python
-7//2
-7%2
(2+3j).imag
```

Aynı işlem tablosuna `-7 / 2`, `-7 // 2`, `-7 % 2`, `5 & 3`, `5 | 2`, `5 ^ 3`, `~5`, `5 << 1`, `5 >> 1` ve negatif kaydırma sayısını ekle. Tam sayı ile float ortak işleminin türünü ve complex sıralama sınırını göster.

Kaynaktaki sayısal hash sözleşmesi için `1`, `1.0`, `1+0j` değerlerini dict anahtarı olarak birlikte kullan; eşit değerlerin hash ilişkisini göster. `hash(-1)` istisnasını ve verilmiş hash_fraction kodundaki paydanın modulus ile bölünebildiği dalı, kaynakta verilen kuralla yazılı izle; algoritmayı sıfırdan yeniden yazma.

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `-4`; `1`; `3.0`.
- [ ] Bölme, taban bölmesi, kalan ve complex parçasını ayır
- [ ] Bit işlemleri ve işaretli kaydırmalar gerekçelendirilmiş; negatif kaydırma ValueError, complex sıralama TypeError verir.

- [ ] Eşit sayısal değerler aynı anahtarı temsil eder; hash(-1) -2 olur; hash eşitliği ters yönde eşitlik kanıtı sayılmaz.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
