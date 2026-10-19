# Görev 6.1.1: Dosyanın iki giriş yolunu ayır

**Odak:** `__name__` == "`__main__`" koruması ve komut satırı argümanları.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:6.1](../README.md).
- Ön bilgi: [t:2.1.1](../../../02-using-the-python-interpreter/2.1-invoking-the-interpreter/2.1.1-argument-passing/README.md).

## Tek görev

1. counts.py dosyasında count_items işlevini koru; dosyanın sonuna bölümdeki `__main__` korumasıyla sys.argv[1:] öğe sayısını yazdıran kod ekle. python counts.py a b çalıştırması ile yeni REPL içinde import counts ve counts.count_items(["a", "b"]) çağrılarını karşılaştır.

## Geçiş ölçütleri

- [ ] Dosya olarak çalışınca 2 basıyor; import sırasında komut satırı işlemi çalışmıyor.
- [ ] Açık işlev çağrısı 2 döndürüyor.
- [ ] İki giriş yolunda `__name__` değerleri ve korumanın neden gerekli olduğu açıklanmış.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
