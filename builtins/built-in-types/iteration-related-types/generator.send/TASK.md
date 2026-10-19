# Görev b:2.6.5: generator.send durum geçişini kanıtla

## Önce

[b:2.6](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

aşağıdaki generatorı generatorını kur. Başlatılmamış örneğe send(7) dene; yeni örnekte next ardından send(7) uygula. Sonuçları çağrı -> durulan nokta -> sonraki durum tablosuyla göster.

```python
def g():
    x = yield 4
    yield x + 1
```

## Geçiş ölçütleri

- [ ] Başlatılmamış örnekte non-None send TypeError; next 4, send(7) 8 verir; x=7 olur.
- [ ] Çağrı ve tüketim/ilerleme anı birbirinden ayrılmıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
