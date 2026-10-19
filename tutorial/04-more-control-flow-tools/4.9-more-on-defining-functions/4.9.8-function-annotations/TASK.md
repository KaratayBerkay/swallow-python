# Görev 4.9.8: Tür açıklamasını çalışma zamanı denetiminden ayır

**Odak:** Parametre ve dönüş annotation sözdizimi, varsayılan ve `__annotations__` metaverisi.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:4.9.7](../4.9.7-documentation-strings/README.md).

## Tek görev

1. left: str ve right: str = "!" parametreleriyle iki değeri + kullanarak döndüren, dönüşü str olarak açıklanmış combine yaz. `__annotations__` içeriğini incele; combine("Hi") ve combine(2, 3) çağrılarını dene.

2. Sonuç ile açıklanan tür uyuşmadığında yorumlayıcının ne yaptığını anlat.

## Geçiş ölçütleri

- [ ] İlk sonuç Hi!, ikinci sonuç 5; annotation kendiliğinden tür hatası üretmiyor.
- [ ] Parametreler : ile, dönüş -> ile açıklanmış; varsayılan doğru yerde.
- [ ] `__annotations__` içinde left, right, return adları mevcut; anahtar sırası veya repr adresi ezberlenmemiş.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
