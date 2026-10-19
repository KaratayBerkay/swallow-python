# Görev b:3.23: exec sözleşmesini uygula

## Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

`g={}; l={}` üzerinde sabit `kod` kodunu `exec(kod,g,l)` ile çalıştır. x ve oku hangi sözlüktedir? `l["oku"]()` çağrısını aynı sözlüğün hem globals hem locals olduğu yeni denemeyle karşılaştır.

```python
kod = "x=5\ndef oku():\n    return x"
```

## Geçiş ölçütleri

- [ ] Ayrı sözlükte x ve oku l içindedir, fonksiyon global araması g içinde x bulamaz: NameError.
- [ ] Tek sözlükte fonksiyon 5 döndürür; exec sonucu None olur.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)
