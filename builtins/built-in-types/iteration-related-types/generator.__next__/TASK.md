# Görev b:2.6.4: generator.__next__ durum geçişini kanıtla

## Önce

[b:2.6](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

aşağıdaki generatorı generatorını kur. Oluşturma anını ve üç next çağrısını izle; son hatanın value alanını göster. Sonuçları çağrı -> durulan nokta -> sonraki durum tablosuyla göster.

```python
def g():
    yield 4
    yield 6
    return 9
```

## Geçiş ölçütleri

- [ ] Oluşturma gövdeyi çalıştırmaz; çağrılar 4,6 ve value=9 olan StopIteration üretir.
- [ ] Çağrı ve tüketim/ilerleme anı birbirinden ayrılmıştır.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
