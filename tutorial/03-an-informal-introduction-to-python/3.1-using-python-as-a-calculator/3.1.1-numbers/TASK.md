# Görev 3.1.1: Bir siparişin hesabını yorumlayıcıda çıkar

**Odak:** Aritmetik, işlem önceliği, int/float, atama, bölüm-kalan, üs ve REPL içindeki _.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:3](../../README.md).
- Ön bilgi: [t:2.1](../../../02-using-the-python-interpreter/2.1-invoking-the-interpreter/README.md).

## Tek görev

1. Yeni bir REPL oturumunda 29 ürünü 4 kişilik paketlere ayıran hesabı yap: gerçek bölüm, tam paket sayısı, kalan ve geri birleştirilen toplam.

2. Sonra fiyatı 80.0 ve vergi oranı 0.125 olan tek ürünün vergisini hesapla; bir sonraki ifadede _ ile vergili toplamı bul ve iki basamağa yuvarla.

3. Son olarak -4**2 ile (-4)**2 ve 30 - 6*3 ile (30 - 6)*3 sonuçlarını karşılaştır.

4. Tanımlanmamış bir adı ayrı bir girişte dene.

## Geçiş ölçütleri

- [ ] Bölüm 7.25, tam paket 7, kalan 1, geri birleştirme 29.
- [ ] Atama satırlarının REPL içinde kendiliğinden çıktı vermediği ve / sonucunun float olduğu açıklanmış.
- [ ] Vergi 10.0, toplam 90.0; _ önceki gösterilen sonucu kullanıyor ve ona doğrudan atama yapılmamış.
- [ ] Üs sonuçları -16 ve 16; parantezin önceliği değiştirmesi açıklanmış.
- [ ] Tanımsız ad NameError veriyor; Decimal ve Fraction yalnızca adı geçen türler olarak kalıyor.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
