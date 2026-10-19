# Görev 9.3.4: Kaydedilen metodun hangi nesneye bağlı kaldığını göster

**Odak:** Bağlı metot, self argümanının eklenmesi ve sonradan çağırma.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:9.3.3](../9.3.3-instance-objects/README.md).

## Tek görev

1. name alanını tutan ve read(self) ile döndüren küçük sınıf yaz. a ve b örneklerini oluştur; saved = a.read kaydet, a adını b nesnesine yeniden bağla. saved(), a.read() ve ClassName.read(b) sonuçlarını karşılaştır. saved oluşturulması sırasında read gövdesinin çalışıp çalışmadığını açıkla.

## Geçiş ölçütleri

- [ ] saved ilk nesnenin adını, a.read() ikinci nesnenin adını döndürüyor.
- [ ] ClassName.read(b), b.read() ile eşdeğer.
- [ ] Metot kaydında çağrı parantezi yok ve gövde henüz yürümüyor.
- [ ] Nesnenin ilk argüman olarak otomatik eklenmesi ve metot nesnesinin nesne/fonksiyon bağını saklaması açıklanmış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
