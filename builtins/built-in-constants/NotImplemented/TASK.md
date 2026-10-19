# Görev b:1.4: Operatörün geri dönüş yolunu izle

## Önce

[b:1](../README.md) ve bu sayfanın açıklama/örnekleri.

Sürüm: Python 3.14 veya üzeri. Daha eski yorumlayıcıda yalnız bu sürüme bağlı kısmı gerekçeli yazılı iz ile çözebilirsin; çalıştırma kanıtını bekleyen olarak kaydet.

## Tek görev

Sol nesnenin __add__ metodu NotImplemented, sağ nesnenin __radd__ metodu 9 döndürüyor. `sol + sag` akışını yazılı izle. İki metot da NotImplemented döndürürse ne olur? Sabiti raise etmek, NotImplementedError yükseltmek ve bool bağlamına sokmakla karşılaştır.

## Geçiş ölçütleri

- [ ] Yansıyan işlem denenir ve 9 döner; iki taraf desteklemezse TypeError olur.
- [ ] NotImplemented bir exception değildir; raise etmek TypeError verir; NotImplementedError ayrı hata türüdür.
- [ ] Python 3.14+ bool(NotImplemented) TypeError verir; eski sürüm davranışı yeni sürüm beklentisi yerine sayılmaz.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
