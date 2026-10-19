# Görev 9.3.1: Sınıf gövdesinin ne zaman yürüdüğünü göster

**Odak:** class bildiriminin yürütülmesi, yeni namespace ve sınıf adının dış kapsamda bağlanması.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:9.2.1](../../9.2-python-scopes-and-namespaces/9.2.1-scopes-and-namespaces-example/README.md).

## Tek görev

1. label = "outside" ile başla.

2. Bir class Lesson gövdesinde label = "inside" ve print(label) kullan; gövde bittikten sonra print(label) ile dış değeri göster.

3. Aynı sınıf bildirimini if False içine koyan ayrı bir taslakta sınıfın oluşup oluşmayacağını açıklayıp dene.

4. Bu adımda örnek oluşturma gerekmiyor.

## Geçiş ölçütleri

- [ ] İlk çıktı inside, sonraki outside.
- [ ] Sınıf gövdesinin atamaları kendi namespace alanında; dış label korunmuş.
- [ ] Sınıf bildirimi yürütülünce dış kapsamda Lesson adı bağlanıyor.
- [ ] False dalındaki tanım yürütülmediği için yeni sınıf bağlanmıyor; class yalnız metin şablonu sayılmamış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
