# Görev 5.8: Ana modülü built-in modülle karıştırma

**Odak:** `__main__` başlangıçta oluşur; başlatma biçimiyle kimliği ilişkilidir.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.7](../5.7-package-relative-imports/README.md).
- Ön bilgi: [t:6.1.1](../../../tutorial/06-modules/6.1-more-on-modules/6.1.1-executing-modules-as-scripts/README.md).

## Tek görev

1. Normal import edilen helper modülü ile python helper.py olarak başlatılan dosya için ad çizimi yap.

2. Her durumda `__main__` hangisi, helper hangi adla bağlanıyor ve `__name__` kontrolü hangi blokları yürütür? sys ile aynı biçimde başlangıçta hazır olmasının `__main__` modülünü neden built-in sınıfına sokmadığını açıkla.

## Geçiş ölçütleri

- [ ] Doğrudan dosya girişinde `__name__` `__main__`; normal importta helper.
- [ ] Ana modülün başlatma seçenekleriyle değişmesi belirtilmiş.
- [ ] Başlangıçta hazırlanma ile built-in modül olma ayrı tutulmuş.
- [ ] Henüz alt bölümdeki `__spec__` varyantlarını ezberden üretmek gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
