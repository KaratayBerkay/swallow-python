# Görev 9.2.1: Kapsam izini tek değişiklikle yeniden çıkar

**Odak:** Yerel/nonlocal/global atamaların aynı örnekte ayrıştırılması.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:9.2](../README.md).

## Tek görev

1. README içindeki scope_test örneğinin kopyasında başlangıçtaki spam = "test spam" satırını "start" yap; do_nonlocal içindeki nonlocal bildirimini kaldır.

2. Dört çıktı satırını çalıştırmadan önce çıkar, sonra doğrula.

3. İkinci denemede yalnız bildirimi geri koy ve hangi satırların neden değiştiğini açıkla.

## Geçiş ölçütleri

- [ ] Bildirim yokken ilk üç dış gözlem start, son modül gözlemi global spam.
- [ ] nonlocal geri geldiğinde ikinci ve üçüncü gözlem nonlocal spam oluyor.
- [ ] Değişim print konumuyla değil atamanın hedef namespace alanıyla açıklanmış.
- [ ] Global atama daha önce modül düzeyinde spam bulunmasa da modül bağını oluşturuyor.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
