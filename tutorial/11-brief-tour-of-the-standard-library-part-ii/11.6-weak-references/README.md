## 11.6. Weak references

Python does automatic memory management (reference counting for most objects and garbage collection to eliminate cycles). The memory is freed shortly after the last reference to it has been eliminated.

This approach works fine for most applications but occasionally there is a need to track objects only as long as they are being used by something else. Unfortunately, just tracking them creates a reference that makes them permanent. The `weakref` module provides tools for tracking objects without creating a reference. When the object is no longer needed, it is automatically removed from a weakref table and a callback is triggered for weakref objects. Typical applications include caching objects that are expensive to create:

``` python
>>> import weakref, gc
>>> class A:
...     def __init__(self, value):
...         self.value = value
...     def __repr__(self):
...         return str(self.value)
...
>>> a = A(10)                   # create a reference
>>> d = weakref.WeakValueDictionary()
>>> d['primary'] = a            # does not create a reference
>>> d['primary']                # fetch the object if it is still alive
10
>>> del a                       # remove the one reference
>>> gc.collect()                # run garbage collection right away
0
>>> d['primary']                # entry was automatically removed
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    d['primary']                # entry was automatically removed
  File "C:/python315/lib/weakref.py", line 46, in __getitem__
    o = self.data[key]()
KeyError: 'primary'
```
> Code: [init.py](init.py)

<!-- learning-task:start -->
### Bölüm görevi

**Görev 11.6: İzleyen tablonun nesneyi yaşatıp yaşatmadığını göster**

**Odak:** Güçlü/zayıf referans, WeakValueDictionary ve son güçlü bağın silinmesi.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:11.5](../11.5-logging/README.md).
- Ön bilgi: [t:9.1](../../09-classes/9.1-a-word-about-names-and-objects/README.md).

#### Tek görev

1. Bölümdeki A sınıfıyla bir nesne oluştur; onu weakref.WeakValueDictionary içinde tut.

2. Ayrıca keeper adını aynı nesneye bağla.

3. İlk adı silip gc.collect sonrası weak tabloyu kontrol et; sonra keeper adını da sil, gc.collect yapıp tekrar bak.

4. Deneyi REPL içindeki son sonuç referansından etkilenmemesi için ayrı bir betikte yap.

#### Geçiş ölçütleri

- [ ] keeper varken weak tablodan erişim mümkün.
- [ ] Son güçlü bağ silinince anahtara erişim KeyError.
- [ ] weak tabloya koymanın nesneyi tek başına yaşatmadığı açıklanmış.
- [ ] gc.collect dönüşündeki belirli sayı beklenmemiş; yanlışlıkla saklanan nesne referansı sonucu bozmuyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../11.7-tools-for-working-with-lists/README.md)
<!-- learning-task:end -->
