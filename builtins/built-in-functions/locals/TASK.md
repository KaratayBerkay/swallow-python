# Görev b:3.43: locals sözleşmesini uygula

## Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

Sürüm: Python 3.13 veya üzeri. Daha eski yorumlayıcıda yalnız bu sürüme bağlı kısmı gerekçeli yazılı iz ile çözebilirsin; çalıştırma kanıtını bekleyen olarak kaydet.

## Tek görev

Python 3.13+ için bir fonksiyonda `x=1; a=locals(); a["x"]=9; b=locals()` satırlarını izle. x, a["x"], b["x"] ve `a is b` değerlerini raporla. Modül düzeyindeki locals davranışıyla karşılaştır.

## Geçiş ölçütleri

- [ ] Fonksiyonda değerler 1, 9, 1, False olur; a değişikliği x adını yeniden bağlamaz.
- [ ] Modül düzeyinde locals global namespace ile aynıdır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
