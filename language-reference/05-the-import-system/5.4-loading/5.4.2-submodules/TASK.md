# Görev 5.4.2: Alt modülün iki erişim yolunun aynı nesneye çıktığını göster

**Odak:** Alt modül yüklenmesinin ebeveyn namespace üzerinde oluşturduğu bağ.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.4.1](../5.4.1-loaders/README.md).

## Tek görev

1. Bölümdeki spam örneğini kendi çalışma kopyanda kullan. import spam sonrasında spam.foo ve spam.Foo adlarını incele. sys.modules["spam.foo"] is spam.foo ve sys.modules["spam"] is spam ilişkilerini karşılaştır.

2. Bir sınıfın dışarı aktarılmasıyla alt modül bağının neden aynı olay olmadığını açıkla.

## Geçiş ölçütleri

- [ ] spam.foo modül, spam.Foo sınıf nesnesi.
- [ ] İki kimlik kontrolü de doğru.
- [ ] `__init__` yalnız Foo adını açıkça alsa bile alt modül ebeveynde foo niteliği olarak bağlı.
- [ ] Yerel kullanıcı adı ile ebeveyn modül niteliği ayrılmış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
