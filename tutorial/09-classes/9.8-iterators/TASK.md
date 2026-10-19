# Görev 9.8: Tükenen iteratorü yeniden kullanmayı dene

**Odak:** Iterable/iterator, iter/next, `__iter__`/`__next__`, saklanan durum ve StopIteration.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:9.7](../9.7-odds-and-ends/README.md).
- Ön bilgi: [t:8.4](../../08-errors-and-exceptions/8.4-raising-exceptions/README.md).

## Tek görev

1. Bölümdeki Reverse sınıfından yola çıkarak sırayla 0 ile limit arasındaki sayıları, limit hariç, veren Counter iteratorü yaz. iter(self) kendisini döndürsün; sınırda StopIteration yükseltsin. limit=2 için iki next ve üçüncü hata girişini dene; aynı nesne üzerinde for çalıştır, sonra yeni Counter(2) ile tekrar for çalıştır.

2. Boş sınırı da dene.

## Geçiş ölçütleri

- [ ] İlk iki değer 0 ve 1; üçüncü next StopIteration.
- [ ] Tükenmiş aynı nesnede for yeni değer üretmiyor; yeni nesne 0, 1 üretiyor.
- [ ] limit=0 hemen tükeniyor.
- [ ] Durum örnek üzerinde tutuluyor; for sona ermek için StopIteration kullanıyor.
- [ ] Yeni iterable üzerinde iter oluşturmakla tükenmiş iteratorü yeniden almak ayrılmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
