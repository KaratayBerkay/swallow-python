# Görev 7.2.2: Yapılandırılmış veriyi dosyadan geri getir

**Odak:** JSON serialization/deserialization, dumps/dump/load ve metin/nesne ayrımı.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:7.2.1](../7.2.1-methods-of-file-objects/README.md).
- Ön bilgi: [t:5.5](../../../05-data-structures/5.5-dictionaries/README.md).

## Tek görev

1. data = {"name": "Ada", "scores": [2, 5], "active": True} verisini önce json.dumps ile metin olarak göster; sonra UTF-8 dosyaya json.dump ile yazıp yeni açılışta json.load ile geri al.

2. Geri gelen veriyle asıl veriyi karşılaştır; scores öğesinin yine liste olarak kullanılabildiğini göster.

3. Kaynaktaki pickle notunun dil bağımlılığı ve güven sınırını sözle açıkla.

## Geçiş ölçütleri

- [ ] dumps sonucu metin; load sonucu yine sözlük ve içindeki scores liste.
- [ ] dump dosya nesnesiyle, dumps metin üretmek için kullanılmış.
- [ ] Geri gelen değer aslına eşit; yalnız dosyanın görünüşüne bakılarak başarı sayılmamış.
- [ ] Özel sınıf örneklerinin doğrudan aynı yöntemle desteklendiği varsayılmamış; pickle notu kod çalıştırma olasılığıyla ilişkilendirilmiş.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
