## `set.remove`

```
set.remove(elem, /)
```

Remove element *elem* from the set.  Raises [KeyError](https://docs.python.org/3.15/builtins/exceptions.html#KeyError) if *elem* is
not contained in the set.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.11.3: remove ile üyeliği güncelle**

#### Önce

[b:2.11](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

`s={1,2}; diger=s` ile başla. İlk `s.remove(1)` çağrısının dönüşünü ve iki adın üyelerini kaydet. Ardından aynı s üzerinde `s.remove(9)` çağır; sonucu veya hata türünü göster.

#### Geçiş ölçütleri

- [ ] İlk üyeler `{2}`, ilk dönüş None; küme sırasına dayalı beklenti yok.
- [ ] Eksik öğe KeyError verir.
- [ ] Diger aynı kümenin güncel üyelerini görür.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../frozenset.isdisjoint/README.md)
<!-- learning-task:end -->
