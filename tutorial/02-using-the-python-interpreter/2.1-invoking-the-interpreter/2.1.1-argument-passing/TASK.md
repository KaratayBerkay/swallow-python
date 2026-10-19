# Görev 2.1.1: Komutun programa bıraktığı argümanları izle

**Odak:** sys.argv içeriği, ilk eleman ve yorumlayıcı seçenekleri ile program argümanlarının sınırı.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:2.1](../README.md).

## Tek görev

1. Şu başlatmalar için sys.argv değerlerini kâğıt üzerinde çıkar: python demo.py red 7; python -c "import sys" -v; python -m paket.arac red; python - red; argümansız etkileşimli oturum. -m örneğinde bulunan modül dosyasının yolunu /calisma/paket/arac.py kabul et.

2. Her satırda yorumlayıcının tükettiği seçeneklerle programa kalanları ayır.

3. Henüz öğretilmeyen liste işleme kodu yazman gerekmiyor.

## Geçiş ölçütleri

- [ ] Dosya örneğinde demo.py, red ve 7 metin olarak yer alıyor.
- [ ] -c, standart girdi ve etkileşimli oturumun ilk elemanları sırasıyla -c, - ve boş metin.
- [ ] -m için ilk eleman /calisma/paket/arac.py; sonraki argüman red.
- [ ] -c sonrasındaki -v program argümanı olarak kalıyor; sayısal görünen 7 dönüştürülmeden metin.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
