### 16.1.4. The Customization Modules

Python provides two hooks to let you customize it: sitecustomize and usercustomize. To see how it works, you need first to find the location of your user site-packages directory. Start Python and run this code:

``` python
>>> import site
>>> site.getusersitepackages()
'/home/user/.local/lib/python3.x/site-packages'
```
> Code: [site_example.py](site_example.py)

Now you can create a file named `usercustomize.py` in that directory and put anything you want in it. It will affect every invocation of Python, unless it is started with the `-s` option to disable the automatic import.

sitecustomize works in the same way, but is typically created by an administrator of the computer in the global site-packages directory, and is imported before usercustomize. See the documentation of the `site` module for more details.

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 16.1.4: Kullanıcı ve sistem özelleştirmesinin kapsamını ayır**

**Odak:** sitecustomize/usercustomize yeri, sıra ve -s ile kullanıcı özelleştirmesini devre dışı bırakma.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:16.1.3](../16.1.3-the-interactive-startup-file/README.md).

##### Tek görev

1. site.getusersitepackages() ile yalnız kullanıcı paket dizininin yolunu öğren.

2. Dosya oluşturmadan özelleştirme planı yaz: sistem yöneticisinin sitecustomize dosyası, kullanıcının usercustomize dosyası, bunların sırası ve -s ile başlatma durumunda ne değişeceği.

3. PYTHONSTARTUP ile bu iki dosyanın etki alanını karşılaştır.

##### Geçiş ölçütleri

- [ ] Yol mevcut yorumlayıcıdan alınmış; örnekteki /home/user yolu kopyalanmamış.
- [ ] sitecustomize önce, usercustomize sonra; kullanıcı dosyası kullanıcı site-packages alanıyla ilişkili.
- [ ] -s kullanıcı özelleştirmesini engelliyor; tüm sistem özelleştirmesini kaldırdığı iddia edilmemiş.
- [ ] PYTHONSTARTUP etkileşimli oturuma özgü, customization modülleri daha geniş başlangıç kapsamına sahip.
- [ ] Kalıcı sistem/kullanıcı başlangıç dosyası yazılmadan plan üzerinden doğrulama yapılmış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
