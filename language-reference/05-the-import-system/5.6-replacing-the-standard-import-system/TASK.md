# Görev 5.6: Aramayı sürdürmekle reddetmeyi ayır

**Odak:** Meta path değişimi, `__import__` değiştirme sınırı ve None/hata ayrımı.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.5.2](../5.5-the-path-based-finder/5.5.2-path-entry-finder-protocol/README.md).

## Tek görev

1. Gerçek import sistemini değiştirmeden üç gereksinim için tasarım seç: bütün standart arama düzenini değiştirmek; yalnız import ifadesinin davranışını değiştirmek; belirli bir modülü erken hookta engellemek.

2. Son gereksinimde find_spec None döndürürse sonraki finderın ne yapacağını, ModuleNotFoundError yükselirse ne olacağını adım adım yaz.

## Geçiş ölçütleri

- [ ] Bütün sistem için sys.meta_path, yalnız ifade için built-in `__import__` sınırı belirtilmiş.
- [ ] None aramaya devam ettirir; engelleme garantisi değildir.
- [ ] ModuleNotFoundError zinciri durdurur.
- [ ] importlib gibi diğer giriş yollarının `__import__` değişiminden etkilenmeyebileceği açıklanmış; canlı sistem değiştirilmemiş.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
