# Görev 7.1.2: Şablon alanlarını argümana bağla

**Odak:** Otomatik/numaralı/anahtarlı format alanları, sözlük erişimi, ** ve alan genişliği.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:7.1.1](../7.1.1-formatted-string-literals/README.md).
- Ön bilgi: [t:4.9.5](../../../04-more-control-flow-tools/4.9-more-on-defining-functions/4.9.5-unpacking-argument-lists/README.md).

## Tek görev

1. data = {"name": "Ada", "count": 7} için "Ada:   7" satırını format ile üç yoldan üret: konumsal numaralar, {0[name]} gibi sözlük alanı, `**data` ile anahtar alanları.

2. İlk yolda argümanları ters sırayla verip alan numaralarını düzelt.

3. Ayrıca iki küçük işaretçi değişken için vars() içinden adlara erişimin şablona veri sağlamasını bölümdeki örnek üzerinden açıkla.

## Geçiş ölçütleri

- [ ] Üç yol aynı metni ve genişliği üretiyor.
- [ ] Konum sırası değişince doğru değerler numarayla seçiliyor.
- [ ] Sözlük alanı erişimiyle ** açma aynı mekanizma sanılmamış.
- [ ] vars() sözlük sağlıyor; bütün ortam çıktısının sabit olması beklenmemiş.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
