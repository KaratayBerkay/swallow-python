# Görev 16.1.4: Kullanıcı ve sistem özelleştirmesinin kapsamını ayır

**Odak:** sitecustomize/usercustomize yeri, sıra ve -s ile kullanıcı özelleştirmesini devre dışı bırakma.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:16.1.3](../16.1.3-the-interactive-startup-file/README.md).

## Tek görev

1. site.getusersitepackages() ile yalnız kullanıcı paket dizininin yolunu öğren.

2. Dosya oluşturmadan özelleştirme planı yaz: sistem yöneticisinin sitecustomize dosyası, kullanıcının usercustomize dosyası, bunların sırası ve -s ile başlatma durumunda ne değişeceği.

3. PYTHONSTARTUP ile bu iki dosyanın etki alanını karşılaştır.

## Geçiş ölçütleri

- [ ] Yol mevcut yorumlayıcıdan alınmış; örnekteki /home/user yolu kopyalanmamış.
- [ ] sitecustomize önce, usercustomize sonra; kullanıcı dosyası kullanıcı site-packages alanıyla ilişkili.
- [ ] -s kullanıcı özelleştirmesini engelliyor; tüm sistem özelleştirmesini kaldırdığı iddia edilmemiş.
- [ ] PYTHONSTARTUP etkileşimli oturuma özgü, customization modülleri daha geniş başlangıç kapsamına sahip.
- [ ] Kalıcı sistem/kullanıcı başlangıç dosyası yazılmadan plan üzerinden doğrulama yapılmış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
