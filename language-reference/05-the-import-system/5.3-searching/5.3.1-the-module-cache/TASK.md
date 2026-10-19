# Görev 5.3.1: Eksik cache kaydıyla None kaydını ayır

**Odak:** sys.modules başarı/None/eksik durumları, silme ile nesne ömrü ve reload kimliği.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [r:5.3](../README.md).
- Ön bilgi: [t:9.1](../../../../tutorial/09-classes/9.1-a-word-about-names-and-objects/README.md).

## Tek görev

1. Gerçek sys.modules üzerinde değişiklik yapmadan bir durum tablosu hazırla: x anahtarı modül nesnesi gösteriyor; x değeri None; x anahtarı yok.

2. Her birinin sonraki import sonucunu yaz.

3. Sonra eski modül nesnesine old referansı tutulurken cache anahtarı silinip yeniden import ve importlib.reload senaryolarının kimlik ilişkisini çiz.

## Geçiş ölçütleri

- [ ] Modül nesnesi varsa arama erken döner; None doğrudan ModuleNotFoundError; eksik kayıt aramaya devam.
- [ ] Cache silme eski nesneyi eldeki başka bağlardan yok etmiyor.
- [ ] Silip yeniden import yeni nesne; reload aynı modül nesnesini yeniden başlatır.
- [ ] Cache anahtarı ile yerel değişken adının yaşamı ayrılmış; canlı modül cache değiştirme gerekmiyor.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)
