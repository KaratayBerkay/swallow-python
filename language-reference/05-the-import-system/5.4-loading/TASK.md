# Görev 5.4: Yükleme hatasında yalnız başarısız modülü çıkar

**Odak:** Modül yaratma, metadata, yürütmeden önce cache, hata temizliği ve dönüş nesnesi.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.3.4](../5.3-searching/5.3.4-the-meta-path/README.md).

**Kaynak/ortam notu:** Bu README kodu yaklaşık bir akıştır ve loader=None durumunu unsupported diye kısaltıyor. Namespace paketler için 5.2.2 anlatımını koru; sözde kodu doğrudan çalışan tam importlib uygulaması sayma. load_module için 3.15 kaldırılma notu geçerlidir.

## Tek görev

1. README içindeki yükleme sözde kodunu çalıştırmadan bir olay izi çıkar.

2. A modülü yaratılıp cache içine konuyor; A yürürken B başarıyla yükleniyor; sonra A hata veriyor.

3. Cache içinde önceden C de var.

4. Hata sonrasında A/B/C durumunu yaz.

5. İkinci izde A yürütülürken yeniden A istenmesini, üçüncüde loaderın cache içindeki A nesnesini değiştirmesini ele al.

6. Reload hatasını ilk import hatasından ayır.

## Geçiş ölçütleri

- [ ] Sıra yaratma, metadata hazırlığı, cache kaydı, exec_module; kendini import cache üzerinden çözülüyor.
- [ ] A ilk yükleme hatasında çıkar, B ve önceden C kalır.
- [ ] Dönen nesne sys.modules üzerinden alındığından yürütmeye verilen nesneden farklı olabilir; bu ayrıntı CPython sınırıyla belirtilmiş.
- [ ] Reload hatasında kayıt aynı biçimde silinmiş varsayılmamış.
- [ ] Sözde koddaki loader=None/ImportError satırı bütün namespace paketlerine genellenmemiş.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
