# Görev 5.2.2: Ayrı konumlardan tek namespace paketi kurulduğunu izle

**Odak:** Namespace portion, `__init__` yokluğu, dinamik `__path__` ve iç içe paket.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.2.1](../5.2.1-regular-packages/README.md).

## Tek görev

1. Yazılı bir import haritası çiz: /a/parent/one ve /b/parent/two var; parent dizinlerinde `__init__`.py yok, /a ve /b arama yolunda. parent ve iki alt öğenin nasıl aynı ad ağacında birleştiğini göster.

2. Sonra arama yoluna /c eklenip /c/parent/three bulunduğunda sonraki aramanın neyi yeniden değerlendireceğini açıkla.

3. Regular paket içindeki __init__siz alt klasör durumunu da çizime ekle.

## Geçiş ölçütleri

- [ ] parent tek namespace paket, iki kök ayrı portion olarak gösterilmiş.
- [ ] parent için zorunlu tek bir fiziksel dizin veya `__init__` varsayılmamış.
- [ ] `__path__` düz sabit liste sanılmamış; ebeveyn yolu değişince yeni portion araması açıklanmış.
- [ ] Regular paket içinde namespace alt paket olasılığı doğru; yeni finder uygulamak gerekmiyor.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
