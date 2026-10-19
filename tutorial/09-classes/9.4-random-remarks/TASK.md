# Görev 9.4: Nitelik aramasının önceliğini izle

**Odak:** Örnek niteliğinin sınıfı gölgelemesi, self üzerinden metot çağrısı ve sınıf dışındaki fonksiyon.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:9.3.5](../9.3-a-first-look-at-classes/9.3.5-class-and-instance-variables/README.md).
- Ön bilgi: [t:6](../../06-modules/README.md).

## Tek görev

1. Notebook sınıfının kopyasında bir örneğin category değerini "personal" yap; diğer örnek ve sınıf değerini kontrol et, sonra örnekteki niteliği sil. add_twice metodunun self.add_note çağrısını iki kez kullanmasını sağla.

2. Bölümdeki f1/g/h örneğini hazır iskelet olarak okuyup h ile g ilişkisinin ve metot içinden global ad aramasının nerede gerçekleştiğini açıkla.

## Geçiş ölçütleri

- [ ] Örnek ataması yalnız bir örneğin sınıf değerini gölgeliyor; del sonrası sınıf değeri tekrar görünüyor.
- [ ] add_twice tek örneğin listesine iki not ekliyor.
- [ ] self sözcüğünün özel anahtar değil anlaşılır adlandırma geleneği olduğu açıklanmış.
- [ ] Sınıfa bağlanan dış fonksiyonun metot olabilmesi ve h/g ortak fonksiyon referansı açıklanmış.
- [ ] Metotların global kapsamı sınıf sözlüğü değil tanımlandıkları modül; `__class__` nesnenin türüyle ilişkilendirilmiş.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
