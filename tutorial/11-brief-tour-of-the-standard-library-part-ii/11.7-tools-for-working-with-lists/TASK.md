# Görev 11.7: Veri yapısını erişim ihtiyacına göre seç

**Odak:** array H, deque, bisect.insort ve heapq minimum alma.

## Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:11.6](../11.6-weak-references/README.md).
- Ön bilgi: [t:5.1.2](../../05-data-structures/5.1-more-on-lists/5.1.2-using-lists-as-queues/README.md).

## Tek görev

1. Tek bir görev listesi için dört görünüm üret: [4, 1, 3] sayılarını array("H", ...) içine koyup toplam ve dilimini al; üç adı deque kuyruğunda işleyip ilkini çıkar; sıralı [(10, "a"), (30, "c")] listesine bisect.insort ile (20, "b") ekle; [4, 1, 3] üzerinde heapify, heappush(0) ve iki heappop yap.

2. Her aracı hangi erişim ihtiyacı için seçtiğini açıkla.

## Geçiş ölçütleri

- [ ] array toplamı 8, dilimi aynı türde sayısal veri; homojen saklama belirtilmiş.
- [ ] Kuyruk ilk geleni çıkarıyor; orta indeks performansı listeyle aynı varsayılmamış.
- [ ] insort sıralı diziyi 10, 20, 30 düzeninde tutuyor.
- [ ] heapten çıkanlar 0, 1; bütün heap listesinin sıralı olması şart sayılmamış.
- [ ] BFS örneğini yeniden yazmak yerine bölümde gerçekten gösterilen işlemler değerlendirilmiş.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)
