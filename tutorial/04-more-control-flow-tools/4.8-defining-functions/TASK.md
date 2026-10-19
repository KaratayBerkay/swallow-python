# Görev 4.8: Yazdırılan sonuçla dönen sonucu ayır

**Odak:** def/çağrı, parametre, yerel adlar, return/None, fonksiyon alias ve listeye append.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:3.2](../../03-an-informal-introduction-to-python/3.2-first-steps-towards-programming/README.md).
- Ön bilgi: [t:4.6](../4.6-pass-statements/README.md).

## Tek görev

1. limit altındaki çift sayıları liste olarak döndüren even_numbers(limit) yaz; 0 ile başlatıp while içinde 2 ekleyebilirsin.

2. Kısa bir docstring ekle. f = even_numbers ile ikinci bir ad ver. 0, 1 ve 7 için sonuçları al.

3. Ardından yalnızca aynı sayıları yazdıran, return kullanmayan bir sürüm yaz ve print ile dönüşünü göster.

4. Dışarıda limit = 100 varken fonksiyon parametresinin neden onu değiştirmediğini açıkla.

## Geçiş ölçütleri

- [ ] Sonuçlar [], [0], [0, 2, 4, 6]; sınır dışarıda kalıyor.
- [ ] f aynı fonksiyonu çağırıyor; f ile çağrının sonucu birbirinden ayrılmış.
- [ ] Yazdıran sürümün dönüşü None; return ifadesiz kullanıldığında da aynı.
- [ ] Parametre ve gövde içindeki atamalar yerel; fonksiyonun gövdesi tanımda değil çağrıda yürütülüyor.
- [ ] Her çağrıda sonuç listesinin yeniden oluştuğu ve append ile biriktiği açıklanmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
